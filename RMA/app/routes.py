from flask import render_template
from intro_to_flask import app

import gc


app.secret_key = 'super super secret key key'

@app.route('/')
def home():
	return render_template('index.html')

@login_required # access limited to authenticated users.
@app.route('/user')
def user_page():
	return render_template('user_page.html')


@app.route('/logout/')
def logout():
	pass


@app.route('/login/', methods=["GET","POST"])
def login():
    pass