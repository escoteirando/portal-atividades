from atv.forms.subscribe_form import SubscribeForm
from atv.services.auth_providers import get_auth_providers
# from django.conf import settings
from django.shortcuts import render

from ..services.auth_service import AuthService, AuthServiceError

SUBSCRIBE_TITLE = 'Escoteirando :: Cadastro'
MENU_ITEMS = [dict(url='home', title='Home')]


def subscribe_form_view_post(request):
    form = SubscribeForm(request.POST)
    try:
        if not form.is_valid():
            # TODO: Implementar um feedback ao usuário sobre o form inválido
            raise Exception('Dados inválidos')

        context = AuthService.subscribe_user(
            email=form.data['email'],
            password=form.data['password'],
            assoc_alias=form.data['assoc_alias'],
            assoc_user=form.data['assoc_user'],
            assoc_pass=form.data['assoc_pass'])

        return render(request, 'subscribed_form.html', context)
    except AuthServiceError as exc:
        context = dict(form=form,
                       title=SUBSCRIBE_TITLE,
                       menu_items=MENU_ITEMS,
                       )
        context[exc.level] = exc.message

    except Exception as exc:
        context = dict(form=form, title=SUBSCRIBE_TITLE,
                       menu_items=MENU_ITEMS,
                       warning=str(exc))

    return render(request, 'auth/subscribe_form.html', context)


def subscribe_form_view(request):
    if request.method == 'POST':
        return subscribe_form_view_post(request)

    _ = get_auth_providers()
    form = SubscribeForm()

    # theme = getattr(settings, 'MARTOR_THEME', 'bootstrap')
    context = dict(form=form, title='mAPPa subscribe',
                   menu_items=[dict(url='home', title='Home')])
    return render(request, f'auth/subscribe_form.html', context)
