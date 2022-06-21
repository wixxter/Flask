from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['First', 'Second', 'Three']
user = ['Alpha', 'Beta', 'Gamma']

@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Все Фласк', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Про нас', menu=user)


@app.route('/profile/<username>' #<path:username>asd/123)
def profile(username):
    return f'Пользователь: {username}'


if __name__ == "__main__":
    app.run(debug=True)

#with app.test_request_context():
#    print(url_for('index'))
