#-*- coding:utf-8 -*-

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Book


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

# def search_form(request):
#     return render_to_response('search_form.html')

def search(request):
    '''
        django 查询成功示例
    '''
    errors = []
    if 'q' in request.GET:
        title =request.GET['q']

        if not title:
            errors.append('Enter a search term.')
        elif len(title)>20:
            errors.append('please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=title)  #忽略大小写
            return render_to_response('search_results.html',{'books':books,'query':title})

    return render_to_response('search_form.html',{'errors':errors})

def contact(request):
    '''
        django 发送邮件成功示例
    '''
    errors = []
    if request.method=='POST':
        if not request.POST.get('subject'):
            errors.append('Enter a subject')
        if not request.POST.get('message'):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                'jianglixiaobai@sina.com',
                [request.POST.get('email')],
                fail_silently=True
            )
            return HttpResponseRedirect('/thanks/')
    return render_to_response('contact_form.html',{'errors':errors})

def thanks(request):
    return HttpResponse('Your email has been sent successfully')

