"""
Flask seed
"""
from flask import Flask, url_for, render_template, redirect, request
# from flask import make_response, session, cookie

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/user/')
@app.route('/user/<string:username>')
def show_user_profile(username=None):
    app.logger.debug('testing app.logger.debug')
    app.logger.warning('testing app.logger.warning (%d)', 777)
    # app.logger.error('testing app.logger.error')
    return render_template('user_profile.html', username=username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)


@app.route('/user/default')
def show_default_user():
    return redirect(url_for('show_user_profile', username='Jaeyoung Chun'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
