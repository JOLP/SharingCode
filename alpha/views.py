from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hackIDE_project import settings

from alpha.models import Chat

from django.views.decorators.csrf import csrf_protect
from alpha.forms import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Chatroom(request):
    queryset = Chat.objects.all()
    count = queryset.count()
    c = Chat.objects.all()
    return render(request, "alpha/chatroom.html", {'chatroom': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    queryset = Chat.objects.all()
    count = queryset.count()
    c = Chat.objects.all()[count-5:]
    return render(request, 'alpha/messages.html', {'chat': c})

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'alpha/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'alpha/success.html',
    )

@login_required
def Home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
