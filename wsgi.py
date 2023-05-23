from blog.app import create_app
from flask import render_template
from blog.models.datebase import db
from werkzeug.security import generate_password_hash


app = create_app()


@app.cli.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print('done!')


@app.cli.command('create-users')
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    james = User(username='james', password=generate_password_hash('222'))
    db.session.add(james)
    db.session.commit()
    print('done! created users:', james)


@app.cli.command('create-tags')
def create_tags():
    """
    Run in your terminal:
    flask create-tags
    > done! created tags: 
    """

    tags = ['flask', 'django', 'python', 'db']

    from blog.models.tags import Tag
    for tag in tags:
        db.session.add(Tag(name=tag))
    db.session.commit()
    print(f'done! created tags: {", ".join(tags)}')


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True,
    )
