#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import publications, people
from flask import Flask, render_template

DATABASE = 'temp/flask.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'easy'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('index.html',tab='index')

@app.route('/people/')
def people_page():
    return render_template('people.html', people = people, tab='people')

@app.route('/publications/')
def publications_page():
    return render_template('publications.html',
                            publications=publications,
                            tab='publications')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


