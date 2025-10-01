class NivelAcademico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return self.nome

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    numero_BI = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

class Aluno(Pessoa):
    turma = models.CharField(max_length=50)
    historico = models.TextField(blank=True)
    notas = models.TextField(blank=True)
    presenca = models.IntegerField(default=0)

class Responsavel(Pessoa):
    vinculo_aluno = models.CharField(max_length=100)

class Professor(Pessoa):
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, related_name='professores')
    nivel_academico = models.ForeignKey('NivelAcademico', on_delete=models.CASCADE, related_name='professores')
    turma = models.CharField(max_length=50)
    horario = models.CharField(max_length=100)

class Funcionario(Pessoa):
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

class MaterialEscolar(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    quantidade = models.IntegerField(default=0)
    fornecedor = models.CharField(max_length=100)

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    serie = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    sala = models.CharField(max_length=20)

