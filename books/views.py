from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from books.forms import Signup_1,Log_in,Add_book
from books.models import Mybook
from django.contrib.auth.models import Group
# Create your views here.

# Home ##################################
def home(request):
    return render(request,'home.html')

# signup##################################
def signup1(request):
    if request.method == "POST":
        form=Signup_1(request.POST)
        if form.is_valid():
            form.save()
            form=Signup_1()
            return redirect('login')
    else:
        form=Signup_1()
    return render(request,'signup1.html',{'form':form})

    
# editor ##################################
def editor(request):
    if request.method == "POST":
        form=Signup_1(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Editor')
            user.groups.add(group)
            form=Signup_1()
            return redirect('login')
    else:
        form=Signup_1()
    return render(request,'editor.html',{'form':form})
    
# delete ##################################
def delete(request,id):
    if request.method == 'POST':
        pi=Mybook.objects.get(pk=id)
        print(pi,'pppppppppppppppppppppppppppppppppppppp')
        pi.delete()
    return redirect('allbook')


# update book------------------------------------------
def update_book(request,id):
    if request.method == 'POST':
        pi=Mybook.objects.get(id=id)
        print(pi,'oooo')
        form=Add_book(request.POST ,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('allbook')
    else:
        pi=Mybook.objects.get(pk=id)
        form=Add_book(instance=pi)
    return render(request,'updatebook.html',{'form':form})
    
    

# Login ##################################
def log_in(request):
    if request.method =="POST":
        form=Log_in(request=request ,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                form=Log_in()
                return redirect('home')
            else:
                return HttpResponseRedirect("bad credintials !!")
    else:
        form=Log_in()
    return render(request,'login.html',{'form':form})


# Logout ##################################
def log_out(request):
    logout(request)
    return redirect('login')


# add-books ##################################
def add_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=Add_book(request.POST)
            if form.is_valid():
                w_name=form.cleaned_data['writer_name']
                book_name=form.cleaned_data['book_name']
                book_cat=form.cleaned_data['book_category']
                book_con=form.cleaned_data['book_content']
                pub_by=form.cleaned_data['published_by']
                book=Mybook(writer_name=w_name,book_name=book_name,book_category=book_cat,book_content=book_con,published_by=pub_by)
                book.save()
                return redirect("allbook")
        else:
            form=Add_book()
        return render(request,'addbook.html',{'form':form})
    else:
        return redirect('login')


# Rendring books from data base:
def all_book(request):
    book=Mybook.objects.all()
    total=len(book)
    return render(request,'allbook.html',{'book':book,'total':total})

# Book-Detail----------------------------------------
def book_detail(request,id):
    book_detail=Mybook.objects.filter(id=id)
    return render(request,'bookdetail.html',{'book_detail': book_detail})

# Book-category----------------------------------------
def book_category(request,book):
    if book == "reader":
        
        book=Mybook.objects.filter(book_category='READER')
        print(book,'oooooooooooo')
        return render(request,'book_category.html',{'book':book})

    elif book == "story":
        
        book=Mybook.objects.filter(book_category='STORY')
        print(book,'oooooooooooo')
        return render(request,'book_category.html',{'book':book})

    elif book == "poetry":
        book=Mybook.objects.filter(book_category='POETRY')
        print(book,'oooooooooooo')
        return render(request,'book_category.html',{'book':book})

    else:
        return redirect('allbook')

# Features ----------------------

def features(request):
    return render(request,'features.html')