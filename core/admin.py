from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ["nome", "sigla"]

class ProfessorAdmin(UserAdmin):
    add_form = ProfessorForm
    #form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "apelido")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "apelido")}),)
    list_display = ["ra","nome","email", "apelido"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["apelido"]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["nome", "carga_horaria"]

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ["id_disciplina", "ano", "semestre"]

class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ["id_curso", "ano", "semestre"]

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["id_grade", "numero"]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ["id_disciplina", "id_turma", "id_professor"]


admin.site.register(Curso, CursoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(GradeCurricular, GradeCurricularAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Turma, TurmaAdmin)