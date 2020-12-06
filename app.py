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

@app.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_history(username):

@app.route('/edit-resource/<resource_id>', methods=['GET', 'POST'])
@login_required
def edit_resource(resource_id):

@app.route('/post-resource', methods=['GET', 'POST'])
@login_required
def post_resource():

@app.route('/resource/<resource_id>/reviews', methods=['GET', 'POST'])
def review(resource_id):

@app.route('/search', methods=['GET'])
def search_page(items=None):

@app.route('/search', methods=['POST'])
def search():

@app.route('/profile')
@login_required
def profile():

@app.route('/edit-user', methods=['GET', 'POST'])
@login_required
def edit_user():

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
