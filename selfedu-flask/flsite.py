from flask import Flask, render_template, url_for, request

app = Flask(__name__)

numb = [{'name': 'First', 'url': 'prost-perv'},
        {'name': 'Second', 'url': 'number 2'},
        {'name': 'Three', 'url': '333'}]

user = [{'name': 'Alpha', 'url': 'Alpha1'},
        {'name': 'Beta', 'url': 'Beta_2'},
        {'name': 'Gamma', 'url': '33 3'}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Все Фласк', menu=numb)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Про нас', menu=user)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    print(url_for('contact'))
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('contact.html', title='Контакты', menu=numb)

@app.route('/profile/<username>') #<path:username>asd/123)
def profile(username):
    return f'Пользователь: {username}'


if __name__ == "__main__":
    app.run(debug=True)

#with app.test_request_context():
#    print(url_for('index'))
