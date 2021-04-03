from django.conf.urls import url
from testapp import views

urlpatterns =[
     url('about',views.about),
     url('result',views.showcontact),
     url('employee',views.employee_info_view),
     url('^$',views.greeting),

]
