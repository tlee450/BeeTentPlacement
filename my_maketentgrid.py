#!/usr/bin/python3

import csv
import datetime
import math
import os
import traceback
import zipfile
from contextlib import redirect_stdout
from io import BytesIO, StringIO

from my_code import shapefile, utmish

import fpdf
import simplekml


class FileWriter(object):
    """ implements a simple class that allows us to write to files in a
        directory using the same call as zipfile, so we can switch between
        using zips and directories easily
    """
    def __init__(self):
        pass

    def __enter__(self):
        # do nothing since there's really no setup and cleanup
        # to do in this class
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # no cleanup necesary
        pass

    def writestr(self, filename, data):
        """
            Create a file called filename relative to self._path
            write data to it. Either bytes or str, which is 
            implicitly converted to UTF-8.
        """
        #combined_path = os.path.join(self._path, filename)
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        file=open(filename,"wb")
        with file:
            if isinstance(data,str):
                file.write(data.encode('UTF-8'))
            else:
                file.write(data)

class BeePDF(fpdf.FPDF):
    def __init__(self, orientation, units, papersize):
        super().__init__(orientation, units, papersize)
        self.last_x=None
        self.last_y=None

    def move_to(self, x,y):
        self.last_x = x
        self.last_y = y

    def line_to(self, x,y):
        self.line(self.last_x, self.last_y, x, y)
        self.last_x = x
        self.last_y = y

def ll_at( lon1, lat1, bearing, distance):
    R = 6378137 #Radius of the Earth in metres
    brng = math.radians(bearing)

    #lat2  52.20444 - the lat result I'm hoping for
    #lon2  0.36056 - the long result I'm hoping for.

    lat1 = math.radians(lat1) #Current lat point converted to radians
    lon1 = math.radians(lon1) #Current long point converted to radians

    lat2 = math.asin( math.sin(lat1)*math.cos(distance/R) +
         math.cos(lat1)*math.sin(distance/R)*math.cos(brng))

    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(distance/R)*math.cos(lat1),
                 math.cos(distance/R)-math.sin(lat1)*math.sin(lat2))

    return (math.degrees(lon2), math.degrees(lat2))

#name is just the date in MMDDYY format
def make_files(myzip, field_path, name, origin):
    # 
    # create the default trimble files for field origin, etc
    myzip.writestr(f"{field_path}/origin.kml", 
                   "<kml>\n    <Placemark>\n        <name>"
                   f"{name}_0001</name>\n" + 
                   "        <Point>\n            <coordinates>"
                   f"{origin[0]:0.9f},{origin[1]:0.9f},761.049" +
                   "</coordinates>\n        </Point>\n    </Placemark>\n</kml>\n")

    myzip.writestr(f"{field_path}/{origin[0]:0.5f}E{origin[1]:0.5f}N761H.pos",
                   '')

    myzip.writestr(f"{field_path}/newField.ok", '')

