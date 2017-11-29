from django.conf.urls import url, include
from . import views



urlpatterns = [
	url(r'^$', views.all),
	url(r'^(?P<expense_id>\d+)/$', views.expense),
	url(r'^delete/(?P<expense_id>\d+)/$', views.delete),
	url(r'^add/$', views.add)
	

]