from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from wtforms import StringField, BooleanField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

class UserEditFormFactory:
    @staticmethod
    def form(user):
        class F(FlaskForm):
            username = StringField(default=teachers.username)
            name = StringField(default=teachers.name)
            location = StringField(default=teachers.location)
            subjects = StringField(default=teachers.subjects)
            education_level = StringField(default=teachers.education_level)
            bio = StringField(default=teachers.bio)
        return F()

class ReviewFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            item_rating = IntegerField(default=5)
            comments = StringField(default='')
        return F()

class PostingFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            resource_name = StringField(default='')
            category = SelectField(u'Category', choices=[('Lecture Recordings', 'Lecture Recordings'), ('Study Guides', 'Study Guides'), ('Handouts', 'Handouts'), ('Projects', 'Projects')])
            file = FileField(u'File Upload')
            description = StringField(default='')
        return F()

class ResourceEditFormFactory:
    @staticmethod
    def form(resource):
        class F(FlaskForm):
            resource_name = StringField(default=resources.resource_name)
            category = SelectField(u'Category', choices=[('Lecture Recordings', 'Lecture Recordings'), ('Study Guides', 'Study Guides'), ('Handouts', 'Handouts'), ('Projects', 'Projects')])
            file = FileField(u'File Upload')
            description = StringField(default=resources.description)
        return F()

class SearchFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            query = StringField(default='')
            category = StringField(default='All')
        return F()