def make_pdf_circle_bays(pdf_writer, field):
    """
        Draw the outline of the circle and male bays using the
        pdf_writer (instance of FPDF) onto the current field's PDF page
    """
    #TODO: cleaner, programmatic way to do this
    width = 8.5 * 72
    height = 11 * 72

    #make the entire circle fit on the page
    scale = 8/8.5*width / field['Radius'] / 2

    pdf_writer.set_line_width(0.5)
    pdf_writer.set_draw_color(0,0,0)

    if field['North_limit'] is not None:
        northlimit = field['North_limit']
    else:
        northlimit = field['Radius']

    if field['East_limit'] is not None:
        eastlimit = field['East_limit']
    else:
        eastlimit = field['Radius']

    if field['South_limit'] is not None:
        southlimit = field['South_limit']
    else:
        southlimit = field['Radius']

    if field['West_limit'] is not None:
        westlimit = field['West_limit']
    else:
        westlimit = field['Radius']

    # draw pivot point
    pdf_writer.ellipse(width/2-2,height/2-2,4,4,'DF')
    
    if field['pie_slice']:
        start_angle = 360 - field['pie_slice'][0] + 90
        end_angle = 360 - field['pie_slice'][1] + 90
        x = math.cos(math.radians(start_angle)) * field['Radius']
        y = math.sin(math.radians(start_angle)) * field['Radius']
        if x > eastlimit: x=eastlimit
        elif x < -westlimit: x = -westlimit
        
        if y > northlimit: y = northlimit
        elif y < -southlimit: y = -southlimit

        pdf_writer.move_to(x * scale + width/2,
                           -y * scale + height/2)

        pdf_writer.line_to(width/2, height/2)

        x = math.cos(math.radians(end_angle)) * field['Radius']
        y = math.sin(math.radians(end_angle)) * field['Radius']
        if x > eastlimit: x=eastlimit
        elif x < -westlimit: x = -westlimit
        
        if y > northlimit: y = northlimit
        elif y < -southlimit: y = -southlimit

        pdf_writer.line_to( x * scale + width/2,
                            -y * scale + height/2 )

        if start_angle < end_angle:
            if end_angle > 180: end_angle = -360 + end_angle
    else:
        start_angle = 360
        end_angle = 0

    x = math.cos(math.radians(start_angle)) * field['Radius']
    y = math.sin(math.radians(start_angle)) * field['Radius']
    if x > eastlimit: x=eastlimit
    elif x < -westlimit: x = -westlimit
    
    if y > northlimit: y = northlimit
    elif y < -southlimit: y = -southlimit

    pdf_writer.move_to(x * scale + width/2,
                      -y * scale + height/2)

    # if arc crosses 0, adjust

    pdf_writer.set_line_width(1)
    angle = start_angle
    while True:
        x = math.cos(math.radians(angle)) * field['Radius']
        y = math.sin(math.radians(angle)) * field['Radius']
        if x > eastlimit: x=eastlimit
        elif x < -westlimit: x = -westlimit
        
        if y > northlimit: y = northlimit
        elif y < -southlimit: y = -southlimit

        pdf_writer.line_to(x * scale + width/2,
                          -y * scale + height/2)

        angle -= 1
        if angle < end_angle: break
     
    pdf_writer.set_line_width(0.5)
    radius = field['Radius']
    radius_sqr = radius * radius
    sprayer_width = field['Sprayer_width']

    if field['spacing'] is not None:
        spacing = field['spacing']  #float(field['spacing']) * conv
    else:
        spacing = calculate_spacing(radius, sprayer_width, num_tents = field['# of Structures'])

    directional_offset = field['directional_offset']
    #if directional_offset:
    #    directional_offset = float(directional_offset) * conv
    #else:
    #    directional_offset = 0

    rotate = 0 - field['Seed_angle']
    rotate = (rotate + 180) % 360 - 180
    pie_slice = field['pie_slice']
    lat_shift = field['Lateral_offset']


    if field.get('Female_bays_per_width'):
        bays_per_sprayer_width = field['Female_bays_per_width']

        # Draw male bays
        pdf_writer.set_draw_color(0,0,230)
        rows = range(-int(radius / sprayer_width * bays_per_sprayer_width ) - 1,int(radius / sprayer_width * bays_per_sprayer_width) + 1)
        for r in rows:
            east = r * sprayer_width / bays_per_sprayer_width + sprayer_width / bays_per_sprayer_width / 2
            north = radius

            east1 = east * math.cos(math.radians(rotate)) - north * math.sin(math.radians(rotate))
            north1 = north * math.cos(math.radians(rotate)) + east * math.sin(math.radians(rotate))

            east2 = east * math.cos(math.radians(rotate)) + north * math.sin(math.radians(rotate))
            north2 = -north * math.cos(math.radians(rotate)) + east * math.sin(math.radians(rotate))

            if abs(east1 - east2) < 0.001: #north and south line
                # trim lines that are outside of the circle entirely
                if east1 > eastlimit or east1 < -westlimit: continue
                if north1 < -southlimit: north1 = -southlimit
                elif north1 > northlimit: north1 = northlimit

                if north2 < -southlimit: north2 = -southlimit
                elif north2 > northlimit: north2 = northlimit

            elif abs(north1 - north2) < 0.001: #east and west line
                #trim lines that are outside of the circle entirely
                if north1 > northlimit or north1 < -southlimit: continue

                if east1 < -westlimit: east1 = -westlimit
                elif east1 > eastlimit: east1 = eastlimit

                if east2 < -westlimit: east2 = -westlimit
                elif east2 > eastlimit: east2 = eastlimit
            else: #some other angle that we can calculate slope
                # if midpoint of bay is outside the radius, we can
                # safely skip it
                e = (east2 + east1) / 2
                n = (north2 + north1) / 2
                #print (east2, east1, e, n)

                if e*e + n*n > radius_sqr: continue

                #TODO: if it's outside the pie skip

            """
            if east1 < -westlimit: east1 = -westlimit
            elif east1 > eastlimit: east1 = eastlimit

            if east2 < -westlimit: east2 = -westlimit
            elif east2 > eastlimit: east2 = eastlimit

            if north1 < -southlimit: north1 = -southlimit
            elif north1 > northlimit: north1 = northlimit

            if north2 < -southlimit: north2 = -southlimit
            elif north2 > northlimit: north2 = northlimit
            """

            pdf_writer.line(east1 * scale + width/2, -north1 * scale + height/2,
                            east2 * scale + width/2, -north2 * scale + height/2)
        
    pdf_writer.set_draw_color(0,0,0)
    pdf_writer.set_font("Arial")
    pdf_writer.set_font_size(24)
    pdf_writer.text(72,72,field['Name'].strip())


