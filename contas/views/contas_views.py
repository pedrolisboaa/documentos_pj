from django.shortcuts import render
from contas.forms import RecemConstruidaForm

def index(request):
    context = {
        'titulo_pagina': 'Contas PJ',
    }
    return render(request, 'contas/index.html', context)


def recem_construida(request):

    form = RecemConstruidaForm()

   
    context = {
        'titulo_pagina': 'Recém Construída',
        'form': form,
    }



    return render(request, 'contas/recem.html', context)


def mei(request):
    context = {
        'titulo_pagina': 'MEI',
    }
    return render(request, 'contas/mei.html', context)


def simples(request):
    context = {
        'titulo_pagina': 'Optante do Simples',
    }
    return render(request, 'contas/simples.html', context)


def lucro_real(request):
    context = {
        'titulo_pagina': 'Lucro Real - Presumido',
    }
    return render(request, 'contas/lucro_real.html', context)


def associacao(request):
    context = {
        'titulo_pagina': 'Associações e Sindicatos',
    }
    return render(request, 'contas/associacao.html', context)


def condominio(request):
    context = {
        'titulo_pagina': 'Condomínio',
    }
    return render(request, 'contas/condominio.html', context)


def cooperativa(request):
    context = {
        'titulo_pagina': 'Cooperativa',
    }
    return render(request, 'contas/cooperativa.html', context)

