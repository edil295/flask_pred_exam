from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators
from app.models import User, Customers


def get_users():
    users = []
    for user in User.query.all():
        obj = (user.id, f'{user.username}')
        users.append(obj)
    return users


class CustomerForm(FlaskForm):
    name = wf.StringField(label='Имя')
    phone_number = wf.StringField(label='Номер телефона')
    item = wf.StringField(label='Наименование товара')
    quantity = wf.IntegerField(label='Количество товара')
    price = wf.IntegerField(label='Цена за ед. товара')
    date_in = wf.DateField(label='Дата прибытия товара', format='%Y-%m-%d')
    user = wf.SelectField(label='Пользователь', choices=get_users(), coerce=int)
    submit = wf.SubmitField(label='Подтвердить')


class UserForm(FlaskForm):
    username = wf.StringField(label='Имя пользоватля', validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=64)
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=64)
    ])
    submit = wf.SubmitField(label='Подтвердить')

