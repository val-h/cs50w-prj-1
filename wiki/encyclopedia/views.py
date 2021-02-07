from django.shortcuts import render

from . import util


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
    pass

