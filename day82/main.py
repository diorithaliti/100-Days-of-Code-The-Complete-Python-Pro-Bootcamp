from flask import Flask, render_template, send_from_directory
from flask_ckeditor import CKEditor
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap(app)

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("SEND NOW")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    # form = ContactForm()
    return render_template('contact.html')

@app.route('/download')
def download():
    return send_from_directory('static', path="files/photo.jpg")

if __name__ == "__main__":
    app.run(debug=True)