def make_tents(myzip, trimble_path, field_name, pivotpoint, radius, width, lat_shift, angle, pie_slice=None, **kwargs):
    """
    Generate tent placement outputs (KML, shapefile, CSV, and optional PDF overlay) around a circular field and
    package them into a Trimble-style ZIP archive.

    Parameters
    ----------
    myzip : zipfile.ZipFile
        Open ZIP-file object to write generated files into.
    trimble_path : str
        Directory path inside the ZIP for Trimble-style structure.
    field_name : str
        Name of the field; used to name subdirectories and files.
    pivotpoint : tuple of float
        (longitude, latitude) of the field center in decimal degrees.
    radius : float
        Maximum radius of the circular field, in meters.
    width : float
        Sprayer width or nominal distance between rows of tents, in meters.
    lat_shift : float
        Lateral offset from the centerline to the first row of tents, in meters.
    angle : float
        Rotation angle (degrees clockwise from north) for the tent grid.
    pie_slice : tuple of float, optional
        (start_angle, end_angle) in degrees to restrict tent placement to a wedge of the circle.
        If None, tents fill the entire circle.
    **kwargs : dict
        Optional keyword arguments:
            spacing (float): explicit row spacing in meters.
            num_tents (int): hint for spacing calculation if spacing not provided.
            eastlimit, westlimit, northlimit, southlimit (float): clipping extents in meters.
            pdf (fpdf.FPDF): PDF writer for drawing tent markers on a page.
            exp_rows (iterable): explicit list of row indices instead of auto-generated rows.
            exp_rows_start_odd (bool): starting phase for experimental rows (True=odd offset first).
            directional_offset (float): additional offset for column placement, in meters.

    Returns
    -------
    None
    """

    # Read or default the clipping limits (meters)
    eastlimit  = kwargs.get('eastlimit', radius)
    northlimit = kwargs.get('northlimit', radius)
    westlimit  = kwargs.get('westlimit', radius)
    southlimit = kwargs.get('southlimit', radius)

    # PDF overlay setup
    pdf = kwargs.get('pdf', None)
    pdf_width, pdf_height = 8.5 * 72, 11 * 72       # Letter size in points
    scale = 8 * 72 / (radius * 2)                   # Scale so 8" fits diameter

    # Convert pivot lon/lat to local east/north origin
    easting, northing = utmish.from_lonlat(pivotpoint[0], pivotpoint[1], pivotpoint[0])
    radius_sqr = radius * radius

    # Determine spacing: explicit or calculated
    num_tents = kwargs.get('num_tents', None)
    if kwargs.get('spacing') is not None:
        spacing = kwargs['spacing']
    else:
        spacing = calculate_spacing(radius, width, num_tents=num_tents)

    # Normalize rotation to [-180,180)
    rotate = (-angle + 180) % 360 - 180

    # CSV writer for tent listing
    csv_buf = StringIO()
    csv_writer = csv.DictWriter(csv_buf, fieldnames=['GPS Position','Tent'])
    csv_writer.writeheader()

    # SimpleKML for Google Earth output
    kml = simplekml.Kml()

    # In-memory shapefile streams
    shp_buf, shx_buf, dbf_buf = BytesIO(), BytesIO(), BytesIO()
    shp_writer = shapefile.Writer(shp=shp_buf, shx=shx_buf, dbf=dbf_buf, shapeType=1)
    # Define shapefile fields
    shp_writer.field('Date','D')
    shp_writer.field('Time','C',size=10)
    shp_writer.field('Version','C',size=8)
    shp_writer.field('Id','N')
    shp_writer.field('Name','C',size=32)
    shp_writer.field('Latitude','N',decimal=8)
    shp_writer.field('Longitude','N',decimal=8)
    shp_writer.field('Height','N',decimal=3)
    shp_writer.field('AlarmRad','N',decimal=4)
    shp_writer.field('WarningRad','N',decimal=4)
    shp_writer.field('Status_Text','C',size=8)
    shp_writer.field('Visible','N')

    tent_id = 0
    pid = 3062  # starting ID for shapefile records

    # Determine row indices: explicit or auto-generated
    exp_rows = kwargs.get('exp_rows')
    if exp_rows:
        rows = exp_rows
        odd = kwargs.get('exp_rows_start_odd', True)
    else:
        # rows span full field width in multiples of 'width'
        limit = int(radius / width)
        rows = range(-limit, limit+1)

    directional_offset = kwargs.get('directional_offset', 0)

    # Loop over each row and column to place tents
    for r in rows:
        # Odd rows are shifted by half-spacing
        odd = odd if exp_rows else (r % 2 != 0)
        for c in range(-int(radius/spacing)-1, int(radius/spacing)+1):
            # Compute unrotated east/north offsets
            base_east = r*width + lat_shift
            base_north = c*spacing + (spacing/2 if odd else 0) + directional_offset
            # Rotate point around center
            ang_rad = math.radians(rotate)
            cosA, sinA = math.cos(ang_rad), math.sin(ang_rad)
            east = base_east*cosA - base_north*sinA
            north = base_north*cosA + base_east*sinA

            # Clip to circle radius
            if east*east + north*north > radius_sqr:
                continue
            # Clip to rectangular limits
            if east>eastlimit or east<-westlimit or north>northlimit or north<-southlimit:
                continue

            # If a pie_slice is defined, enforce angular wedge
            if pie_slice:
                theta = math.degrees(math.atan2(east, north)) % 360
                start, end = pie_slice
                if start <= end:
                    if not(start <= theta <= end): continue
                else:
                    # wedge wraps past 360
                    if not(theta >= start or theta <= end): continue

            # Draw on PDF overlay if provided
            if pdf:
                pdf.set_draw_color(255,0,0)
                pdf.set_fill_color(255,0,0)
                x_pt = east*scale + pdf_width/2 - 2
                y_pt = -north*scale + pdf_height/2 - 2
                pdf.ellipse(x_pt, y_pt, 4, 4, 'DF')

            # Convert back to lon/lat for output
            lon, lat = utmish.to_lonlat(easting+east, northing+north, pivotpoint[0])

            # Add a KML placemark for this tent
            kml.newpoint(name=f"tent {tent_id}", coords=[(lon, lat)])

            # Write shapefile record and point
            shp_writer.record(Date=datetime.date.today(), Time="12:00:00pm",
                              Version="7.78.002", Id=pid, Name=f"Tree_{pid}",
                              Latitude=lat, Longitude=lon, Height=761.064,
                              AlarmRad=0, WarningRad=10.0, Status_Text='', Visible=1)
            shp_writer.point(lon, lat)

            # Write CSV row
            csv_writer.writerow({'GPS Position': f"{lat:.7f},{lon:.7f}", 'Tent': tent_id})

            # Increment counters
            pid += 1
            tent_id += 1

        if exp_rows:
            odd = not odd  # flip starting phase for next explicit row

    # Finalize outputs into the ZIP
    myzip.writestr(f"{trimble_path}/googleearth/{field_name}.kml", kml.kml())
    shp_writer.close()
    myzip.writestr(f"{trimble_path}/AgGPS/Data/TNTBees/BeeTents/{field_name}/PointFeature.shp", shp_buf.getvalue())
    myzip.writestr(f"{trimble_path}/AgGPS/Data/TNTBees/BeeTents/{field_name}/PointFeature.shx", shx_buf.getvalue())
    myzip.writestr(f"{trimble_path}/AgGPS/Data/TNTBees/BeeTents/{field_name}/PointFeature.dbf", dbf_buf.getvalue())
    myzip.writestr(f"{trimble_path}/spreadsheets/{field_name}.csv", csv_buf.getvalue().encode('utf-8'))


