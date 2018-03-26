from django.forms import ModelForm
from .models import *
from authentication.models import *


class AlunoForm(ModelForm):

    def save(self, commit=True):
        aluno = super(AlunoForm, self).save(commit=False)
        aluno.set_password("provisoria123")
        aluno.perfil = 'A'
        if commit:
            aluno.save()
        return aluno

    class Meta:
        model = Aluno
        fields = ['ra', 'nome', 'email', 'celular', 'id_curso']

class ProfessorForm(ModelForm):

    def save(self, commit=True):
        professor = super(ProfessorForm, self).save(commit=False)
        professor.set_password("provisoria123")
        professor.perfil = 'P'
        if commit:
            professor.save()
        return professor

    class Meta:
        model = Professor
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class DisciplinaOfertadaForm(ModelForm):
    class Meta:
        model = DisciplinaOfertada
        fields = '__all__'

class GradeCurricularForm(ModelForm):
    class Meta:
        model = GradeCurricular
        fields = '__all__'

class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'

class PeriodoDisciplinaForm(ModelForm):
    class Meta:
        model = PeriodoDisciplina 
        fields = '__all__'

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ["id_turma"]
        #["nome_disciplina", "ano_ofertado", "semestre_ofertado", "id_turma"]

class AvisoForm(ModelForm):
    class Meta:
        model = Aviso
        fields = ["id_turma", "data", "descricao"]