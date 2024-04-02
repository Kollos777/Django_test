from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .utils import mydatabase

def main(request, page=1):
    db = mydatabase()
    quotes = db.quote.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_one_page = paginator.page(page)
    return render(request, 'quotes/index.html',context={'quotes': quotes_one_page})