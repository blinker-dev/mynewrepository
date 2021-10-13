# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:05:14 2021

@author: unknown
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"