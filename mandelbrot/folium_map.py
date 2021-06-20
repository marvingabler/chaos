import folium

m = folium.Map(location=[45.523, -122.675], width=750, height=500)
img = folium.raster_layers.ImageOverlay(
        name="Mercator projection SW",
        image="output.png",
        bounds=[[-82, -180], [82, 180]],
        opacity=0.6,
        interactive=True,
        cross_origin=False,
        zindex=1,
    )
img.add_to(m)
folium.LayerControl().add_to(m)
