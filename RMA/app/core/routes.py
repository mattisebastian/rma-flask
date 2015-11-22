from flask import render_template
from flask_user import login_required
from app import app, db

import gc


app.secret_key = 'super super secret key key'

@app.route('/')
def home():
	return render_template('index.html')


@login_required # access limited to authenticated users.
@app.route('/user')
def user_page():
	return render_template('user_page.html')

@app.route('/user/profile', methods=['GET','POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('core.home_page'))

    # Process GET or invalid POST
    return render_template('user_profile_page.html',
                           form=form)


@app.route('/logout/')
def logout():
	pass


@app.route('/login/', methods=["GET","POST"])
def login():
    pass