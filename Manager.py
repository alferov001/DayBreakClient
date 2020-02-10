
from flask import Flask, render_template, session, request, redirect
from utilities import *
import requests, time, random, json


app=Flask(__name__)
app.secret_key = "secret_code"

@app.route('/')
@app.route('/login')
def entry_page():
    return render_template('login.html')

# ПРОВЕРКА ЛОГИНА (admin) И ПАРОЛЯ (1111)
@app.route("/auth", methods=["POST"])
def auth():
    a = request.form
    session["username"] = request.form["login"]
    if a["login"]=="admin" and a["password"]=="1111":
        return redirect ("/button1")
    else:
        return redirect ("/")


@app.route("/button1", methods=["POST", "GET"])
def first_page():
    login = session.pop("username", None)
    ts = str(time.time())
    time_start = {"timestamp": ts, "activity_type": "at_work", "user_id": login}
    url_stat = "http://127.0.0.1:5003/activity"
    r = requests.get(url=url_stat, json=time_start)
    return render_template("button1.html")


@app.route("/button2", methods=["POST","GET"])
def second_page():
    login = session.pop("username", None)
    b = str(time.time())
    url_stat = "http://127.0.0.1:5003/activity"
    time_stop = {"timestamp": b, "activity_type": "out_work", "user_id": login}
    r = requests.get(url=url_stat, json=time_stop)
    return render_template("button2.html")


if __name__=='__main__':
    app.run(port=5003, debug=True)
