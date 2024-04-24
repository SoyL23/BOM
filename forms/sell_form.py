from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class Sell_Form(FlaskForm):
    class Meta:
        csrf = False

    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired(message='Date is required')])
    total = DecimalField('Total', validators=[DataRequired(message='Total is required')])
    client_id = IntegerField('Client ID', validators=[DataRequired(message='Client ID is required')])
    seller_id = IntegerField('Seller ID', validators=[DataRequired(message='Seller ID is required')])
