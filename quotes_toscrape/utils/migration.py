import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_toscrape.settings")
django.setup()
from quotes.models import Quote, Tag, Author
client = MongoClient('mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')
db = client.mydatabase
authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author["fullname"],
        born_date = author["born_date"],
        born_location = author["born_location"],
        description = author["description"]
    )

quotes = db.quote.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t , *_ = Tag.objects.get_or_create(name = tag)
        tags.append(t)
    
    exist_quote = bool(len(Quote.objects.filter(text = quote["quote"])))
    print(exist_quote)
    if not exist_quote:
        author = db.author.find_one({"_id":quote["author"]})
        a = Author.objects.get(fullname = author['fullname'])
        q = Quote.objects.create(
            text= quote["quote"],
            author = a
        )
        for tag in tags:
            q.tags.add(tag)