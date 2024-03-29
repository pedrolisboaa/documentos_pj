from django.contrib import admin
from .models import RecemConstruida , Mei, Simples, LucroReal, Associacao, Condominio, Cooperativa


# Register your models here.
@admin.register(RecemConstruida, Mei, Simples, LucroReal, Associacao, Condominio, Cooperativa)
class RecemContruidaAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo',
        'email',
        'data_recebimento_documentacao'
    )

    ordering = '-id',
    search_fields = 'id', 'nome_completo', 'email'


