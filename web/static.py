# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import Flask, Response

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

app = Flask(__name__)
app.register_blueprint(web)
