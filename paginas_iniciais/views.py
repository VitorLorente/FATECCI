from django.shortcuts import render, redirect
from core.forms import AlunoForm, MatriculaForm
#from questionario.forms import QuestaoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Aluno, DisciplinaOfertada, Disciplina, Matricula, Turma

# Create your views here.
def home(request):
    return render(request, "index.html")

def cursos(request):
    return render(request, "cursos.html")

def noticias(request):
    return render(request, "noticias.html")

def grade(request):
    return render(request, "grade-curricular.html")

def detalhes(request):
    return render(request, "detalhes.html")

def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"


@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def pagina_aluno(request):
    aluno = Aluno.objects.get(id=request.user.id)
    disciplinas = DisciplinaOfertada.objects.all()
    disciplinas_matriculadas = Matricula.objects.filter(id_aluno=request.user.id)
    lista_disciplinas = []
    for disciplina in disciplinas_matriculadas:
        lista_disciplinas.append(disciplina.id_disciplina)
    
    context = {
        'curso' : aluno.id_curso.nome,
        'disciplinasOfertadas' : disciplinas,
        'disciplinas_matriculadas' : disciplinas_matriculadas,
        'lista_disciplinas' : lista_disciplinas
    }

    return render(request, "pagina_aluno.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def pagina_professor(request):
    turmas = Turma.objects.filter(id_professor=request.user.id)
    context = {
        'turmas' : turmas
    }

    return render(request, "pagina_professor.html", context)

def contato(request):
    return render(request, "contato.html")

def matricula(request):
    if request.POST:
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AlunoForm()
        

    context = {
        'form' : form
    }
    #django-widget-tweaks

    return render(request, "matricula.html", context)

def matricula_disciplina(request):
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MatriculaForm()

    context = {
        'form' : form
    }

    return render(request, "matricula_disciplina.html", context)

def disciplina(request, slug):
    disciplina = Disciplina.objects.get(slug=slug)
    aluno = Aluno.objects.get(id=request.user.id)
    matriculas = Matricula.objects.filter(id_aluno=aluno.id)
    lista_matriculas = []
    for item in matriculas:
        lista_matriculas.append(item.id_disciplina.id_disciplina.id)
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.id_aluno = Aluno.objects.get(id=request.user.id)
            forms.id_disciplina = DisciplinaOfertada.objects.get(id_disciplina=disciplina)
            forms.save()
    else:
        form = MatriculaForm()

    context = {
        'matriculas' : lista_matriculas,
        'disciplina' : disciplina,
        'form' : form,
        'user' : request.user
    }

    return render(request, "disciplina.html", context)