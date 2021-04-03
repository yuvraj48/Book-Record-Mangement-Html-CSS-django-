from django.conf.urls import url
from brm import views


urlpatterns=[
url('view-book',views.viewBooks),
url('edit-book',views.editbook),
url('delete-book',views.deletebook),
url('search-book',views.searchbook),
url('new-book',views.newbook),
url('add',views.add),
url('search',views.search),
url('edit',views.editbook),
url('login',views.userlogin),
url('login',views.userlogout),
]
