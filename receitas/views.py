from django.shortcuts import render
from .models import Receita


def index(request):

    receitas = Receita.objects.all()

    dados = {
    'nomes_das_receitas' : receitas
    }

    return render(request,'index.html', dados)


def receita(request):
    return render(request, 'receita.html')