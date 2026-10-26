# Project Inspection: beetent_trimble-master

## Repository Tree (filtered)

```
beetent_trimble-master/
beetent_trimble-master/
  .gitmodules
  README.md
  TNT Pollinating Fields.ods
  maketentgrid.py
  nuitka_compile.sh
  shapefile.py
  utmish.py
  fpdf/
    __init__.py
    fonts.py
    fpdf.py
    html.py
    php.py
    py3k.py
    template.py
    ttfonts.py
  simplekml/
    __init__.py
    abstractview.py
    base.py
    constants.py
    coordinates.py
    featgeom.py
    icon.py
    kml.py
    makeunicode.py
    model.py
    networklinkcontrol.py
    overlay.py
    region.py
    schema.py
    styleselector.py
    substyle.py
    timeprimitive.py
    tour.py
  utm/
    __init__.py
    _version.py
    conversion.py
    error.py
```

## Quick Stats

{
"extracted_to": "/mnt/data/beetent_trimble-master",
"file_count": 37,
"python_files": 33,
"readmes_found": [
"beetent_trimble-master/README.md"
],
"requirements_files": [],
"entrypoints": []
}

## README snippets

### beetent_trimble-master/README.md

```
This is a simple program to create the necesary files for Trimble
FMX or similar GPS systems to mark out the position of bee tents for
David.


```

## Python Modules Overview

### beetent_trimble-master/maketentgrid.py

- Module docstring: None
- Uses argparse: True, uses click: False
  - Class `FileWriter` (line 22): implements a simple class that allows us to write to files in a directory using the same call as zipfile, so we can switch between using zips and directories easily
    - Method `__init__`(self) (line 27)
    - Method `__enter__`(self) (line 30)
    - Method `__exit__`(self, exc_type, exc_value, exc_traceback) (line 35)
    - Method `writestr`(self, filename, data) (line 39)
  - Class `BeePDF` (line 57): None
    - Method `__init__`(self, orientation, units, papersize) (line 58)
    - Method `move_to`(self, x, y) (line 63)
    - Method `line_to`(self, x, y) (line 67)
  - Function `ll_at`(lon1, lat1, bearing, distance) (line 72)
  - Function `make_files`(myzip, field_path, name, origin) (line 91)
  - Function `make_pdf_circle_bays`(pdf_writer, field) (line 106)
  - Function `make_tents`(myzip, trimble_path, field_name, pivotpoint, radius, width, lat_shift, angle, pie_slice) (line 297)
  - Function `make_line`(myzip, field_path, pivotpoint, lat_offset, angle) (line 466)
  - Function `calculate_spacing`(radius, width, factor, num_tents) (line 515)
  - Function `process_csvfile`(csv_file, path, use_zip, timestamp, use_metric) (line 539)
  - Contains `if __name__ == '__main__':` block (line 752)

### beetent_trimble-master/shapefile.py

- Module docstring: shapefile.py Provides read and write support for ESRI Shapefiles. author: jlawhead<at>geospatialpython.com version: 2.1.3 Compatible with Python versions 2.7-3.x
- Uses argparse: False, uses click: False
  - Class `_Array` (line 153): Converts python tuples to lists of the appropritate type. Used to unpack different shapefile header parts.
    - Method `__repr__`(self) (line 156)
  - Function `signed_area`(coords) (line 159)
  - Function `ring_bbox`(coords) (line 168)
  - Function `bbox_overlap`(bbox1, bbox2) (line 175)
  - Function `bbox_contains`(bbox1, bbox2) (line 183)
  - Function `ring_contains_point`(coords, p) (line 191)
  - Function `ring_sample`(coords, ccw) (line 233)
  - Function `ring_contains_ring`(coords1, coords2) (line 277)
  - Function `organize_polygon_rings`(rings) (line 282)
  - Class `Shape` (line 396): None
    - Method `__init__`(self, shapeType, points, parts, partTypes) (line 397)
    - Method `__geo_interface__`(self) (line 416)
    - Method `_from_geojson`(geoj) (line 511)
    - Method `shapeTypeName`(self) (line 587)
  - Class `_Record` (line 590): A class to hold a record. Subclasses list to ensure compatibility with former work and to reuse all the optimizations of the builtin list. In addition to the list interface, the values of the [...]
    - Method `__init__`(self, field_positions, values, oid) (line 606)
    - Method `__getattr__`(self, item) (line 621)
    - Method `__setattr__`(self, key, value) (line 640)
    - Method `__getitem__`(self, item) (line 656)
    - Method `__setitem__`(self, key, value) (line 677)
    - Method `oid`(self) (line 696)
    - Method `as_dict`(self, date_strings) (line 700)
    - Method `__repr__`(self) (line 712)
    - Method `__dir__`(self) (line 715)
  - Class `ShapeRecord` (line 726): A ShapeRecord object containing a shape along with its attributes. Provides the GeoJSON **geo_interface** to return a Feature dictionary.
    - Method `__init__`(self, shape, record) (line 729)
    - Method `__geo_interface__`(self) (line 734)
  - Class `Shapes` (line 739): A class to hold a list of Shape objects. Subclasses list to ensure compatibility with former work and to reuse all the optimizations of the builtin list. In addition to the list interface, this [...]
    - Method `__repr__`(self) (line 745)
    - Method `__geo_interface__`(self) (line 749)
  - Class `ShapeRecords` (line 755): A class to hold a list of ShapeRecord objects. Subclasses list to ensure compatibility with former work and to reuse all the optimizations of the builtin list. In addition to the list interface, [...]
    - Method `__repr__`(self) (line 761)
    - Method `__geo_interface__`(self) (line 765)
  - Class `ShapefileException` (line 769): An exception to handle shapefile specific problems.
  - Class `Reader` (line 773): Reads the three files of a shapefile as a unit or separately. If one of the three files (.shp, .shx, .dbf) is missing no exception is thrown until you try to call a method that depends on that [...]
    - Method `__init__`(self) (line 791)
    - Method `__str__`(self) (line 848)
    - Method `__enter__`(self) (line 861)
    - Method `__exit__`(self, exc_type, exc_val, exc_tb) (line 867)
    - Method `__len__`(self) (line 873)
    - Method `__iter__`(self) (line 908)
    - Method `__geo_interface__`(self) (line 914)
    - Method `shapeTypeName`(self) (line 921)
    - Method `load`(self, shapefile) (line 924)
    - Method `load_shp`(self, shapefile_name) (line 941)
  - Class `Writer` (line 1341): Provides write support for ESRI Shapefiles.
    - Method `__init__`(self, target, shapeType, autoBalance) (line 1343)
    - Method `__len__`(self) (line 1380)
    - Method `__enter__`(self) (line 1386)
    - Method `__exit__`(self, exc_type, exc_val, exc_tb) (line 1392)
    - Method `__del__`(self) (line 1398)
    - Method `close`(self) (line 1401)
    - Method `__getFileObj`(self, f) (line 1437)
    - Method `__shpFileLength`(self) (line 1449)
    - Method `__bbox`(self, s) (line 1462)
    - Method `__zbox`(self, s) (line 1484)
  - Contains `if __name__ == '__main__':` block (line 2204)

