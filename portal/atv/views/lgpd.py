from django.shortcuts import render
from django.http import HttpRequest


def load_termos_de_uso():
    return '''# Termos de uso

:warning: Em construção
'''


def load_politica_de_privacidade():
    return '''# Política de privacidade
    
## Acesso aos dados do mAPPa

Este site solicita as credenciais do mAPPa apenas para fins de identificação/autenticação do escotista e estas credenciais não são armazenadas.

'''


def load_default_doc():
    return '''# DOCUMENTO INEXISTENTE'''


lgpd_docs = dict(
    termos_de_uso=load_termos_de_uso,
    politica_de_privacidade=load_politica_de_privacidade
)


def lgpd_view(request: HttpRequest):
    p = request.path.replace('/', '')
    doc_func = lgpd_docs.get(p, load_default_doc)
    md = doc_func()
    context = dict(document=md)

    return render(request, 'lgpd.html', context)
