from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, \
    PasswordResetForm, ChangeEmailForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        else:
            flash("Wrong Password.")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('.login'))


@auth.route('/confirm/<token>')
def confirmpage(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token.encode('utf-8'))
    except:
        flash('Error!')
    user = User.query.filter_by(data.get('id'))
    if data.get('password', False):
        user.reset_password(data.get('password'))
    elif data.get('email', False):
        use.change_email(data.get('email'))
    else:
        flash('Failed!')
    return redirect(url_for('.login'))


@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        token = user.generate_token('password', form.new_password.data)
        send_email(user.email, 'Reset Your Password',
                   'auth/email/confirm', user=user, token=token,
                   next=request.args.get('next'))
        flash('A confirmation email has been sent to you by email,'
              'please login again.')
        return redirect(url_for('.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.password = form.password.data
        db.session.add(current_user)
        db.session.commit()
        logout_user()
        flash('Your password has been updated，please login again.')
        return redirect(url_for('.login'))
    return render_template("auth/change_password.html", form=form)


@auth.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        newemail = form.newemail.data
        token = current_user.generate_token('email', newemail)
        send_email(newemail, 'Change Your Email Address',
                   'auth/email/confirm', user=current_user, token=token)
        logout_user()
        flash('A confirmation email has been sent to you by your new email,'
              'please login again.')
        return redirect((url_for('.login')))
    return render_template('auth/change_email.html', form=form)