### beetent_trimble-master/utmish.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Function `in_bounds`(x, lower, upper, upper_strict) (line 39)
  - Function `mixed_signs`(x) (line 48)
  - Function `negative`(x) (line 52)
  - Function `to_lonlat`(easting, northing, central_longitude) (line 58)
  - Function `from_lonlat`(longitude, latitude, central_longitude) (line 130)

### beetent_trimble-master/fpdf/**init**.py

- Module docstring: FPDF for python
- Uses argparse: False, uses click: False

### beetent_trimble-master/fpdf/fonts.py

- Module docstring: None
- Uses argparse: False, uses click: False

### beetent_trimble-master/fpdf/fpdf.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Function `set_global`(var, val) (line 44)
  - Function `load_cache`(filename) (line 47)
  - Class `FPDF` (line 57): PDF Generation class
    - Method `__init__`(self, orientation, unit, format) (line 60)
    - Method `get_page_format`(format, k) (line 149)
    - Method `check_page`(fn) (line 160)
    - Method `set_margins`(self, left, top, right) (line 170)
    - Method `set_left_margin`(self, margin) (line 178)
    - Method `set_top_margin`(self, margin) (line 184)
    - Method `set_right_margin`(self, margin) (line 188)
    - Method `set_auto_page_break`(self, auto, margin) (line 192)
    - Method `set_display_mode`(self, zoom, layout) (line 198)
    - Method `set_compression`(self, compress) (line 213)

### beetent_trimble-master/fpdf/html.py

- Module docstring: HTML Renderer for FPDF.py
- Uses argparse: False, uses click: False
  - Function `px2mm`(px) (line 16)
  - Function `hex2dec`(color) (line 19)
  - Class `HTML2FPDF` (line 26): Render basic HTML to FPDF
    - Method `__init__`(self, pdf, image_map) (line 29)
    - Method `width2mm`(self, length) (line 59)
    - Method `handle_data`(self, txt) (line 68)
    - Method `box_shadow`(self, w, h, bgcolor) (line 124)
    - Method `output_table_header`(self) (line 132)
    - Method `output_table_footer`(self) (line 147)
    - Method `output_table_sep`(self) (line 161)
    - Method `handle_starttag`(self, tag, attrs) (line 169)
    - Method `handle_endtag`(self, tag) (line 281)
    - Method `set_font`(self, face, size) (line 348)
  - Class `HTMLMixin` (line 396): None
    - Method `write_html`(self, text, image_map) (line 397)

### beetent_trimble-master/fpdf/php.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Function `substr`(s, start, length) (line 8)
  - Function `sprintf`(fmt) (line 13)
  - Function `print_r`(array) (line 15)
  - Function `UTF8ToUTF16BE`(instr, setbom) (line 21)
  - Function `UTF8StringToArray`(instr) (line 34)
  - Function `die`(msg) (line 40)
  - Function `str_repeat`(s, count) (line 43)
  - Function `str_pad`(s, pad_length, pad_char, pad_type) (line 46)

### beetent_trimble-master/fpdf/py3k.py

- Module docstring: Special module to handle differences between Python 2 and 3 versions
- Uses argparse: False, uses click: False
  - Function `hashpath`(fn) (line 35)
  - Function `b`(s) (line 69)
  - Function `exception`() (line 78)

### beetent_trimble-master/fpdf/template.py

- Module docstring: PDF Template Helper for FPDF.py
- Uses argparse: False, uses click: False
  - Function `rgb`(col) (line 15)
  - Class `Template` (line 18): None
    - Method `__init__`(self, infile, elements, format, orientation, title, author, subject, creator, keywords) (line 19)
    - Method `load_elements`(self, elements) (line 33)
    - Method `parse_csv`(self, infile, delimiter, decimal_sep) (line 39)
    - Method `add_page`(self) (line 66)
    - Method `__setitem__`(self, name, value) (line 70)
    - Method `has_key`(self, name) (line 83)
    - Method `__contains__`(self, name) (line 86)
    - Method `__getitem__`(self, name) (line 89)
    - Method `split_multicell`(self, text, element_name) (line 102)
    - Method `render`(self, outfile, dest) (line 121)

### beetent_trimble-master/fpdf/ttfonts.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Function `sub32`(x, y) (line 44)
  - Function `calcChecksum`(data) (line 59)
  - Class `TTFontFile` (line 73): None
    - Method `__init__`(self) (line 75)
    - Method `getMetrics`(self, file) (line 78)
    - Method `readTableDirectory`(self) (line 100)
    - Method `get_table_pos`(self, tag) (line 114)
    - Method `seek`(self, pos) (line 119)
    - Method `skip`(self, delta) (line 123)
    - Method `seek_table`(self, tag, offset_in_table) (line 127)
    - Method `read_tag`(self) (line 133)
    - Method `read_short`(self) (line 137)
    - Method `unpack_short`(self, s) (line 145)

### beetent_trimble-master/simplekml/**init**.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False

### beetent_trimble-master/simplekml/abstractview.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `GxViewerOptions` (line 23): Enables special viewer modes. The arguments are the same as the properties.
    - Method `__init__`(self, gxoptions) (line 28)
    - Method `newgxoption`(self, name, enabled) (line 34)
    - Method `__str__`(self) (line 38)
  - Class `AbstractView` (line 46): Abstract element, extended by :class:`simplekml.Camera` and :class:`simplekml.LookAt` The arguments are the same as the properties. .. note:: Not to be used directly.
    - Method `__init__`(self, longitude, latitude, altitude, heading, tilt, altitudemode, gxaltitudemode, gxtimespan, gxtimestamp, gxhorizfov, gxvieweroptions) (line 56)
    - Method `longitude`(self) (line 82)
    - Method `longitude`(self, longitude) (line 87)
    - Method `latitude`(self) (line 91)
    - Method `latitude`(self, latitude) (line 96)
    - Method `altitude`(self) (line 100)
    - Method `altitude`(self, altitude) (line 105)
    - Method `heading`(self) (line 109)
    - Method `heading`(self, heading) (line 114)
    - Method `tilt`(self) (line 118)
  - Class `Camera` (line 199): A virtual camera that views the scene. The arguments are the same as the properties. Basic Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint() pnt.camera.latitude = 0.02 [...]
    - Method `__init__`(self, roll) (line 229)
    - Method `roll`(self) (line 234)
    - Method `roll`(self, roll) (line 239)
  - Class `LookAt` (line 243): Positions the camera in relation to the object that is being viewed. The arguments are the same as the properties (most inherited from :class:`simplekml.AbstractView`) Usage:: import simplekml [...]
    - Method `__init__`(self, range) (line 266)
    - Method `range`(self) (line 271)
    - Method `range`(self, range) (line 276)
  - Class `GxOption` (line 280): Child element of :class:`simplekml.GxViewerOptions`. The arguments are the same as the properties.
    - Method `__init__`(self, name, enabled) (line 289)
    - Method `name`(self) (line 295)
    - Method `name`(self, name) (line 304)
    - Method `enabled`(self) (line 308)
    - Method `enabled`(self, enabled) (line 313)
    - Method `__str__`(self) (line 316)

