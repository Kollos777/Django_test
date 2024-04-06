from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote, Author
from .utils import mydatabase

def main(request, page=1):
    db = mydatabase()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_one_page = paginator.page(page)
    return render(request, 'quotes/index.html',context={'quotes': quotes_one_page})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'quotes/author.html', {'author': author})