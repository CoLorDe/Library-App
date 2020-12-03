from flask import g, render_template, redirect, url_for, current_app, send_from_directory
from app.base import bp

@bp.route('/')
def index():
    return render_template('index.html', title=None)

@bp.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')

@bp.route('/about')
def about():
    return render_template('about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('contact.html', title='Constact')

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
