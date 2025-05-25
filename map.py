from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(
        location=[45.52336, -122.6750]
    )
    return map._repr_html_()

@app.route("/open-street-map")
def open_street_map():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Toner',
        zoom_start=13
    )

    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)

    return map._repr_html_()

@app.route("/open-marker")
def open_marker():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )

    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)

    folium.Marker(
        location=[45.52446, -122.6850],
        popup="<b>Marker 2 here</b>",
        tooltip="Click Here!",
        icon = folium.Icon(color='green')
    ).add_to(map)

    folium.Marker(
        location=[45.52556, -122.6950],
        popup="<b>Marker 3 here</b>",
        tooltip="Click Here!",
        icon = folium.Icon(color='red')
    ).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)