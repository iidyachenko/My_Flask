from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users = Blueprint("users", __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: "Игорь",
    2: "Павел",
    3: "Алексей",
}


@users.route("/")
def users_list():
    return render_template("users/list.html", users=USERS)


@users.route("/<int:user_id>/")
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/detail.html', user_id=user_id, user_name=user_name)
