"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from books.views import current_url_view,ua_display,display_meta,search,contact,\
    thanks,sendAdminsEmail
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',current_url_view),
    url(r'^ua/$',ua_display),
    url(r'^display_meta/$',display_meta),
    # url(r'^search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^contact/$',contact),
    url(r'^thanks/$',thanks),
    url(r'^emailtoadmin',sendAdminsEmail),
]