### beetent_trimble-master/simplekml/base.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Kmlable` (line 29): Enables a subclass to be converted into KML.
    - Method `__init__`(self) (line 36)
    - Method `__str__`(self) (line 45)
    - Method `_chrconvert`(cls, text) (line 85)
    - Method `addfile`(self, path) (line 107)
  - Class `Vector2` (line 110): Abstract class representing a vector. Args: _ x: int in xunits (default None) _ y: int in yunits (default None) _ xunits: string of type of x units. See :class:`simplekml.Units` (default None) _ [...]
    - Method `__init__`(self, x, y, xunits, yunits) (line 123)
    - Method `x`(self) (line 136)
    - Method `x`(self, x) (line 141)
    - Method `y`(self) (line 145)
    - Method `y`(self, y) (line 150)
    - Method `xunits`(self) (line 154)
    - Method `xunits`(self, xunits) (line 159)
    - Method `yunits`(self) (line 163)
    - Method `yunits`(self, yunits) (line 168)
    - Method `__str__`(self) (line 171)
  - Class `OverlayXY` (line 177): Point in overlay image that is mapped to screen coordinate :class:`simplekml.ScreenXY` Arguments are the same as the properties.
    - Method `__init__`(self) (line 183)
  - Class `ScreenXY` (line 187): Point relative to the screen origin that the overlay image is mapped to. Arguments are the same as the properties.
    - Method `__init__`(self) (line 194)
  - Class `RotationXY` (line 198): Point relative to the screen about which the screen overlay is rotated. Arguments are the same as the properties.
    - Method `__init__`(self) (line 205)
  - Class `Size` (line 209): Specifies the size of the image for the screen overlay. Arguments are the same as the properties.
    - Method `__init__`(self) (line 215)
  - Class `HotSpot` (line 219): Specifies the position inside the [Icon] that is anchored to the [Point]. Arguments are the same as the properties.
    - Method `__init__`(self) (line 226)
  - Class `Snippet` (line 230): A short description of the feature. Arguments are the same as the properties.
    - Method `__init__`(self, content, maxlines) (line 236)
    - Method `content`(self) (line 242)
    - Method `content`(self, content) (line 247)
    - Method `maxlines`(self) (line 251)
    - Method `maxlines`(self, maxlines) (line 256)
    - Method `__str__`(self) (line 259)
  - Class `KmlElement` (line 267): Overrides the original Element to format the KML to GMaps standards.
    - Method `patch`(cls) (line 273)
    - Method `unpatch`(cls) (line 280)
    - Method `writexml`(self, writer, indent, addindent, newl) (line 285)
  - Function `check`(classtype, subclass) (line 296)

### beetent_trimble-master/simplekml/constants.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `AltitudeMode` (line 19): AltitudeMode constants.
  - Class `GxAltitudeMode` (line 26): gx:AltitudeMode constants.
  - Class `ColorMode` (line 32): ColorMode constants.
  - Class `DisplayMode` (line 38): DisplayMode constants.
  - Class `ListItemType` (line 44): ListItemType constants.
  - Class `State` (line 52): State constants.
  - Class `Units` (line 62): Units constants.
  - Class `Shape` (line 69): Shape constants.
  - Class `GridOrigin` (line 76): GridOrigin constants.
  - Class `RefreshMode` (line 82): RefreshMode constants.
  - Class `ViewRefreshMode` (line 89): ViewRefreshMode constants.
  - Class `Types` (line 97): Types constants.
  - Class `GxPlayMode` (line 109): GxPlayMode constants.
  - Class `GxFlyToMode` (line 114): GxFlyToMode constants.
  - Class `Color` (line 120): Color constants (HTML and CSS) and converters. Constants: Same as HTML and CSS standard colors. All constants are lowercase. Class methods: \* :func:`simplekml.Color.rgb` - convert RGB to KML HEX [...]
    - Method `rgb`(cls, r, g, b, a) (line 135)
    - Method `hex`(cls, hstr) (line 148)
    - Method `hexa`(cls, hstr) (line 158)
    - Method `changealpha`(cls, alpha, gehex) (line 167)
    - Method `changealphaint`(cls, alpha, gehex) (line 177)

### beetent_trimble-master/simplekml/coordinates.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Coordinates` (line 18): Represents a list of Coordinate classes.
    - Method `__init__`(self, coords) (line 20)
    - Method `addcoordinates`(self, coords) (line 25)
    - Method `__str__`(self) (line 33)

