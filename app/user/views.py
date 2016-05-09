from flask import render_template
from flask_login import login_required
from . import user


@user.route('login/')
def login():
    return render_template('index.html')
