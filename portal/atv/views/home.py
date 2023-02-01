from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url


@login_required
def home_view(request):
    context = dict(title='Escoteirando :: Atv',
                   cards=[
                       dict(title='Pesquisar',
                            text='Faça uma busca por atividades na nossa base de dados',
                            link='#',
                            link_title='Pesquisar'),
                       dict(title='Criar',
                            text='Crie sua atividade',
                            link='#',
                            link_title='Criar'),
                       dict(title='Comunidade',
                            text='Informações sobre quem contribui por aqui',
                            link=resolve_url('comunidade'),
                            link_title='Comunidade')
                   ])
    return render(request, f'home.html', context)
