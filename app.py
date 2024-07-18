from flask import Flask

from dao.hard_coded_data import default_province_data, default_city_data
from flask_cors import CORS, cross_origin

app = Flask('dumpy_map_api')
front_url = ['localhost:3000', '127.0.0.1:3000']


@app.route('/provinces', methods=["GET"])
@cross_origin(front_url)
def get_map_data():
    return default_province_data


@app.route('/provinces/<province_name>', methods=["GET"])
@cross_origin(front_url)
def get_province_map_data(province_name):
    return default_city_data.get(province_name, {})


if __name__ == '__main__':
    app.run()
