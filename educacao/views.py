from django.shortcuts import render
from .models import Aluno




def home_view(request):
    context = {
        'alunos' : Aluno.objects.all()
    }
    return render(request, 'home.html', context)


def informacoes_aluno(request, pk):
    context = {
        'aluno': Aluno.objects.get(pk=pk)
    }
    return render(request, 'informacoes_aluno.html', context)