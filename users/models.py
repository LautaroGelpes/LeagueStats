from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

# Create your models here.
class CommonUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    rank = models.IntegerField(default=0)

    user_permissions = models.ManyToManyField(Permission, related_name='commonuser_permissions')
    groups = models.ManyToManyField(Group, related_name='commonuser_groups')


# class attributes
#username: Campo de nombre de usuario único.
#first_name: Primer nombre del usuario.
#last_name: Apellido del usuario.
#mail: Dirección de correo electrónico del usuario.
#password: Contraseña del usuario (almacenada de forma segura).
#is_active: Indica si la cuenta del usuario está activa.
#is_superuser: Indica si el usuario tiene todos los permisos.
#last_login: Fecha y hora del último inicio de sesión.
#date_joined: Fecha y hora en que el usuario se unió.