from django.urls import path
from books.views import *
# from django.contrib.auth import views as auth_view

urlpatterns=[
    path('',home,name="home"),
    path('signup1/',signup1,name="signup1"),
    path('editor/',editor,name="editor"),
    # path('login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=Log_in),name='login'),
    path('login/',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('addbook/',add_book,name='addbook'),
    path('allbook/',all_book,name='allbook'),
    path('bookdetail/<int:id>',book_detail,name='book-detail'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update_book,name='update'),
    path('bookcategory/<slug:book>',book_category,name='book-category'),
    path('features/',features,name='features'),
]