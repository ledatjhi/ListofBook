from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import BookFilter

# Create your views here.


def homepage(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    book_filter = BookFilter(request.GET, queryset=book_list)
    # context = {'filter': book_filter}


    paginator = Paginator(book_filter.qs, 5)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {'books': books, 'filter': book_filter}
    
    return render(request, 'main/home.html', context)