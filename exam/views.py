from django.shortcuts import render
from django.http import HttpResponse

def showTest(request):
    que="who develop C language?"
    a="yuvraj"
    b="denies richie"
    c="koi nhi"
    d="both a and b"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/text.html',context=data)
    return res
def showresult(request):
    s="<h1>pass</h1>"
    return HttpResponse(s)
# Create your views here.
