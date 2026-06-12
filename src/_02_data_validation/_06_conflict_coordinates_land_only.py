from shapely.geometry import Point
import geopandas as gpd
import geodatasets
from shapely.prepared import prep

def conflict_coordinates_land_only(df):

    """
    Function cuts off offshore zones, approving only land + 100 km buffer zone.
    Applied as filter on DataFrame to retain only conflict coordinates that are on land.
    Returns:
    - On_land - checks if a conflict point is on land
    - Land_Valid - land + buffer zone
    """
    # Load world land polygons and create a unified geometry
    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    world = world.make_valid() # Ensure geometries are valid
    world = world.buffer(0) # Fix any minor geometry issues
    world_union = world.unary_union

    # Function to check if a conflict point is on land
    def on_land(lon, lat):
        point = Point(lon, lat)
        return world_union.contains(point)

    # Apply the on_land function to each row and create a new column 'On_Land'
    df['On_Land'] = df.apply(lambda row: on_land(row['Longitude'], row['Latitude']), axis=1).astype(int)

    gdf_world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    gdf_world = gdf_world.make_valid() # Ensure geometries are valid
    gdf_world = gdf_world.to_crs(epsg=3857) # Project to Web Mercator for buffering in meters
    world_buffer = gdf_world.buffer(100_000) # 100 km buffer in meters
    world_buffer = world_buffer.to_crs(epsg=4326) # Convert back to lat/lon
    world_buffer = world_buffer.buffer(0) # Fix any geometry issues after buffering
    world_buffer_union = world_buffer.unary_union # Create a single geometry for the buffered land areas
    world_buffer_union = prep(world_buffer_union) # Prepare the geometry for faster spatial queries

    # Check if conflict points are within the buffered land area and create 'Land_Valid' column
    df['Land_Valid'] = df.apply(lambda row: world_buffer_union.contains(Point(row['Longitude'], row['Latitude'])), axis=1).astype(int)

    # Filter the DataFrame to keep only rows where 'Land_Valid' is 1 (valid land coordinates)
    df = df[df['Land_Valid']==1]
    
    return df

