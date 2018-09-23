import os
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment

app = create_app(os.getenv('FLASKY_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Post=Post, Comment=Comment, \
                Follow=Follow, Permission=Permission)

if __name__ == '__main__':
    # Role.insert_roles()
    # print(Role.query.all())
    # User.add_self_follows()
    app.run(debug=True)