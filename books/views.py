#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response


def current_url_view(request):
    return HttpResponse("welcome come to the page at %s" % request.path)

def ua_display(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua ='unknow'
    return HttpResponse("you browser is %s" % ua)

def display_meta(request):
    values= request.META.items()
    values.sort()
    html = []
    for k ,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
