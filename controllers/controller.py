from re import template
from flask import render_template
from app import app
from models.event_list import events


@app.route('/events')
def index():
    return render_template('index.html', title='Home' ,events=events)