from django.conf.urls import url, include
from . import views



urlpatterns = [
	url(r'^$', views.all),
	url(r'^(?P<income_id>\d+)/$', views.income),
	url(r'^delete/(?P<income_id>\d+)/$', views.delete),
	url(r'^add/$', views.add)

]

