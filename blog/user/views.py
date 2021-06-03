from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from flask_login import login_required

from blog.models import User

users = Blueprint("users", __name__, url_prefix='/users', static_folder='../static')


@users.route("/")
def users_list():
    user_db = User.query.all()
    return render_template("users/list.html", users=user_db)


@users.route("/<int:user_id>/")
@login_required
def user_details(user_id: int):
    try:
        user = User.query.filter_by(id=user_id).one_or_none()
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/detail.html', user_id=user_id, user_name=user.email)
