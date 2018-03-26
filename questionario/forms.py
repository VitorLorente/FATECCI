from core.models import *
from django.forms import ModelForm


class QuestaoForm(ModelForm):
    class Meta:
        model = Questao
        fields = '__all__'

class ArquivoQuestaoForm(ModelForm):
    class Meta:
        model = ArquivoQuestao
        fields = '__all__'

class RespostaForm(ModelForm):
    class Meta:
        model = Resposta
        fields = ["id_questao", "id_aluno", "data_de_envio"]

class ArquivoRespostaForm(ModelForm):
    class Meta:
        model = ArquivoResposta
        fields = '__all__'