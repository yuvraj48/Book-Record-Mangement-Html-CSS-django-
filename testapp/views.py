from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/Employee.html',data)
    return(res)
def greeting(request):
    s="<h1>this is my first project</h1><p>this is landing page</p>"
    return HttpResponse(s)

def showcontact(request):
    s="<h1>contact</h1>"
    s+="<p>yuvraj:978888787</p>"
    s+="<p>kukuri:978888787</p>"
    s+="<p>lll:978888787</p>"
    return HttpResponse(s)

def about(request):
    text="this is an about page"
    return render(request,'testapp/about.html',{'text':text})
