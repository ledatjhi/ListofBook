from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
    #     ("Content", {"fields": ["tutorial_content"]})
    # ]
    fields = ["book_title",
             "book_author",
             "book_published",
             "book_pages",
             "book_type",
             "book_picturename"]

admin.site.register(Book, BookAdmin)