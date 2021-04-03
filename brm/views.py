from django.shortcuts import render
from brm.forms import Newbookform,SearchForm
from brm import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.boo
def userlogin(request):
     data={}
     if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password'];
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/brm/view-book/')
        else:
            data['error']="username or password is incorrect"
            res=render(request,'brm/user_login.html',data)
            return res
     else:
        return render(request,'brm/user_login.html',data)
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('brm/login/')
def searchbook(request):
    form=SearchForm()
    res=render(request,'brm/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    books=models.book.objects.filter(title=form.data['title'])
    res=render(req,'brm/search_book.html',{'form':form,'book':book})
def deletebook(request):
    bookid=request.GET['bookid']
    book=models.book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('brm/view-book')
def editbook(request):
    book=models.book.objects.get(id=request.GET['bookid'])
    fields={'title': book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=Newbookform(initial=fields)
    res=render(request,'brm/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
        if request.method=='POST':
            form=Newbookform(request.POST)
            book=models.book()
            book.id=request.POST['bookid']
            book.title=form.data['title']
            book.price=form.data['price']
            book.author=form.data['author']
            book.publisher=form.data['publisher']
            book.save()
        return HttpResponseRedirect('brm/view_book.html')

def viewBooks(request):
     books=models.book.objects.all()
     #username=request.session['username']
     res=render(request,'brm/view_book.html',{'books':books})  #'username':username})
     return res

def newbook(request):
      form=Newbookform()
      res=render(request,'brm/books.html',{'form':form})
      return res

def add(request):
    if request.method=='POST':
        form=Newbookform(request.POST)
        book=models.book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="record stored<br><a href='/brm/view-book'>view all books</a>"
    return HttpResponse(s)
