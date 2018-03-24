# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from authentication.models import Usuario

class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'CURSO'
        unique_together = (('sigla', 'nome'),)

    def __str__(self):
        return "{} - {}".format(self.sigla, self.nome)

class Aluno(Usuario):
    celular = models.CharField(max_length=11, blank=True, null=True)
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')

    class Meta:
        db_table = 'ALUNO'

    def __str__(self):
        return self.ra

class Coordenador(Usuario):
    celular = models.CharField(max_length=11, blank=True, null=True)
    id_curso = models.ForeignKey(Curso)

    class Meta:
        db_table = 'COORDENADOR'

class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=240)
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(max_digits=3, decimal_places=0)
    pratica = models.DecimalField(max_digits=3, decimal_places=0)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField(blank=True, null=True)
    conteudo = models.TextField()
    bibliografia_basica = models.TextField(blank=True, null=True)
    bibliografia_complementar = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        db_table = 'DISCIPLINA'

    def __str__(self):
        return self.nome

class DisciplinaOfertada(models.Model):
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        db_table = 'DISCIPLINA_OFERTADA'
        unique_together = (('id_disciplina', 'ano', 'semestre'),)

    def __str__(self):
        return "{} - {} {}".format(self.id_disciplina, self.semestre, self.ano)

class Professor(Usuario):
    apelido = models.CharField(unique=True, max_length=30)
    celular = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'PROFESSOR'

    def __str__(self):
        return self.apelido

class Turma(models.Model):
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    id_turma = models.CharField(max_length=1)
    id_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor')
    turno = models.CharField(max_length=15)

    class Meta:
        db_table = 'TURMA'
        unique_together = (('id_disciplina', 'id_turma', 'turno'),)

    def __str__(self):
        return "{} {} {}".format(self.id_disciplina, self.id_turma, self.turno)

class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='id_disciplina')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        db_table = 'MATRICULA'

class Questao(models.Model):
    id_disciplina = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='id_disciplina')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero = models.IntegerField()
    data_limite_entrega = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()

    class Meta:
        db_table = 'QUESTAO'
        unique_together = (('id_turma', 'numero'),)

class ArquivoQuestao(models.Model):
    id_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_questao')
    arquivo = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'ARQUIVO_QUESTAO'

class Resposta(models.Model):
    id_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='id_questao')
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.DateField()

    class Meta:
        db_table = 'RESPOSTA'
        unique_together = (('id_aluno', 'id_questao'),)

class ArquivoResposta(models.Model):
    id_resposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='id_resposta')
    arquivo = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'ARQUIVO_RESPOSTA'

class CursoTurma(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        db_table = 'CURSO_TURMA'
        unique_together = (('id_curso', 'id_turma'),)

class GradeCurricular(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        db_table = 'GRADE_CURRICULAR'
        unique_together = (('id_curso', 'ano', 'semestre'),)

    def __str__(self):
        return "{} - {}º semestre {}".format(self.id_curso, self.semestre, self.ano)

class Periodo(models.Model):
    id_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING, db_column='id_grade')
    numero = models.IntegerField()

    class Meta:
        db_table = 'PERIODO'
        unique_together = (('id_grade', 'numero'),)

class PeriodoDisciplina(models.Model):
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')

    class Meta:
        db_table = 'PERIODO_DISCIPLINA'
        unique_together = (('id_periodo', 'id_disciplina'),)
