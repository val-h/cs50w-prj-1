import markdown2 as md2
from random import choice
from django.shortcuts import render, redirect

from . import util
from .forms import NewEntry, EditEntry

def index(request):
    """Index page of the website."""
    context = {
        'entries': util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context=context)

def wiki_page(request, title):
    """Render a requested page."""
    context = {
        'title': title,
        'content': None,
    }
    try:
        context['content'] = md2.markdown(util.get_entry(title))
    except:
        return render(request, 'encyclopedia/404.html', context=context)

    if context['content'] == None:
        return render(request, 'encyclopedia/404.html', context=context)
    else:
        return render(request, 'encyclopedia/wiki_page.html', context=context)

def random_page(request):
    """Choose a random page and redirect the user to it."""
    entries = util.list_entries()
    random_entry = choice(entries)
    return redirect('encyclopedia:wiki_page', random_entry)

def search_page(request):
    """Search for a page with either full name or slice of it."""
    if request.method == "POST":
        entries = util.list_entries()
        # Display the page if names match exactly
        if request.POST['q'] in entries:
            # wiki_page(request, request.POST['q'])
            return redirect('encyclopedia:wiki_page', request.POST['q'])
        
        # Show a page with the search results if any
        matches = []
        for entry in entries:
            if request.POST['q'] in entry:
                matches.append(entry)
        if matches:
            return render(request, 'encyclopedia/search.html', {'entries': matches})
        else:
            context={'title': request.POST['q']}
            return render(request, 'encyclopedia/404.html', context)

def new_page(request):
    """New page for any user to create."""
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            title, content = form.cleaned_data['title'], form.cleaned_data['content']
            if title not in util.list_entries():
                util.save_entry(title, content)
                return redirect('encyclopedia:wiki_page', title)
            else:
                return render(request, 'encyclopedia/new_page.html', {
                    'form': form,
                    'error': True})

    else:
        form = NewEntry()
        return render(request, 'encyclopedia/new_page.html', {
            'form': form,
            'error': False})

def edit_page(request, title):
    if request.method == "POST":
        form = EditEntry(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return redirect('encyclopedia:wiki_page', title)
    
    else:
        entry = util.get_entry(title)
        form = EditEntry({'content': entry})
        return render(request, 'encyclopedia/edit_page.html', context={
            'entry': title,
            'form': form})

