from flask import Flask, jsonify, render_template, request
import mapsApi

app = Flask(__name__)

@app.route("/")
def main():
    location = {'lat': mapsApi.getLat_Lng(address)[0]}, {'lng': mapsApi.getLat_Lng(address)[1]}
    return jsonify({'location': location})

if __name__ == "__main__":
    app.run()
