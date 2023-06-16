from django.urls import path
from .views import index, recem_construida, mei, simples, lucro_real, associacao, condominio, cooperativa


app_name = 'contas'

urlpatterns = [
    path('', index, name="index"),
    
    # Contas PJ
    path('recem_construida/', recem_construida, name="recem_construida"),
    path('mei', mei, name="mei"),
    path('simples', simples, name="simples"),
    path('lucro_real', lucro_real, name="lucro_real"),
    path('associacao', associacao, name="associacao"),
    path('condominio,', condominio, name="condominio"),
    path('cooperativa', cooperativa, name="cooperativa"),
]

