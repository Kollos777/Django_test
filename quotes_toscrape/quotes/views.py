from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Quote, Author
from .utils import mydatabase
from .forms import AuthorForm, QuoteForm

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

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:add_author')
    else:
        form = AuthorForm()
    
    return render(request, 'quotes/add_author.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:add_quote')
    else:
        form = QuoteForm()
    
    return render(request, 'quotes/add_quote.html', {'form': form})