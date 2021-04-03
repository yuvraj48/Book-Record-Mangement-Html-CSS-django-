from django.conf.urls import url
from exam import views
#static jo change ni showcontact#dynamic jo change ho jati hai
urlpatterns =[
     url('test',views.showTest),
     url('result',views.showresult),

]
