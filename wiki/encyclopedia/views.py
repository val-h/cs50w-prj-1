# import re
from re import match
from django.shortcuts import render, redirect

from . import util
from .forms import NewEntry

def index(request):
    context = {
        'entries': util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context=context)

def wiki_page(request, title):
    context = {
        'title': title,
        # To make a custom md to html parser for later
        'content': util.get_entry(title),
    }
    if context['content'] == None:
        return render(request, 'encyclopedia/404.html', context=context)
    else:
        return render(request, 'encyclopedia/wiki_page.html', context=context)

# Tried to make a search query while using wiki_page but it needs it parameter
# to work with the previous feature, directly typing it in the url.
def search_page(request):
    if request.method == "POST":
        entries = util.list_entries()
        # Display the page if names match exactly
        if request.POST['q'] in entries:
            # return wiki_page(request, request.POST['q'])
            return redirect('encyclopedia:wiki_page', request.POST['q'])
        
        # Show a page with the search results if any
        matches = []
        for entry in entries:
            if request.POST['q'] in entry:
                matches.append(entry)
        if matches:
            return render(request, 'encyclopedia/search.html', {'entries': matches})
        else:
            return render(request, 'encyclopedia/404.html')

def new_page(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            title, content = form.cleaned_data['title'], form.cleaned_data['content']
            if title not in util.list_entries():
                util.save_entry(title, content)
                return redirect('encyclopedia/wiki_page', title)
            else:
                return render(request, 'encyclopedia/new_page.html', {
                    'form': form,
                    'error': True})

    else:
        form = NewEntry()
        return render(request, 'encyclopedia/new_page.html', {
            'form': form,
            'error': False})
