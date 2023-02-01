from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models.associacao import Associacao
from .models.atividade import Atividade
from .models.escotista import Escotista
from .models.grupo_escoteiro import GrupoEscoteiro


class AtividadeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }


class AssociacaoAdmin(admin.ModelAdmin):
    ...


class EscotistaAdmin(admin.ModelAdmin):
    ...


class GrupoEscoteiroAdmin(admin.ModelAdmin):
    ...


admin.site.register(Associacao, AssociacaoAdmin)
admin.site.register(GrupoEscoteiro, GrupoEscoteiroAdmin)
admin.site.register(Escotista, EscotistaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
