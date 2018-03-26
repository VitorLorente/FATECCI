from django.shortcuts import render, redirect
from .forms import *
from paginas_iniciais.views import checa_aluno, checa_professor
from core.models import Aluno
from django.contrib.auth.decorators import login_required, user_passes_test

def corrige_gabarito(gabarito, resposta):
    i = 0
    nota = 0
    while i < 10:
        if resposta[i] == gabarito[i]:
            nota += 1
        i+=1 
    return nota


@login_required(login_url="/login")
@user_passes_test(checa_professor)
def cadastro_avaliacao(request):
    if request.POST:
        form = QuestaoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/cadastro_avaliacao2')

    else:
        form = QuestaoForm()        

    context = {
        'form' : form
    }

    return render(request, "cadastro_avaliacao.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def cadastro_avaliacao2(request):
    if request.POST:
        form = ArquivoQuestaoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
    else:
        form = ArquivoQuestaoForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_avaliacao2.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def cadastro_resposta(request):
    if request.POST:
        form = RespostaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/cadastro_resposta2')
    else:
        form = RespostaForm()
        

    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def cadastro_resposta2(request):
    aluno = Aluno.objects.get(id=request.user.id)
    if request.POST:
        #questao = ArquivoQuestao.objects.get(id_turma=request.POST.get('id_turma'), id_questao=request.POST.get('id_questao'))
        #rquivo = request.FILES.name
        form = ArquivoRespostaForm(request.POST, request.FILES)
        arquivo = request.FILES['arquivo']
        path = 'core/static/'
        path += arquivo.name
        lista_respostas = []
        if form.is_valid():
            form.save()
            with open(path, 'r') as f:
                datas = str(f.read())

            dts = datas.split(";")
            for data in dts:
                lista_respostas.append(data)
        #questao = Questao.objects.get(id_turma=request.POST.get('id_turma'), nome_disciplina=request.POST.get('nome_disciplina'))
        resposta = Resposta.objects.get(id_aluno = request.user.id, id=request.POST.get('id_resposta'))
        gab = ArquivoQuestao.objects.get(id_questao=resposta.id_questao)
        gabarito = gab.gabarito.split(";")
        resposta.nota = float(corrige_gabarito(gabarito, lista_respostas))
        resposta.save()
        nota = resposta.nota
    else:
        form = ArquivoRespostaForm()
    context = {
        'form' : form
    }

    return render(request, "cadastro_resposta2.html", context)