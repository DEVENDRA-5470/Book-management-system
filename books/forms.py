from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

from books.models import Mybook


# Signup form
class Signup_1(UserCreationForm):

    password1=forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'placeholder':"Password",
        'class':' w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'})
    )
    password2=forms.CharField(
        label=("Password Confirm"),
        widget=forms.PasswordInput(attrs={'placeholder':"Re-Password",
        'class':'w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'})
    )
    class Meta:
        model=User
        fields=['username','email']
        label={'username':"Name",'email':"Email address"}
        widgets={
            'username':forms.TextInput(attrs={'placeholder':"Enter your name ",'autofocus':True,
            'class':'w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out '}),
            'email':forms.EmailInput(attrs={'placeholder':"Email address ",
            'class':'w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'})
        }



# Login-form

class Log_in(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"placeholder":'Username',
        'class':'w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password',
        'class':'w-full bg-gray-900 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-green-900 rounded border border-gray-600 focus:border-green-500 text-base outline-none text-white py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))


# book-form

class Add_book(forms.ModelForm):
    class Meta:
        model=Mybook
        fields=['writer_name','book_name','book_category','book_content','published_by']
        widgets={
            'writer_name':forms.TextInput(attrs={'placeholder':'Book name char:150',
            'class':"appearance-none block w-full bg-gray-200 text-black border border-white rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" }),
            'book_name':forms.TextInput(attrs={'placeholder':'Book name char:150',
            'class':"appearance-none block w-full bg-gray-200 text-black border border-white rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" }),
            'book_category':forms.TextInput(attrs={'placeholder':'Book name char:150',
            'class':"block  appearance-none w-full bg-gray-200 border border-white text-black py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" }),
            'book_content':forms.Textarea(attrs={'placeholder':'Write your Journey here',
            'class':" capitalize appearance-none block w-full bg-gray-200 text-gray-700 border border-white rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" }),
            'published_by':forms.TextInput(attrs={'placeholder':'Book name char:150',
            'class':"appearance-none block w-full bg-gray-200 text-black  border border-white rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" })
            }