from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
import os
import models
import forms
import sys
from numpy import dot
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from itsdangerous import URLSafeTimedSerializer
import traceback
import datetime
from datetime import timedelta
import random
import string
import urllib.request
import requests
import base64
import json

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
@login_required
def home():


@app.route('/resource/<resource_id>')
@login_required
def resource(resource_id):
    resource = db.session.query(models.Resources)\
        .filter(models.Resources.resource_id).all()
    return

@app.route('/edit-resource/<resource_id>', methods=['GET', 'POST'])
@login_required
def edit_resource(resource_id):
    try:
        resource = db.session.query(models.Resources).filter(models.Resources.resource_id == resource_id).filter(models.Resources.teacher_id == current_user.username).one()
        form = forms.ResourceEditFormFactory.form(resource)
        if form.validate_on_submit():
            form.errors.pop('database', None)

            if (request.files['image']):
                image = request.files['image']
                apiUrl = 'https://api.imgur.com/3/image'
                b64_image = base64.standard_b64encode(image.read())
                params = {'image' : b64_image}
                headers = {'Authorization' : 'Client-ID 12aa250c79dba8d'}
                #client_id = '12aa250c79dba8d'
                #client_secret = '0e132c4d82850eda1d2a172903f5a85bcea10a0b'
                response = requests.post(apiUrl, headers=headers, data=params)
                result = json.loads(response.text)
                edit_posting = models.Resources()
                edit_posting.file = result['data']['link']
                models.Resources.edit(resource_id, current_user.username, form.resource_name.data, form.category.data, form.subject.data, edit_posting.file, form.description.data, form.date_posted.data)
            else:
                models.Resources.edit(resource_id, current_user.username, form.resource_name.data, form.category.data, form.subject.data, resource.file, form.description.data, form.date_posted.data)

                flash('Item been modified successfully')
                return
    except:
        flash('You are not posting this item or this is not a valid resource.')
    return

@app.route('/post-resource', methods=['GET', 'POST'])
@login_required
def post_resource():
    form = forms.PostingFormFactory.form()
    if form.validate_on_submit():
        randomString = ''.join(random.choices(string.ascii_uppercase +
                         string.digits, k = 30))
        new_posting = models.Resources()
        new_posting.resource_id = randomString
        new_posting.teacher_id = current_user.username
        new_posting.resource_name = form.resource_name.data
        new_posting.category = form.category.data
        new_posting.subject = form.subject
        new_posting.description = form.description.data

        if (request.files['image']):
            image = request.files['image']
            apiUrl = 'https://api.imgur.com/3/image'
            b64_image = base64.standard_b64encode(image.read())
            params = {'image' : b64_image}
            headers = {'Authorization' : 'Client-ID 12aa250c79dba8d'}
            #client_id = '12aa250c79dba8d'
            #client_secret = '0e132c4d82850eda1d2a172903f5a85bcea10a0b'
            response = requests.post(apiUrl, headers=headers, data=params)
            result = json.loads(response.text)
            new_posting.image = result['data']['link']

        db.session.add(new_posting)

        db.session.commit()
        db.session.close()

        flash('Resource posted successfully')
        return

    return

@app.route('/resource/<resource_id>/reviews', methods=['GET', 'POST'])
def review(resource_id):
    resource = db.session.query(models.Resources) \
        .filter(models.Resources.resource_id == resource_id).first()

    reviews = db.session.query(models.Reviews) \
        .filter(models.Reviews.resource_id == resource_id) \
        .group_by(models.Reviews.review_id).all()

    form = forms.ReviewFormFactory.form()
    if form.validate_on_submit():
        num_reviews = len([r for r in reviews if r.teacher_id == current_user.username])

        if num_reviews >= 1:
            flash('You can only review an item once')
            return

        try:
            new_review = models.Reviews()
            new_review.item_rating = form.item_rating.data
            new_review.comments = form.comments.data
            new_review.resource_id = resource_id
            new_review.teacher_id = resource.teacher_id
            new_review.reviewer_username = current_user.username
            print(new_review)

            db.session.add(new_review)
            db.session.commit()
            db.session.close()

            return
        except BaseException as e:
            form.errors['database'] = str(e)

    avg_rating = 0
    if len(reviews):
        for review in reviews:
            avg_rating += review.item_rating
        avg_rating /= len(reviews)
        avg_rating = round(avg_rating, 2)

    return

@app.route('/search', methods=['GET'])
def search_page(resources=None):
    resources = [] if resources is None else resources
    return


@app.route('/search', methods=['POST'])
def search():
    resources = []

    form = forms.SearchFormFactory.form()
    if form.validate_on_submit():
        try:
            if form.category.data == 'All' or form.category.data is None:
                resources = db.session.query(models.Resources) \
                    .filter(models.Resources.resource_name.like('%{}%'.format(form.query.data))).limit(10).all()
            else:
                resources = db.session.query(models.Resources) \
                    .filter(models.Resources.resource_name.like('%{}%'.format(form.query.data))) \
                    .filter(models.Resources.category == form.category.data).limit(10).all()

        except BaseException as e:
            form.errors['database'] = str(e)
            return

    return

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile(username):
    


@app.route('/edit-user', methods=['GET', 'POST'])
@login_required
def edit_user():
    form = forms.UserEditFormFactory.form(current_user)

    if form.validate_on_submit():
        form.errors.pop('database', None)
        models.Teachers.edit(current_user.username, form.name.data, form.location.data, form.subjects.data, form.education_level.data, form.bio.data)
        return
    return

@app.route('/login')
def login():

@app.route('/login', methods=['POST'])
def login_post():

@app.route('/forgot', methods=['POST'])
def forgot_post():

@app.route('/reset/<token>')
def reset_with_token(token):

@app.route('/reset/<token>', methods=['POST'])
def reset_post(token):

@app.route('/forgot')
def forgot():

@app.route('/logout')
@login_required
def logout():

@app.route('/register')
def register():

@app.route('/register', methods = ['POST'])
def register_post():
