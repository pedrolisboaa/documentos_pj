from django.shortcuts import render

def index(request):
    context = {
        'titulo_pagina': 'INDEXX',
    }
    return render(request, 'contas/index.html', context)