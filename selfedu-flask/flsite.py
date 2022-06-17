from flask import Flask, render_template

app = Flask(__name__)


menu = ['First', 'Second', 'Three']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Все Фласк', menu=menu)

@app.route('/about_us')
@app.route('/about')
def about():
    return render_template('about.html', title='Про нас')


if __name__ =="__main__":
    app.run(debug=True)