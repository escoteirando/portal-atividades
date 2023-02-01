from django.urls import path

from atv.views import subscribe_form_view, home_view, lgpd_view, comunidade_view
from atv.views.auth import login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('subscribe/', subscribe_form_view, name='subscribe_form'),
    path('termos_de_uso/', lgpd_view, name='termos_de_uso'),
    path('politica_de_privacidade/', lgpd_view, name='politica_de_privacidade'),
    path('comunidade/', comunidade_view, name='comunidade')
]
