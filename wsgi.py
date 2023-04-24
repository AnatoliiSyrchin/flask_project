from blog.app import create_app
from flask import render_template
from blog.models.datebase import db
from werkzeug.security import generate_password_hash


app = create_app()


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", password=generate_password_hash('111'), is_staff=True)
    james = User(username="james", password=generate_password_hash('222'))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)


@app.route('/')
def index():
    return render_template("index.html")
