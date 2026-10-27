# Geospatial Tent Placement Verifier

This repository/notebook contains a set of Python functions designed to verify and adjust the geographical placement of objects (specifically, tents) in a field. Its primary purpose is to ensure that these tents maintain a minimum safe distance from the tracks of a center-pivot irrigation system. 

If a tent is placed dangerously close to a pivot track, the code automatically calculates a safe new position and shifts the tent, taking into account the compass angle at which the field bays are seeded.

## Features

* **Accurate Geodesic Math:** Utilizes `geographiclib` and `geopy` to handle Earth's curvature (WGS-84 model) rather than relying on flat-plane approximations.
* **Fast Spatial Querying:** Uses `scikit-learn`'s `BallTree` algorithm with a Haversine metric to quickly identify pivot track points that are too close to tent locations.
* **Smart Relocation:** Automatically shifts tents along the field's seeding angle, moving them either "up" or "down" the bay depending on their position relative to the pivot center and the track.
* **Interactive Mapping:** Leverages `geopandas.explore()` (powered by Folium) to visualize original tent locations, shifted tent locations, and the generated pivot tracks on an interactive web map.

## Dependencies

To run this code, you will need the following Python libraries installed:

* `geopandas`
* `numpy`
* `pandas`
* `shapely`
* `geographiclib`
* `geopy`
* `scikit-learn`
* `folium` (for interactive map plotting)

## Core Functions

### `verify_tent_position(tents, pivot_tracks, pivot_point, min_dist, seed_angle)`
*The workhorse function of the notebook.*

**Parameters:**
* `tents` *(GeoDataFrame)*: The original tent locations.
* `pivot_tracks` *(GeoDataFrame)*: The points making up the pivot tracks.
* `pivot_point` *(tuple)*: The `(lat, lon)` center point of the irrigation pivot.
* `min_dist` *(float)*: The minimum safe distance (in meters) required between a tent and a track.
* `seed_angle` *(float)*: The compass angle at which the bays are seeded (default is 0.0°).

**How it works:**
1. **Coordinate Parsing:** It safely extracts the coordinates, ensuring they are formatted as `(lat, lon)` for mathematical operations, rather than the `(lon, lat)` standard used by Shapely/GeoDataFrames.
2. **Spatial Indexing:** It builds a `BallTree` from the pivot track points. This allows for lightning-fast radius queries (checking which tracks are within `min_dist` of each tent).
3. **Collision Detection & Resolution:** 
   * If a tent is too close to a track, it calculates the geodesic distance to the pivot center to determine if the tent is on the *inside* or *outside* of the track.
   * It determines the bearing from the pivot to the tent and normalizes it against the `seed_angle`.
   * Using the `ll_at()` function, it shifts the tent 1.0 meter away from the track along the seeding angle axis.
4. **Output:** Returns a new `GeoDataFrame` containing the safe, corrected geometries for all tents.

### Supporting Functions

* **`geodesic_circle_points(lat0, lon0, radii_m, n, start_bearing)`:** Generates a series of points representing concentric circles (the pivot tracks) around a center point, accounting for Earth's curvature.
* **`geodesic_circle_polygons(...)`:** Similar to the points function, but constructs closed Shapely `Polygon` objects for visualization.
* **`ll_at(lat1, lon1, bearing, distance)`:** Solves the "direct geodesic problem" by calculating a new destination coordinate given a starting coordinate, a bearing, and a travel distance in meters.
* **`get_lat_lon(point_geom)`:** A helper utility to safely extract a `(lat, lon)` tuple from a Shapely `Point` object.

## Important Note on Coordinates
Geospatial libraries often differ in how they expect coordinate pairs. 
* **Shapely / GeoPandas / GeoJSON** typically use `(x, y)` which translates to `(Longitude, Latitude)`.
* **Geodesic Math (Haversine, Geopy, GeographicLib)** strictly requires `(Latitude, Longitude)`.
This codebase explicitly handles these conversions to prevent unexpected shifts or errors in mathematical outputs.
