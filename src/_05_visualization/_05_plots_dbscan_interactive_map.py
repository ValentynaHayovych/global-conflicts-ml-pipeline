import geopandas as gpd
import folium

def interactive_dbscan_map(df):

    """
    Function creates interactive map with each country and conflict coordinate labeled.
    Applied DBSCAN_Cluster to validate or invalidate each point.
    Returns:
    - dbscan_clusters_map.html
    """

    world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")

    m = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodbpositron')

    folium.GeoJson(
        world,
        style_function=lambda x:{'fillcolor': 'lightgrey', 'color':'darkgrey', 'weight':0.5},
        tooltip=folium.GeoJsonTooltip(fields=['ADMIN'], aliases=['Country:'])                   
    ).add_to(m)

    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            popup=folium.Popup(
                (f"Cluster: {row['DBSCAN_Cluster']}<br>"
                f"Deaths: {row['Total_Deaths']}<br>"
                f"{row['Country_A']} vs {row['Country_B']}"),
                max_width=300
            ),
            color='purple' if row['DBSCAN_Cluster'] == -1 else 'green',
            fill='purple' if row['DBSCAN_Cluster'] == -1 else 'green',
            ).add_to(m)

    return m
