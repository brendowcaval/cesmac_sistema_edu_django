from django.db import models

class Aluno(models.Model): # nome sobrenome cpf email
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome