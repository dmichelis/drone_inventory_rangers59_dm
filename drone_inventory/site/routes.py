from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

"""
Blueprint Configuration 
The first argument, called 'site' is the blueprint's name,
which is used by Flask's routing system.

The second argument, __name__, is the blueprint's import name,
which Flask uses to locate the blueprint resources.

The last argument, 'template_folder', is the blueprint's HTML template folser.
Which tells the blueprint which HTML files to sue for specific routes.
"""
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')