def make_line(myzip, field_path, pivotpoint, lat_offset, angle):
    # create starting point for grid
    easting, northing = utmish.from_lonlat(pivotpoint[0], pivotpoint[1], pivotpoint[0])

    kml = simplekml.Kml()

    shp = BytesIO()
    shx = BytesIO()
    dbf = BytesIO()

    w = shapefile.Writer(shp = shp, shx = shx, dbf = dbf, shapeType=3 )
    w.field("Date", "D")
    w.field("Time", "C", size=10)
    w.field("Version", "C", size=8)
    w.field("Id", "N")
    w.field("Length","N", decimal=3)
    w.field("Dist1","N", decimal=3)
    w.field("Dist2","N", decimal=3)

    rotate = 0 - angle
    rotate = (rotate + 180) % 360 - 180

    # make an AB line 100 metres long
    east1 = lat_offset
    north1 = 0

    east2 = lat_offset
    north2 = 100

    # rotate the AB line about the pivot point
    east1r = east1 * math.cos(math.radians(rotate)) - north1 * math.sin(math.radians(rotate))
    north1r = north1 * math.cos(math.radians(rotate)) + east1 * math.sin(math.radians(rotate))
    east2r = east2 * math.cos(math.radians(rotate)) - north2 * math.sin(math.radians(rotate))
    north2r = north2 * math.cos(math.radians(rotate)) + east2 * math.sin(math.radians(rotate))
    
    # convert grid coords back to lat lon
    ab1 = utmish.to_lonlat(east1r + easting, north1r + northing, pivotpoint[0])
    ab2 = utmish.to_lonlat(east2r + easting, north2r + northing, pivotpoint[0])

    kml.newlinestring(name = "AB Line", coords = [ ab1, ab2])
    w.record(Date=datetime.date.today(), Time="12:00:00pm",Version="7.78.002",Id=0, Length=100, Dist1=0, Dist2=0)
    w.line( [ [ ab1, ab2 ] ])

    myzip.writestr("%s/Swaths.kml" % field_path, kml.kml())    
    w.close()
    myzip.writestr('%s/Swaths.dbf' % field_path, dbf.getvalue())
    myzip.writestr('%s/Swaths.shp' % field_path, shp.getvalue())
    myzip.writestr('%s/Swaths.shx' % field_path, shx.getvalue())

