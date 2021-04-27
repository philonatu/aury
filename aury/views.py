from django.shortcuts import render
from .models import myText


def index(request):
    texts = myText.objects.filter()
    print(texts)

    return render(request, 'index.html', {'texts': texts}, )

def book(request):
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'book.html', {'texts': texts})



def page_list(request):
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'page_list.html', {'texts': texts})
