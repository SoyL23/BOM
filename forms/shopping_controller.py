from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, DecimalField, FieldList, FormField
from wtforms.validators import DataRequired

class Shopping_Form(FlaskForm):
    class Meta:
        csrf = False

    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired(message='Date is required')])
    quantity = IntegerField('Quantity', validators=[DataRequired(message='Quantity is required')])
    total = DecimalField('Total', validators=[DataRequired(message='Total is required')])
    id_courses = FieldList(IntegerField('Course_ID', validators=[DataRequired(message='Course ID is required')]), min_entries=1)
    client_id = IntegerField('Client_ID', validators=[DataRequired(message='Client ID is required')])
