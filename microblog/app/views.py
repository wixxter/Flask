from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'ASD'}  # выдуманный пользователь
    return render_template("index.html", title='Фласк', user=user)
