
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def login_user(request):

    # logout(request)
    invalid = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hr/')
        else:
            invalid = True
    return render(request, 'login.html', {'invalid': invalid})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')


def login_admin(request):
    return render(request, 'login-admin.html')


def ll_required():
    return redirect('/auth/login/')
