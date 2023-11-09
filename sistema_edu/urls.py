from django.contrib import admin
from django.urls import path
from educacao.views import home_view, informacoes_aluno

urlpatterns = [
    path('', home_view),
    path('alunos/<int:pk>/', informacoes_aluno, name='informacoes_aluno'),
    path('admin/', admin.site.urls),
]
