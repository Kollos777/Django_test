from bson.objectid import ObjectId
from django import template
from ..utils import mydatabase

register = template.Library()


def get_author(id_):
    db = mydatabase()
    author = db.author.find_one({"_id": ObjectId(id_)})
    return author['fullname']


register.filter('author', get_author)

