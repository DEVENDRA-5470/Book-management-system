from django.contrib import admin
from books.models import Mybook
# Register your models here.
@admin.register(Mybook)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','writer_name','book_name','book_category','published_by','published_date']

# admin.site.register(Mybook)
