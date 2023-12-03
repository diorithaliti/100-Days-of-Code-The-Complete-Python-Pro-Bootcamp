from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_choices = ["✘","☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"]
wifi_strength_choices = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
power_choices = ["✘","🔌", "🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"]
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location(URL from Google Map)', validators=[DataRequired()])
    opening = StringField('Opening time(ex 8AM', validators=[DataRequired()])
    closing = StringField('Closing time(ex 8PM)', validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee rating", choices=coffee_choices)
    wifi_strength_rating = SelectField(label="Wifi strength rating", choices=wifi_strength_choices)
    power_rating = SelectField(label="Power rating", choices=power_choices)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', newline='\n', encoding='utf-8', mode='a') as csv_file:
            csv_file.write(f"{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.opening.data},"
                           f"{form.closing.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength_rating.data},"
                           f"{form.power_rating.data} \n ")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
