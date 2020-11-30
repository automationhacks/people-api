from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/articles')
def get_all_articles():
    return 'List of: ' + url_for('get_all_articles')


@app.route('/articles/<article_id>')
def get_article(article_id):
    return 'You are reading: ' + article_id


if __name__ == '__main__':
    app.run()
