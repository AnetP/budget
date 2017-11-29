from django.conf.urls import url, include
from django.contrib import admin
from . import views

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home),

    url(r'^accounts/authorize/$', views.authorize),
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/invalid/$', views.invalid),
    url(r'^accounts/register/$', views.register),


    url(r'^incomes/', include('income.urls')),
    url(r'^expenses/', include('expense.urls')),

]
