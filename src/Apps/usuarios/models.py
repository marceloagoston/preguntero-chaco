from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime

class Usuario(AbstractUser):
    nacimiento = models.DateField(help_text=u'Fecha Nacimiento', default=datetime.date.today)
    es_admin = models.BooleanField(default=False)