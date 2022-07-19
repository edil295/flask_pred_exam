from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Customers, User
from app import forms
from flask_login import login_user, logout_user, login_required
# post functions


def index():
    customers = Customers.query.all()
    return render_template('index.html', customers=customers)


@login_required
def customer_create():
    form = forms.CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            item = request.form.get('item')
            quantity = request.form.get('quantity')
            price = request.form.get('price')
            data_in = request.form.get('data_in')
            user = request.form.get('user')
            new_customer = Customers(name=name, phone_number=phone_number, item=item, quantity=quantity,
                                     price=price, data_in=data_in, user_id=user)
            db.session.add(new_customer)
            db.session.commit()
            return redirect(url_for('index'))
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')
    return render_template('customer_create.html', form=form)


def customer_detail(customer_id):
    form = forms.CustomerForm()
    customer = Customers.query.filter_by(id=customer_id).first()
    if customer:
        return render_template('customer_detail.html', customer=customer, form=form)
    else:
        flash('customer not field', category='danger')
        return redirect(url_for('index'))


@login_required
def customer_delete(customer_id):
    customer = Customers.query.filter_by(id=customer_id).first()
    if customer:
        if request.method == 'POST':
            db.session.delete(customer)
            db.session.commit()
            flash('Сотрудник успешно удален', category='success')
            return redirect(url_for('index'))
        else:
            form = forms.CustomerForm()
            return render_template('customer_delete.html', customer=customer, form=form)
    else:
        flash('Сотрудник не найден', category='danger')
        return redirect(url_for('index'))


@login_required
def customer_update(customer_id):
    customer = Customers.query.filter_by(id=customer_id).first()
    if customer:
        form = forms.CustomerForm(obj=customer)
        if request.method == 'POST':
            if form.validate_on_submit():
                name = request.form.get('name')
                phone_number = request.form.get('phone_number')
                item = request.form.get('item')
                quantity = request.form.get('quantity')
                price = request.form.get('price')
                data_in = request.form.get('data_in')
                user = request.form.get('user')
                customer.name = name
                customer.phone_number = phone_number
                customer.item = item
                customer.quantity = quantity
                customer.price = price
                customer.data_in = data_in
                customer.user_id = user
                db.session.commit()
                flash('Данные успешно изменены', category='success')
                return redirect(url_for('index'))
            if form.errors:
                for errors in form.errors.values():
                    for error in errors:
                        flash(error, category='danger')
        return render_template('customer_update.html', form=form, customer=customer)
    else:
        flash('Сотрудник не найден', category='danger')
        return redirect(url_for('index'))

# user functions


def register():
    form = forms.UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=request.form.get('username'), password=request.form.get('password'))
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегестрировались', category='success')
            return redirect(url_for('index'))
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')
    return render_template('register.html', form=form)


def login():
    form = forms.UserForm()

    if request.method == 'POST':
        # if form.validate_on_submit():
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.check_password(request.form.get('password')):
            login_user(user)
            flash('Вы успешно аутентентифицировались', category='succes')
            return redirect(url_for('index'))
        else:
            flash('Неверный логин или пароль', category='danger')
        if form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')
    return render_template('login.html', form=form)


def logout():
    logout_user()
    flash('Вы вышли из учетной записи', category='success')
    return redirect(url_for('index'))

