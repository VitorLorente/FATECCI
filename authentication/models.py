from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def _criar_usuario(self, ra, password, **campos):
        if not ra: 
            raise ValueError("RA deve ser declarado!")
        user = self.model(ra=ra, **campos)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **campos):
        return self._criar_usuario(ra, password, **campos)

    def create_superuser(self, ra, password=None, **campos):
        campos.setdefault('perfil', 'C')
        return self._criar_usuario(ra, password, **campos)

class Usuario(AbstractBaseUser):
    ra = models.IntegerField("RA", unique=True)
    password = models.CharField("Senha", max_length=200)
    nome = models.CharField("Nome", max_length=120, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=80, blank=True, null=True)
    ativo = models.BooleanField("Ativo", default=True)
    perfil = models.CharField("Perfil", max_length=1)
    
    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ["email", "nome"]

    object = UsuarioManager()

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def __str__(self):
        return self.nome

    @property
    def is_staff(self):
        return self.perfil == "C"

    def has_module_perms(self, package_name):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    class Meta:
        db_table = 'USUARIO'