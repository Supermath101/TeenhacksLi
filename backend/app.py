from flask import Flask, jsonify, render_template, request, Response
import mapsApi
import json

app = Flask(__name__)



@app.route("/", methods=["POST"])
def main():
    address = json.loads(request.data)
    address = address['address']
    location = {'lat': mapsApi.getLat_Lng(address)[0]}, {'lng': mapsApi.getLat_Lng(address)[1]}
    resp = Response(json.dumps(location))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp

if __name__ == "__main__":
    app.run()
