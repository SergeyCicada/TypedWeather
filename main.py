from format_weather import *
from flask import Flask, request, render_template
import logging

logging.basicConfig(filename="Basic.log")

app = Flask(__name__)


@app.route('/')
def search_weather():
    return render_template("form.html")


@app.route('/search/')
def weather():
    try:
        s = request.values["s"]
        return format_weather(get_weather(get_coordinates(s)))
    except Exception:
        return "Sorry, page not found ;("


if __name__ == '__main__':
    app.run()
