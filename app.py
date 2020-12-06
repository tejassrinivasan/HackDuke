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
def home():
    return render_template("login.html")




if __name__ == '__main__':
    app.run(debug=True)