### beetent_trimble-master/simplekml/featgeom.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Feature` (line 33): Abstract class extended by all features. The arguments are the same as the properties. .. note:: Not to be used directly.
    - Method `__init__`(self, name, visibility, open, atomauthor, atomlink, address, xaladdressdetails, phonenumber, snippet, description, camera, lookat, timestamp, timespan, region, extendeddata, gxballoonvisibility) (line 42)
    - Method `id`(self) (line 87)
    - Method `name`(self) (line 92)
    - Method `name`(self, name) (line 97)
    - Method `visibility`(self) (line 101)
    - Method `visibility`(self, visibility) (line 106)
    - Method `open`(self) (line 110)
    - Method `open`(self, open) (line 115)
    - Method `atomauthor`(self) (line 119)
    - Method `atomauthor`(self, atomauthor) (line 124)
  - Class `Container` (line 434): Abstract class, extended by :class:`simplekml.Document` and :class:`simplekml.Folder` Arguments are the same as :class:`simplekml.Feature` .. note:: Not to be used directly.
    - Method `__init__`(self) (line 442)
    - Method `features`(self) (line 446)
    - Method `allfeatures`(self) (line 460)
    - Method `geometries`(self) (line 473)
    - Method `allgeometries`(self) (line 481)
    - Method `containers`(self) (line 489)
    - Method `allcontainers`(self) (line 497)
    - Method `styles`(self) (line 510)
    - Method `allstyles`(self) (line 518)
    - Method `stylemaps`(self) (line 526)
  - Class `Document` (line 697): A container for features and styles. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() doc = kml.newdocument(name='A Document') pnt = doc.newpoint() [...]
    - Method `__init__`(self) (line 711)
    - Method `newschema`(self) (line 714)
  - Class `Folder` (line 725): A container for features that act like a folder. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() fol = kml.newfolder(name='A Folder') pnt = [...]
    - Method `__init__`(self) (line 739)
  - Class `Geometry` (line 743): Abstract class for all Geometries. Arguments are the same as :class:`simplekml.Placemark` .. note:: Not to be used directly.
    - Method `__init__`(self) (line 751)
    - Method `id`(self) (line 761)
    - Method `name`(self) (line 766)
    - Method `name`(self, name) (line 771)
    - Method `visibility`(self) (line 775)
    - Method `visibility`(self, visibility) (line 780)
    - Method `atomauthor`(self) (line 784)
    - Method `atomauthor`(self, atomauthor) (line 789)
    - Method `atomlink`(self) (line 793)
    - Method `atomlink`(self, atomlink) (line 798)
  - Class `Placemark` (line 1026): A Placemark is a Feature with associated Geometry. Args: _ geometry: any class that inherits from :class:`simplekml.Geometry` _ _all other args same as_ :class:`simplekml.Feature` .. note:: Not [...]
    - Method `__init__`(self, geometry) (line 1037)
    - Method `geometry`(self) (line 1042)
    - Method `geometry`(self, geom) (line 1048)
  - Class `PointGeometry` (line 1052): Abstract class for any geometry requiring coordinates (not :class:`simplekml.Polygon`). Args: _ coords: list of tuples (see :func:`simplekml.coords` for examples) _ _all other args same as_ [...]
    - Method `__init__`(self, coords) (line 1062)
    - Method `coords`(self) (line 1069)
    - Method `coords`(self, coords) (line 1085)
  - Class `LinearRing` (line 1090): A closed line string, typically the outer boundary of a :class:`simplekml.Polygon` Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pol = kml.newpolygon() [...]
    - Method `__init__`(self, coords, extrude, tessellate, altitudemode, gxaltitudemode, gxaltitudeoffset) (line 1104)
    - Method `extrude`(self) (line 1119)
    - Method `extrude`(self, extrude) (line 1124)
    - Method `tessellate`(self) (line 1128)
    - Method `tessellate`(self, tessellate) (line 1133)
    - Method `altitudemode`(self) (line 1137)
    - Method `altitudemode`(self, mode) (line 1145)
    - Method `gxaltitudemode`(self) (line 1149)
    - Method `gxaltitudemode`(self, mode) (line 1158)
    - Method `gxaltitudeoffset`(self) (line 1162)
  - Class `Point` (line 1174): A geographic location defined by lon, lat, and altitude. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') pnt.coords = [...]
    - Method `__init__`(self, extrude, altitudemode, gxaltitudemode) (line 1214)
    - Method `extrude`(self) (line 1225)
    - Method `extrude`(self, extrude) (line 1230)
    - Method `altitudemode`(self) (line 1234)
    - Method `altitudemode`(self, mode) (line 1242)
    - Method `gxaltitudemode`(self) (line 1246)
    - Method `gxaltitudemode`(self, mode) (line 1255)
    - Method `__str__`(self) (line 1258)
  - Class `LineString` (line 1262): A connected set of line segments. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() ls = kml.newlinestring(name='A LineString') ls.coords = [...]
    - Method `__init__`(self, extrude, tessellate, altitudemode, gxaltitudemode, gxaltitudeoffset, gxdraworder) (line 1289)
    - Method `extrude`(self) (line 1306)
    - Method `extrude`(self, extrude) (line 1311)
    - Method `tessellate`(self) (line 1315)
    - Method `tessellate`(self, tessellate) (line 1320)
    - Method `altitudemode`(self) (line 1324)
    - Method `altitudemode`(self, mode) (line 1332)
    - Method `gxaltitudemode`(self) (line 1336)
    - Method `gxaltitudemode`(self, mode) (line 1345)
    - Method `gxaltitudeoffset`(self) (line 1349)
  - Class `Polygon` (line 1370): A Polygon is defined by an outer boundary and/or an inner boundary. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pol = kml.newpolygon(name='A [...]
    - Method `__init__`(self, extrude, tessellate, altitudemode, gxaltitudemode, outerboundaryis, innerboundaryis) (line 1401)
    - Method `extrude`(self) (line 1418)
    - Method `extrude`(self, extrude) (line 1423)
    - Method `tessellate`(self) (line 1427)
    - Method `tessellate`(self, tessellate) (line 1432)
    - Method `altitudemode`(self) (line 1436)
    - Method `altitudemode`(self, mode) (line 1444)
    - Method `gxaltitudemode`(self) (line 1448)
    - Method `gxaltitudemode`(self, mode) (line 1457)
    - Method `innerboundaryis`(self) (line 1461)
  - Class `MultiGeometry` (line 1495): MultiGeometry is a collection of simple features (Points, LineStrings, etc). Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() multipnt = [...]
    - Method `__init__`(self, geometries) (line 1523)
    - Method `_newfeature`(self, cls) (line 1528)
    - Method `newpoint`(self) (line 1534)
    - Method `newlinestring`(self) (line 1544)
    - Method `newpolygon`(self) (line 1554)
    - Method `newgroundoverlay`(self) (line 1564)
    - Method `newscreenoverlay`(self) (line 1574)
    - Method `newphotooverlay`(self) (line 1584)
    - Method `newmodel`(self) (line 1594)
    - Method `__str__`(self) (line 1604)
  - Class `Overlay` (line 1613): Abstract class for image overlays. Arguments are the same as the properties. .. note:: Not to be used directly.
    - Method `__init__`(self, color, draworder, icon) (line 1621)
    - Method `color`(self) (line 1631)
    - Method `color`(self, color) (line 1636)
    - Method `draworder`(self) (line 1640)
    - Method `draworder`(self, draworder) (line 1645)
    - Method `icon`(self) (line 1649)
    - Method `icon`(self, icon) (line 1657)
  - Class `GroundOverlay` (line 1661): Draws an image overlay draped onto the terrain. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() ground = kml.newgroundoverlay(name='GroundOverlay') [...]
    - Method `__init__`(self, altitude, altitudemode, gxaltitudemode, latlonbox, gxlatlonquad) (line 1683)
    - Method `altitude`(self) (line 1697)
    - Method `altitude`(self, altitude) (line 1702)
    - Method `altitudemode`(self) (line 1706)
    - Method `altitudemode`(self, altitudemode) (line 1714)
    - Method `gxaltitudemode`(self) (line 1718)
    - Method `gxaltitudemode`(self, gxaltitudemode) (line 1727)
    - Method `latlonbox`(self) (line 1731)
    - Method `latlonbox`(self, latlonbox) (line 1742)
    - Method `gxlatlonquad`(self) (line 1746)
  - Class `ScreenOverlay` (line 1760): Draws an image overlay fixed to the screen. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() screen = kml.newscreenoverlay(name='ScreenOverlay') [...]
    - Method `__init__`(self, overlayxy, screenxy, rotationxy, size, rotation) (line 1782)
    - Method `rotation`(self) (line 1796)
    - Method `rotation`(self, rotation) (line 1801)
    - Method `overlayxy`(self) (line 1805)
    - Method `overlayxy`(self, overlayxy) (line 1818)
    - Method `screenxy`(self) (line 1822)
    - Method `screenxy`(self, screenxy) (line 1834)
    - Method `rotationxy`(self) (line 1838)
    - Method `rotationxy`(self, rotationxy) (line 1849)
    - Method `size`(self) (line 1853)
  - Class `PhotoOverlay` (line 1865): Geographically locate a photograph in Google Earth. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() photo = kml.newphotooverlay(name='PhotoOverlay Test') [...]
    - Method `__init__`(self, rotation, viewvolume, imagepyramid, point, shape) (line 1884)
    - Method `rotation`(self) (line 1898)
    - Method `rotation`(self, rotation) (line 1903)
    - Method `viewvolume`(self) (line 1907)
    - Method `viewvolume`(self, viewvolume) (line 1915)
    - Method `imagepyramid`(self) (line 1919)
    - Method `imagepyramid`(self, imagepyramid) (line 1927)
    - Method `point`(self) (line 1931)
    - Method `point`(self, point) (line 1939)
    - Method `shape`(self) (line 1943)
  - Class `NetworkLink` (line 1952): References a KML file or KMZ archive on a local or remote network. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() netlink = [...]
    - Method `__init__`(self, refreshvisibility, flytoview, link) (line 1967)
    - Method `refreshvisibility`(self) (line 1977)
    - Method `refreshvisibility`(self, refreshvisibility) (line 1987)
    - Method `flytoview`(self) (line 1991)
    - Method `flytoview`(self, flytoview) (line 1999)
    - Method `link`(self) (line 2003)
    - Method `link`(self, link) (line 2011)
  - Class `Model` (line 2015): A 3D object described in a COLLADA file. Arguments are the same as the properties.
    - Method `__init__`(self, altitudemode, gxaltitudemode, location, orientation, scale, link, resourcemap) (line 2021)
    - Method `altitudemode`(self) (line 2040)
    - Method `altitudemode`(self, altitudemode) (line 2048)
    - Method `gxaltitudemode`(self) (line 2052)
    - Method `gxaltitudemode`(self, gxaltitudemode) (line 2061)
    - Method `location`(self) (line 2065)
    - Method `location`(self, location) (line 2073)
    - Method `orientation`(self) (line 2077)
    - Method `orientation`(self, orientation) (line 2085)
    - Method `scale`(self) (line 2089)
  - Class `GxTrack` (line 2128): A track describes how an object moves through the world over a given time period. Arguments are the same as the properties. Usage:: # This is a recreation of the example found in the KML [...]
    - Method `__init__`(self, extrude, altitudemode, gxaltitudemode, model) (line 2206)
    - Method `extrude`(self) (line 2223)
    - Method `extrude`(self, extrude) (line 2228)
    - Method `altitudemode`(self) (line 2232)
    - Method `altitudemode`(self, altitudemode) (line 2241)
    - Method `gxaltitudemode`(self) (line 2245)
    - Method `gxaltitudemode`(self, gxaltitudemode) (line 2254)
    - Method `newdata`(self, gxcoord, when, angle) (line 2257)
    - Method `newwhen`(self, when) (line 2268)
    - Method `newgxcoord`(self, coord) (line 2279)
  - Class `GxMultiTrack` (line 2346): A container for grouping gx:tracks. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() multitrack = kml.newgxmultitrack() track1 = [...]
    - Method `__init__`(self, tracks, gxinterpolate) (line 2361)
    - Method `newgxtrack`(self) (line 2367)
    - Method `__str__`(self) (line 2379)

### beetent_trimble-master/simplekml/icon.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Link` (line 21): Specifies the location of: _ KML files fetched by network links _ Model files The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() netlink = [...]
    - Method `__init__`(self, href, refreshmode, refreshinterval, viewrefreshmode, viewrefreshtime, viewboundscale, viewformat, httpquery) (line 39)
    - Method `id`(self) (line 59)
    - Method `href`(self) (line 64)
    - Method `href`(self, href) (line 69)
    - Method `refreshmode`(self) (line 73)
    - Method `refreshmode`(self, refreshmode) (line 78)
    - Method `refreshinterval`(self) (line 82)
    - Method `refreshinterval`(self, refreshinterval) (line 87)
    - Method `viewrefreshmode`(self) (line 91)
    - Method `viewrefreshmode`(self, viewrefreshmode) (line 96)
  - Class `Icon` (line 142): Defines an image associated with an Icon style or overlay. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') [...]
    - Method `__init__`(self, gxx, gxy, gxw, gxh) (line 157)
    - Method `gxx`(self) (line 170)
    - Method `gxx`(self, gxx) (line 175)
    - Method `gxy`(self) (line 179)
    - Method `gxy`(self, gxy) (line 184)
    - Method `gxw`(self) (line 188)
    - Method `gxw`(self, gxw) (line 193)
    - Method `gxh`(self) (line 197)
    - Method `gxh`(self, gxh) (line 202)
    - Method `__str__`(self) (line 205)
  - Class `ItemIcon` (line 213): con used in the List view that reflects the state of a Folder or Link fetch. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = [...]
    - Method `__init__`(self, state, href) (line 228)
    - Method `href`(self) (line 234)
    - Method `href`(self, href) (line 239)
    - Method `state`(self) (line 243)
    - Method `state`(self, state) (line 248)

### beetent_trimble-master/simplekml/kml.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Kml` (line 30): The main class that represents a KML file. This class represents a KML file, and the compilation of the KML file will be done through this class. The base feature is a document, all arguments [...]
    - Method `__init__`(self) (line 52)
    - Method `__str__`(self) (line 64)
    - Method `_getnamespaces`(self) (line 67)
    - Method `addfile`(self, path) (line 71)
    - Method `features`(self) (line 91)
    - Method `allfeatures`(self) (line 96)
    - Method `geometries`(self) (line 104)
    - Method `allgeometries`(self) (line 112)
    - Method `containers`(self) (line 120)
    - Method `allcontainers`(self) (line 128)

### beetent_trimble-master/simplekml/makeunicode.py

- Module docstring: Obtained from http://python3porting.com/noconv.html enable unicode support in python 2 and 3.
- Uses argparse: False, uses click: False

### beetent_trimble-master/simplekml/model.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is [...]
- Uses argparse: False, uses click: False
  - Class `Location` (line 22): Specifies the exact coordinates of the Model's origin. The arguments are the same as the properties.
    - Method `__init__`(self, longitude, latitude, altitude) (line 28)
    - Method `longitude`(self) (line 38)
    - Method `longitude`(self, longitude) (line 43)
    - Method `latitude`(self) (line 47)
    - Method `latitude`(self, latitude) (line 52)
    - Method `altitude`(self) (line 56)
    - Method `altitude`(self, altitude) (line 61)
  - Class `Orientation` (line 65): Describes rotation of a 3D model's coordinate system. The arguments are the same as the properties.
    - Method `__init__`(self, heading, tilt, roll) (line 70)
    - Method `heading`(self) (line 80)
    - Method `heading`(self, heading) (line 85)
    - Method `tilt`(self) (line 89)
    - Method `tilt`(self, tilt) (line 94)
    - Method `roll`(self) (line 98)
    - Method `roll`(self, roll) (line 103)
  - Class `Scale` (line 107): Scales a model along the x, y, and z axes in the model's coordinate space. The arguments are the same as the properties.
    - Method `__init__`(self, x, y, z) (line 113)
    - Method `x`(self) (line 123)
    - Method `x`(self, x) (line 128)
    - Method `y`(self) (line 132)
    - Method `y`(self, y) (line 137)
    - Method `z`(self) (line 141)
    - Method `z`(self, z) (line 146)
  - Class `Alias` (line 150): Contains a mapping from a sourcehref to a targethref. The arguments are the same as the properties.
    - Method `__init__`(self, targethref, sourcehref) (line 156)
    - Method `targethref`(self) (line 164)
    - Method `targethref`(self, targethref) (line 169)
    - Method `sourcehref`(self) (line 173)
    - Method `sourcehref`(self, sourcehref) (line 178)
  - Class `ResourceMap` (line 182): Contains and specifies 0 or more [Alias] elements. The arguments are the same as the properties.
    - Method `__init__`(self, aliases) (line 188)
    - Method `aliases`(self) (line 196)
    - Method `aliases`(self, aliases) (line 201)
    - Method `newalias`(self) (line 204)
    - Method `__str__`(self) (line 215)

### beetent_trimble-master/simplekml/networklinkcontrol.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `LinkSnippet` (line 24): A short description of the feature. Arguments are the same as the properties. _New in version 1.1.1_
    - Method `__init__`(self) (line 33)
    - Method `__str__`(self) (line 36)
  - Class `NetworkLinkControl` (line 44): Controls the behavior of files fetched by a :class:`simplekml.NetworkLink`. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() kml.document = None # Removes [...]
    - Method `__init__`(self, minrefreshperiod, maxsessionlength, cookie, message, linkname, linkdescription, linksnippet, expires, update, camera, lookat) (line 60)
    - Method `minrefreshperiod`(self) (line 86)
    - Method `minrefreshperiod`(self, minrefreshperiod) (line 94)
    - Method `maxsessionlength`(self) (line 98)
    - Method `maxsessionlength`(self, maxsessionlength) (line 106)
    - Method `cookie`(self) (line 110)
    - Method `cookie`(self, cookie) (line 118)
    - Method `message`(self) (line 122)
    - Method `message`(self, message) (line 130)
    - Method `linkname`(self) (line 134)

### beetent_trimble-master/simplekml/overlay.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `ViewVolume` (line 23): Defines how much of the current scene is visible. The arguments are the same as the properties.
    - Method `__init__`(self, leftfov, rightfov, bottomfov, topfov, near) (line 29)
    - Method `leftfov`(self) (line 43)
    - Method `leftfov`(self, leftfov) (line 48)
    - Method `rightfov`(self) (line 52)
    - Method `rightfov`(self, rightfov) (line 57)
    - Method `topfov`(self) (line 61)
    - Method `topfov`(self, topFov) (line 66)
    - Method `bottomfov`(self) (line 70)
    - Method `bottomfov`(self, bottomFov) (line 75)
    - Method `near`(self) (line 79)
  - Class `ImagePyramid` (line 88): A hierarchical set of images. The arguments are the same as the properties.
    - Method `__init__`(self, titlesize, maxwidth, maxheight, gridorigin) (line 94)
    - Method `titlesize`(self) (line 106)
    - Method `titlesize`(self, titlesize) (line 111)
    - Method `maxwidth`(self) (line 115)
    - Method `maxwidth`(self, maxwidth) (line 120)
    - Method `maxheight`(self) (line 124)
    - Method `maxheight`(self, maxheight) (line 129)
    - Method `gridorigin`(self) (line 133)
    - Method `gridorigin`(self, gridorigin) (line 139)

### beetent_trimble-master/simplekml/region.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `Box` (line 24): Abstract class for box elements. The arguments are the same as the properties. .. note:: Not to be used directly.
    - Method `__init__`(self, north, south, east, west) (line 33)
    - Method `north`(self) (line 45)
    - Method `north`(self, north) (line 50)
    - Method `south`(self) (line 54)
    - Method `south`(self, south) (line 59)
    - Method `east`(self) (line 63)
    - Method `east`(self, east) (line 68)
    - Method `west`(self) (line 72)
    - Method `west`(self, west) (line 77)
  - Class `LatLonBox` (line 81): Specifies where the top, bottom, right, and left sides of a bounding box for the ground overlay are aligned. Args: \* _same as properties_ \* _all other args same as_ :class:`simplekml.Box`
    - Method `__init__`(self, rotation) (line 89)
    - Method `rotation`(self) (line 94)
    - Method `rotation`(self, rotation) (line 102)
  - Class `LatLonAltBox` (line 106): A bounding box that describes an area of interest defined by geographic coordinates and altitudes. Args: \* _same as properties_ \* _all other args same as_ :class:`simplekml.Box`
    - Method `__init__`(self, minaltitude, maxaltitude, altitudemode) (line 113)
    - Method `minaltitude`(self) (line 124)
    - Method `minaltitude`(self, minAltitude) (line 129)
    - Method `maxaltitude`(self) (line 133)
    - Method `maxaltitude`(self, maxaltitude) (line 138)
    - Method `altitudemode`(self) (line 142)
    - Method `altitudemode`(self, altitudemode) (line 150)
  - Class `Lod` (line 154): Level of Detail describes the size of the projected region. The arguments are the same as the properties.
    - Method `__init__`(self, minlodpixels, maxlodpixels, minfadeextent, maxfadeextent) (line 159)
    - Method `minlodpixels`(self) (line 171)
    - Method `minlodpixels`(self, minlodpixels) (line 176)
    - Method `maxlodpixels`(self) (line 180)
    - Method `maxlodpixels`(self, maxlodpixels) (line 185)
    - Method `minfadeextent`(self) (line 189)
    - Method `minfadeextent`(self, minfadeextent) (line 194)
    - Method `maxfadeextent`(self) (line 198)
    - Method `maxfadeextent`(self, maxfadeextent) (line 203)
  - Class `GxLatLonQuad` (line 207): Used for nonrectangular quadrilateral ground overlays. The arguments are the same as the properties.
    - Method `__init__`(self, coords) (line 212)
    - Method `coords`(self) (line 218)
    - Method `coords`(self, coords) (line 227)
  - Class `Region` (line 236): Used for nonrectangular quadrilateral ground overlays. The arguments are the same as the properties.
    - Method `__init__`(self, latlonaltbox, lod) (line 241)
    - Method `latlonaltbox`(self) (line 251)
    - Method `latlonaltbox`(self, latlonaltbox) (line 257)
    - Method `lod`(self) (line 261)
    - Method `lod`(self, lod) (line 267)

### beetent_trimble-master/simplekml/schema.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `SimpleField` (line 21): Custom field, forms part of a schema. The arguments are the same as the properties.
    - Method `__init__`(self, name, type, displayname) (line 27)
    - Method `name`(self) (line 34)
    - Method `name`(self, name) (line 39)
    - Method `type`(self) (line 43)
    - Method `type`(self, type) (line 48)
    - Method `displayname`(self) (line 52)
    - Method `displayname`(self, displayname) (line 57)
    - Method `__str__`(self) (line 60)
  - Class `GxSimpleArrayField` (line 68): Custom array field for gx:track, forms part of a schema. Args: \* _same as properties_ \* _all other args same as_ :class:`simplekml.SimpleField`
    - Method `__init__`(self, name, type, displayname) (line 76)
    - Method `__str__`(self) (line 79)
  - Class `SimpleData` (line 88): Data of a schema. The arguments are the same as the properties.
    - Method `__init__`(self, name, value) (line 94)
    - Method `name`(self) (line 100)
    - Method `name`(self, name) (line 105)
    - Method `value`(self) (line 109)
    - Method `value`(self, value) (line 114)
    - Method `__str__`(self) (line 117)
  - Class `GxSimpleArrayData` (line 121): Data of a :class:`simplekml.GxSimpleArrayField`. The arguments are the same as the properties.
    - Method `__init__`(self, name, values) (line 127)
    - Method `name`(self) (line 135)
    - Method `name`(self, name) (line 140)
    - Method `newvalue`(self, value) (line 143)
    - Method `__str__`(self) (line 147)
  - Class `Schema` (line 156): Custom KML schema that is used to add custom data to KML Features. The arguments are the same as the properties.
    - Method `__init__`(self, name) (line 162)
    - Method `id`(self) (line 169)
    - Method `name`(self) (line 174)
    - Method `name`(self, name) (line 179)
    - Method `newsimplefield`(self, name, type, displayname) (line 182)
    - Method `newgxsimplearrayfield`(self, name, type, displayname) (line 195)
    - Method `__str__`(self) (line 208)
  - Class `Data` (line 223): Data of extended data used to add custom data to KML Features. The arguments are the same as the properties.
    - Method `__init__`(self, name, value, displayname) (line 229)
    - Method `name`(self) (line 236)
    - Method `name`(self, name) (line 241)
    - Method `value`(self) (line 245)
    - Method `value`(self, value) (line 250)
    - Method `displayname`(self) (line 254)
    - Method `displayname`(self, displayname) (line 259)
    - Method `__str__`(self) (line 262)
  - Class `SchemaData` (line 273): Data of a schema that is used to add custom data to KML Features. The arguments are the same as the properties.
    - Method `__init__`(self, schemaurl) (line 279)
    - Method `schemaurl`(self) (line 286)
    - Method `schemaurl`(self, schemaurl) (line 294)
    - Method `newsimpledata`(self, name, value) (line 297)
    - Method `newgxsimplearraydata`(self, name, value) (line 310)
    - Method `__str__`(self) (line 322)
  - Class `ExtendedData` (line 333): Data of a schema that is used to add custom data to KML Features. The arguments are the same as the properties.
    - Method `__init__`(self) (line 339)
    - Method `schemadata`(self) (line 345)
    - Method `schemadata`(self, schemadata) (line 353)
    - Method `newdata`(self, name, value, displayname) (line 356)
    - Method `__str__`(self) (line 369)

### beetent_trimble-master/simplekml/styleselector.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `StyleSelector` (line 23): Abstract style class, extended by :class:`simplekml.Style` and :class:`simplekml.StyleMap` There are no arguments.
    - Method `__init__`(self) (line 29)
    - Method `id`(self) (line 33)
  - Class `Style` (line 38): Styles affect how Geometry is presented. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') pnt.coords = [(1.0, 2.0)] [...]
    - Method `__init__`(self, iconstyle, labelstyle, linestyle, polystyle, balloonstyle, liststyle) (line 54)
    - Method `__str__`(self) (line 69)
    - Method `iconstyle`(self) (line 73)
    - Method `iconstyle`(self, iconstyle) (line 81)
    - Method `labelstyle`(self) (line 85)
    - Method `labelstyle`(self, labelstyle) (line 93)
    - Method `linestyle`(self) (line 97)
    - Method `linestyle`(self, linestyle) (line 105)
    - Method `polystyle`(self) (line 109)
    - Method `polystyle`(self, polystyle) (line 117)
  - Class `StyleMap` (line 145): Styles affect how Geometry is presented. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(coords=[(18.432314,-33.988862)]) [...]
    - Method `__init__`(self, normalstyle, highlightstyle) (line 159)
    - Method `__str__`(self) (line 168)
    - Method `normalstyle`(self) (line 185)
    - Method `normalstyle`(self, normal) (line 193)
    - Method `highlightstyle`(self) (line 197)
    - Method `highlightstyle`(self, highlighturl) (line 205)

### beetent_trimble-master/simplekml/substyle.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `ColorStyle` (line 24): Abstract base class for geometry styles. The arguments are the same as the properties. .. note:: Not to be used directly.
    - Method `__init__`(self, color, colormode) (line 33)
    - Method `id`(self) (line 39)
    - Method `color`(self) (line 44)
    - Method `color`(self, color) (line 49)
    - Method `colormode`(self) (line 53)
    - Method `colormode`(self, colormode) (line 58)
    - Method `__str__`(self) (line 61)
  - Class `LineStyle` (line 69): Specifies the drawing style for all line geometry. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() lin = kml.newlinestring(name="Pathway", description="A [...]
    - Method `__init__`(self, width, gxoutercolor, gxouterwidth, gxphysicalwidth, gxlabelvisibility) (line 86)
    - Method `width`(self) (line 101)
    - Method `width`(self, width) (line 106)
    - Method `gxoutercolor`(self) (line 110)
    - Method `gxoutercolor`(self, gxoutercolor) (line 115)
    - Method `gxouterwidth`(self) (line 119)
    - Method `gxouterwidth`(self, gxouterwidth) (line 124)
    - Method `gxphysicalwidth`(self) (line 128)
    - Method `gxphysicalwidth`(self, gxphysicalwidth) (line 133)
    - Method `gxlabelvisibility`(self) (line 137)
  - Class `PolyStyle` (line 146): Specifies the drawing style for all polygons. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pol = kml.newpolygon(name="Atrium Garden", [...]
    - Method `__init__`(self, fill, outline) (line 165)
    - Method `fill`(self) (line 171)
    - Method `fill`(self, fill) (line 176)
    - Method `outline`(self) (line 180)
    - Method `outline`(self, outline) (line 185)
  - Class `IconStyle` (line 189): Specifies how icons for point Placemarks are drawn. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') pnt.coords = [...]
    - Method `__init__`(self, scale, heading, icon, hotspot) (line 205)
    - Method `scale`(self) (line 215)
    - Method `scale`(self, scale) (line 220)
    - Method `heading`(self) (line 224)
    - Method `heading`(self, heading) (line 229)
    - Method `icon`(self) (line 233)
    - Method `icon`(self, icon) (line 239)
    - Method `hotspot`(self) (line 243)
    - Method `hotspot`(self, hotspot) (line 251)
  - Class `LabelStyle` (line 255): Specifies how the name of a Feature is drawn. Arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') pnt.coords = [(1.0, [...]
    - Method `__init__`(self, scale) (line 272)
    - Method `scale`(self) (line 279)
    - Method `scale`(self, scale) (line 284)
  - Class `BalloonStyle` (line 288): Specifies the content and layout of the description balloon. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name="BallonStyle", [...]
    - Method `__init__`(self, bgcolor, textcolor, text, displaymode) (line 304)
    - Method `id`(self) (line 316)
    - Method `bgcolor`(self) (line 321)
    - Method `bgcolor`(self, bgcolor) (line 326)
    - Method `textcolor`(self) (line 330)
    - Method `textcolor`(self, textcolor) (line 335)
    - Method `text`(self) (line 339)
    - Method `text`(self, text) (line 344)
    - Method `displaymode`(self) (line 348)
    - Method `displaymode`(self, displaymode) (line 354)
  - Class `ListStyle` (line 358): Specifies the display of the elements style in the navigation bar. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() fol = kml.newfolder(name='Folder') [...]
    - Method `__init__`(self, listitemtype, bgcolor, itemicon) (line 373)
    - Method `id`(self) (line 383)
    - Method `itemicon`(self) (line 388)
    - Method `itemicon`(self, itemicon) (line 396)
    - Method `listitemtype`(self) (line 400)
    - Method `listitemtype`(self, listitemtype) (line 405)
    - Method `bgcolor`(self) (line 409)
    - Method `bgcolor`(self, bgcolor) (line 414)

### beetent_trimble-master/simplekml/timeprimitive.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `TimePrimitive` (line 22): Abstract class extended by all time primitive types. .. note:: Not to be used directly.
    - Method `__init__`(self) (line 29)
    - Method `id`(self) (line 33)
  - Class `TimeSpan` (line 38): Represents an extent in time bounded by begin and end dates. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') [...]
    - Method `__init__`(self, begin, end) (line 52)
    - Method `begin`(self) (line 58)
    - Method `begin`(self, begin) (line 63)
    - Method `end`(self) (line 67)
    - Method `end`(self, end) (line 72)
    - Method `__str__`(self) (line 75)
  - Class `GxTimeSpan` (line 82): A copy of the :class:`simplekml.TimeSpan` element, in the extension namespace. Args: \* _same as properties_ \* _all other args same as_ :class:`simplekml.TimeSpan` Usage:: import simplekml kml = [...]
    - Method `__init__`(self) (line 107)
    - Method `__str__`(self) (line 110)
  - Class `TimeStamp` (line 117): Represents a single moment in time. The arguments are the same as the properties. Usage:: import simplekml kml = simplekml.Kml() pnt = kml.newpoint(name='A Point') pnt.timestamp.when = 2011 [...]
    - Method `__init__`(self, when) (line 131)
    - Method `when`(self) (line 137)
    - Method `when`(self, when) (line 142)
    - Method `__str__`(self) (line 145)
  - Class `GxTimeStamp` (line 152): A copy of the :class:`simplekml.TimeStamp` element, in the extension namespace. Args: \* _same as properties_ \* _all other args same as_ :class:`simplekml.TimeStamp` Usage:: import simplekml kml [...]
    - Method `__init__`(self) (line 177)
    - Method `__str__`(self) (line 180)

### beetent_trimble-master/simplekml/tour.py

- Module docstring: Copyright 2011-2018 Kyle Lancaster | 2019 Patrick Eisoldt Simplekml is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later [...]
- Uses argparse: False, uses click: False
  - Class `GxTourPrimitive` (line 22): Abstract class extended by all tour types. .. note:: Not to be used directly.
    - Method `__init__`(self) (line 29)
    - Method `id`(self) (line 33)
  - Class `GxSoundCue` (line 38): Specifies a sound to be played in a tour. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, href, gxdelayedstart) (line 43)
    - Method `href`(self) (line 51)
    - Method `href`(self, href) (line 56)
    - Method `gxdelayedstart`(self) (line 60)
    - Method `gxdelayedstart`(self, gxdelayedstart) (line 65)
    - Method `__str__`(self) (line 68)
  - Class `GxTourControl` (line 75): Allows a tour to be paused. The arguments are the same as the properties.
    - Method `__init__`(self, gxplaymode) (line 80)
    - Method `gxplaymode`(self) (line 86)
    - Method `gxplaymode`(self, gxplaymode) (line 91)
    - Method `__str__`(self) (line 94)
  - Class `GxWait` (line 101): Allows a tour to be paused. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, gxduration) (line 106)
    - Method `gxduration`(self) (line 112)
    - Method `gxduration`(self, gxduration) (line 117)
    - Method `__str__`(self) (line 120)
  - Class `GxFlyTo` (line 126): Allows unbroken flight from point to point. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, gxduration, gxflytomode, camera, lookat) (line 135)
    - Method `gxduration`(self) (line 153)
    - Method `gxduration`(self, gxduration) (line 158)
    - Method `gxflytomode`(self) (line 162)
    - Method `gxflytomode`(self, gxflytomode) (line 167)
    - Method `camera`(self) (line 171)
    - Method `camera`(self, camera) (line 180)
    - Method `lookat`(self) (line 185)
    - Method `lookat`(self, lookat) (line 194)
    - Method `__str__`(self) (line 198)
  - Class `Update` (line 205): Action to take when animation updates. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, targethref, change, create, delete) (line 210)
    - Method `targethref`(self) (line 225)
    - Method `targethref`(self, targethref) (line 230)
    - Method `change`(self) (line 234)
    - Method `change`(self, change) (line 239)
    - Method `create`(self) (line 243)
    - Method `create`(self, create) (line 248)
    - Method `delete`(self) (line 252)
    - Method `delete`(self, delete) (line 257)
  - Class `GxAnimatedUpdate` (line 261): Controls changes during a tour to KML features. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, gxduration, gxdelayedstart, update) (line 267)
    - Method `gxduration`(self) (line 277)
    - Method `gxduration`(self, gxduration) (line 282)
    - Method `gxdelayedstart`(self) (line 286)
    - Method `gxdelayedstart`(self, gxdelayedstart) (line 291)
    - Method `update`(self) (line 295)
    - Method `update`(self, update) (line 303)
    - Method `__str__`(self) (line 306)
  - Class `GxPlaylist` (line 313): Defines a part of a tour. The arguments are the same as the properties. See :class:`simplekml.GxTour` for usage.
    - Method `__init__`(self, gxtourprimitives) (line 318)
    - Method `addgxtourprimitive`(self, gxtourprimitive) (line 325)
    - Method `newgxanimatedupdate`(self) (line 329)
    - Method `newgxflyto`(self) (line 339)
    - Method `newgxsoundcue`(self) (line 349)
    - Method `newgxtourcontrol`(self) (line 359)
    - Method `newgxwait`(self) (line 369)
    - Method `__str__`(self) (line 379)
  - Class `GxTour` (line 387): Defines a tour. The arguments are the same as the properties. Usage:: # Demonstrates touring with the reproduction of the tour sample in the KML Reference # [...]
    - Method `__init__`(self, name, description, gxplaylists) (line 435)
    - Method `name`(self) (line 447)
    - Method `name`(self, name) (line 452)
    - Method `description`(self) (line 456)
    - Method `description`(self, description) (line 461)
    - Method `newgxplaylist`(self, gxtourprimitives) (line 464)
    - Method `__str__`(self) (line 470)

### beetent_trimble-master/utm/**init**.py

- Module docstring: None
- Uses argparse: False, uses click: False

### beetent_trimble-master/utm/\_version.py

- Module docstring: None
- Uses argparse: False, uses click: False

### beetent_trimble-master/utm/conversion.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Function `in_bounds`(x, lower, upper, upper_strict) (line 44)
  - Function `check_valid_zone`(zone_number, zone_letter) (line 54)
  - Function `mixed_signs`(x) (line 65)
  - Function `negative`(x) (line 69)
  - Function `mod_angle`(value) (line 75)
  - Function `to_latlon`(easting, northing, zone_number, zone_letter, northern, strict) (line 80)
  - Function `from_latlon`(latitude, longitude, force_zone_number, force_zone_letter) (line 190)
  - Function `latitude_to_zone_letter`(latitude) (line 289)
  - Function `latlon_to_zone_number`(latitude, longitude) (line 301)
  - Function `zone_number_to_central_longitude`(zone_number) (line 326)

### beetent_trimble-master/utm/error.py

- Module docstring: None
- Uses argparse: False, uses click: False
  - Class `OutOfRangeError` (line 1): None