def calculate_spacing(radius, width, factor=1, num_tents = None):
    """
        Calculate total length of all the passes from pivot
        point outward, every "width" meters (sprayer passes).
        Divide that by the number of acres in the circle to 
        calculate the distance between tents as a factor of
        the sprayer width.

        factor allows tweaking the spacing, either increasing it, or
        decreasing it
    """
    c = 0
    total = 0
    while c < radius:
        total += math.sqrt(radius*radius-c*c)
        c += width

    total = total * 4 - radius*2
    if num_tents:
        return total / num_tents * factor
    else:
        # otherwise 1 per acre
        return total / (math.pi * radius * radius / 4046.87 + 1) * factor

def process_csvfile(csv_file, path = None, use_zip = None, timestamp = None, use_metric = False):

    output = StringIO()

    if use_metric:
        conv = 1

    else:
        conv = 0.3048

    with redirect_stdout(output):
        fields = []
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # perform some type conversions, and validate some fields
                # and calculate convenience entries
                try:
                    row['PP_Longitude'] = float(row['PP_Longitude'])
                    row['PP_Latitude'] = float(row['PP_Latitude'])
                    row['Radius'] = float(row['Radius']) * conv
                    if row['Seed_angle'] == '':
                        print ("Warning! No seed angle supplied for {}. Assuming 0 degrees.".format(row['Name']))
                        row['Seed_angle'] = 0
                    else:
                        row['Seed_angle'] = float(row['Seed_angle'])
                    row['Sprayer_width'] = float(row['Sprayer_width']) * (0.3048 if not use_metric else 1.0)
                    if row['Pie_start'] != '' and row['Pie_end'] != '':
                        row['pie_slice'] = (int(row['Pie_start']),
                                            int(row['Pie_end']))
                    else:
                        row['pie_slice'] = None

                    def _f(val, default):
                        s = str(val).strip()
                        return default if s == '' else float(s) * conv

                    row['North_limit'] = _f(row.get('North_limit', ''), row['Radius'])
                    row['East_limit']  = _f(row.get('East_limit',  ''), row['Radius'])
                    row['South_limit'] = _f(row.get('South_limit', ''), row['Radius'])
                    row['West_limit']  = _f(row.get('West_limit',  ''), row['Radius'])


                    if row['Lateral_offset'] != '':
                        row['Lateral_offset'] = float(row['Lateral_offset']) * conv
                    else:
                        row['Lateral_offset'] = 0

                    if row['Female_bays_per_width'] != '':
                        row['Female_bays_per_width'] = float(row['Female_bays_per_width'])

                        if not row['Lateral_offset']:
                            # calculate it based on the width of the bays. This figures
                            # out where the tent is placed, just to the right-hand side
                            # of the male bay
                            row['Lateral_offset'] = row['Sprayer_width'] / float(row['Female_bays_per_width']) / 2 * 0.75
                    else:
                        row['Female_bays_per_width'] = None

                    if row['Experimental'] != '':
                        exp_rows = row['Experimental'].split(',')
                        exp_rows = [int(x) for x in exp_rows]
                        row['Experimental'] = exp_rows
                    else:
                        row['Experimental'] = None

                    if row['Experimental_start_odd'] != '':
                        row['Experimental_start_odd'] = True
                    else:
                        row['Experimental_start_odd'] = False

                    if row['# of Structures'] != '':
                        row['# of Structures'] = int(float(row['# of Structures']))

                        if row['pie_slice']:
                            # if we have a pie slice, extrapolate how many
                            # tents would cover the entire circle

                            start = row['pie_slice'][0]
                            end = row['pie_slice'][1]

                            if start > end:
                                arc_length = (360 - start) + end
                            else:
                                arc_length = end - start

                            row['# of Structures'] /= arc_length/360

                    else:
                        row['# of Structures'] = None

                    if 'spacing' not in row:
                        row['spacing'] = None
                    else:
                        if not row['spacing']:
                            row['spacing'] = None
                        else:
                            row['spacing'] = float(row['spacing']) * conv

                    val = row.get('directional_offset', '')
                    row['directional_offset'] = float(val) * conv if str(val).strip() != '' else 0

                    fields.append(row)
                except ValueError:
                    print ("Warning! {} has incomplete information. It will not be processed.".format(row['Name']))
                    print (traceback.format_exc())



        #for item in field_data:
        #    fields.append(dict(zip(data_items, item)))

        #zipfilename = '/tmp/beetents ' + datetime.date.today().isoformat() + ".zip"

        if not path:
            if not use_zip:
                # not using zip, place files in the same directory as the CSV file
                dirpath = os.path.join(os.path.dirname(os.path.abspath(csv_file)), "TNT")
            else:
                dirpath = "TNT"
        else:
            dirpath = path
            

        if use_zip:
            zipfilename = use_zip
            if timestamp:
                zipname_parts = os.path.splitext(zipfilename)
                zipfilename = f"{zipname_parts[0]}-{datetime.date.today().isoformat()}{zipname_parts[1]}"
                
            print (f"Writing output to {zipfilename}.")
            writer = zipfile.ZipFile(zipfilename, mode='w')
        else:
            if timestamp:
                dirpath = dirpath+"-"+datetime.date.today().isoformat()

            print ()
            if (use_metric):
                print ("Using METRIC units for distance (metres).")
            else:
                print ("Using IMPERIAL units for distance (feet).")

            print (f"Writing output to folder {dirpath}.")
            print ()
            writer = FileWriter()


        width, height = 612,792 #72 dpi

        # TODO place this is the zip file
        if use_zip:
            pdfpath = os.path.dirname(os.path.abspath(use_zip))
        else:
            pdfpath = dirpath
        if not os.path.exists(pdfpath):
            os.makedirs(pdfpath)
            
        pdfwriter = BeePDF('P','pt','Letter')
        #surface = cairo.PDFSurface (os.path.join(pdfpath, "tntfields.pdf"), width, height)

        with writer:
            for field in fields:
                print ("Processing: {} ({:f}, {:f})".format(field['Name'].strip(), field['PP_Longitude'], field['PP_Latitude']))
                pdfwriter.add_page()
                make_pdf_circle_bays(pdfwriter, field)

                make_files(writer, os.path.join(dirpath, "AgGPS/Data/TNTBees/BeeTents/{}".format(field['Name'].strip())), 
                                   field['Name'].strip(), 
                                   (float(field['PP_Longitude']), float(field['PP_Latitude'])))

                #print (field['# of Structures'])
                make_tents(writer, dirpath, 
                                  field['Name'].strip(),
                                  pivotpoint=(field['PP_Longitude'], field['PP_Latitude']), 
                                  radius=field['Radius'], width=field['Sprayer_width'],  
                                  lat_shift=field['Lateral_offset'], angle=field['Seed_angle'], 
                                  pie_slice=field['pie_slice'],
                                  northlimit=field['North_limit'],
                                  eastlimit=field['East_limit'],
                                  southlimit=field['South_limit'],
                                  westlimit=field['West_limit'],
                                  exp_rows = field['Experimental'],
                                  exp_rows_start_odd = field['Experimental_start_odd'],
                                  pdf=pdfwriter,
                                  num_tents = field['# of Structures'],
                                  spacing = field['spacing'],
                                  directional_offset = field['directional_offset'],

                                  ) 

                make_line(writer, os.path.join(dirpath, "AgGPS/Data/TNTBees/BeeTents/{}".format(field['Name'].strip())), 
                                 (field['PP_Longitude'], field['PP_Latitude']), 
                                 field['Lateral_offset'], field['Seed_angle'])

            if not use_zip:
                pdfwriter.output(os.path.join(dirpath,'TNTFields.pdf'),'F')
            else:
                writer.writestr(os.path.join(dirpath,'TNTFields.pdf'),pdfwriter.output(dest='S'))

    return output

