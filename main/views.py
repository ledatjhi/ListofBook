from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def homepage(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 10)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'main/home.html', { 'books': books })


# def homepage(request):
#     return render(request=request,
#                     template_name="main/home.html",
#                     context = {"books": Book.objects.all})
