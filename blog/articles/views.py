from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles = Blueprint("articles", __name__, url_prefix='/articles', static_folder='../static')
ARTICLES = [
    {
        'id': 1,
        'title': 'Статья  #1',
        'text': 'Тестовый текст для первой статьи',
        'author': {
            'name': 'Игорь',
            'id': 1,
        },
    },
    {
        'id': 2,
        'title': 'Статья #2',
        'text': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ut fugiat non, numquam laudantium ipsum '
                'voluptate incidunt quaerat, odit tempora ad nihil. Id enim debitis esse suscipit nobis dicta '
                'inventore modi.',
        'author': {
            'name': 'Павел',
            'id': 2,
        },
    }
]


@articles.route("/")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles.route("/<int:art_id>/")
def articles_details(art_id: int):
    try:
        ARTICLE = ARTICLES[art_id - 1]
    except (KeyError, IndexError):
        raise NotFound(f"Article #{art_id} doesn't exist!")
    return render_template('articles/detail.html', article=ARTICLE)
