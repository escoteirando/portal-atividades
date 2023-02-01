from atv.forms.auth import LoginForm
from atv.forms.subscribe_form import SubscribeForm
# from django.conf import settings
from django.http import (HttpRequest, HttpResponse, HttpResponseNotAllowed,
                         HttpResponseRedirect)
from django.shortcuts import render
from atv.services.auth_service import AuthService
from django.contrib.auth import login, logout


def _login_view_get(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    context = dict(form=form,
                   title='Login',
                   menu_items=[
                       dict(url='subscribe_form', title='Cadastrar')])

    return render(request, 'auth/login.html', context)


def _login_view_post(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST)
    context = dict(form=form,
                   title='Login',
                   )
    if form.is_valid():
        try:
            user = AuthService.login(email=form.data['email'],
                                     password=form.data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '') or '/')
            context['warning'] = 'Credenciais inválidas'
        except Exception as exc:
            context['warning'] = str(exc)
    else:
        context['warning'] = str(form.errors)
    return render(request, 'auth/login.html', context)


def _not_allowed(request: HttpRequest) -> HttpResponse:
    return HttpResponseNotAllowed(['GET', 'POST'])


def login_view(request: HttpRequest):
    match request.method:
        case 'GET':
            return _login_view_get(request)
        case 'POST':
            return _login_view_post(request)

    return _not_allowed(request)


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect('/')


def subscribe_form_view(request: HttpRequest):
    from atv.services.auth_providers import get_auth_providers
    associacoes = get_auth_providers().providers_names()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = SubscribeForm()

    # theme = getattr(settings, 'MARTOR_THEME', 'bootstrap')
    context = dict(form=form, title='mAPPa subscribe',
                   menu_items=[dict(url='home', title='Home')],
                   associacoes=associacoes)
    return render(request, 'auth/subscribe_form.html', context)