if __name__== "__main__":

    """
    CSV should have the following fields:
    Name,PP_Longitude,PP_Latitude,Radius,Seed_angle,Lateral_offset,Sprayer_width,Pie_start,Pie_end,North_limit,East_limit,South_limit,West_limit,Female_bays_per_width,Experimental,Experimental_start_odd,# of Structures,spacing
    """
    process_csvfile("/Users/taylorlee/Documents/TNT_Code/my_code/field4_test.csv", use_metric=True)





"""    import argparse

    parser = argparse.ArgumentParser(
        description="Generate Trimble bee tent placement files from a CSV."
    )
    parser.add_argument("csv_file", help="Path to the CSV file with field data.")
    parser.add_argument(
        "-z", "--zip", dest="zip", help="Write results into this ZIP file instead of a folder."
    )
    parser.add_argument(
        "-p", "--path", help="Output folder (default: ./TNT next to CSV)."
    )
    parser.add_argument(
        "-t", "--timestamp", action="store_true",
        help="Append today’s date to output folder or zip."
    )
    parser.add_argument(
        "-m", "--metric", action="store_true",
        help="Treat numeric inputs as meters instead of feet (default is feet)."
    )
    args = parser.parse_args()

    # Call the core worker
    process_csvfile(
        csv_file=args.csv_file,
        path=args.path,
        use_zip=args.zip,
        timestamp=args.timestamp,
        use_metric=args.metric,
    )"""

