
import logging

from functions.format_weather import *
from flask import Flask, request, render_template

logging.basicConfig(filename="Basic.log")

app = Flask(__name__)


@app.route('/')
def search_weather():
    return render_template("form.html")


@app.route('/search/', methods=['POST'])
def weather():
    try:
        s = request.values["s"]
        weather = format_weather(get_weather(get_coordinates(s)))
        return render_template("weather.html", weather=weather)
    except Exception:
        return "Sorry, page not found 404 ;("


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
