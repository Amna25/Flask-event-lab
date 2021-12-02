from re import template
from flask import render_template 
from app import app
from models.event_list import events, Event
from flask import request


@app.route('/events')
def index():
    return render_template('index.html', title='Home' ,events=events)


@app.route('/events',methods=['POST'])
def add_event():
    name = request.form["name"]
    date = request.form["date"]
    guests = request.form["list_of_guests"]
    des =request.form["description"]
    room = request.form["room_location"]
    new_event=Event(date,name,guests,des,room)
    events.append(new_event)
    return render_template('index.html', title='Home' ,events=events)
