from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    return render_template('base.html')


@app.route('/clothes/')
def jackets():
    context = {'title': 'Куртки'}
    jacket_items = [
        {'text': 'Ветровка',
         'image': 'jacket.jpg'},
        {'text': 'Пальто',
         'image': 'coat.jpg'},
    ]
    return render_template('clothes.html', **context, jackets=jacket_items)


if __name__ == '__main__':
    app.run(port=5001, debug=True)