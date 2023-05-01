from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError

from blog.models.datebase import db
from blog.models import User
from blog.forms.user import RegistrationForm, LoginForm

auth_app = Blueprint('auth_app', __name__, url_prefix="/auth", static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = 'auth_app.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth_app.login'))


@auth_app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template('auth/login.html', form=form, error='username doesn`t exists')
        if not user.validate_password(form.password.data):
            return render_template(
                'auth/login.html',
                form=form,
                error=f"{check_password_hash(user.password, '1')}"
                # error=f'wrong username or password {generate_password_hash(form.password.data)} {generate_password_hash("1")} {user.password}')
            )
        login_user(user)
        return redirect(url_for('index'))
    
    return render_template('auth/login.html', form=form)


@auth_app.route('/login-as', methods=['GET', 'POST'], endpoint='login-as')
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound

    if request.method == 'GET':
        return render_template('auth/login_as.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        return render_template('auth/login.html', error='username not passed')
    if not password:
        return render_template('auth/login.html', error='password not passed')
    
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template('auth/login.html', error=f'no user {username!r} found')
    if not check_password_hash(user.password, password):
        return render_template('auth/login.html', error=f'wrong password')

    login_user(user)
    return redirect(url_for('index'))


@auth_app.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth_app.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append('username already exists')
            return render_template('auth/register.html', form=form)
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('auth/register.html', form=form)

        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            is_staff = False,
        )
        user.password = form.password.data
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception('couldn`t create user')
            error ='couldn`t create user'
        else:
            current_app.logger.info(f'Created user {user}')
            login_user(user)
            return redirect(url_for('index'))
    return render_template('auth/register.html', form=form, error=error)


__all__ = [
    'login_manager',
    'auth_app',
]