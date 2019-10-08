import datetime

from django.db import models

# Create your models here.

class cronjob(models.Model):
    titel = models.CharField(max_length=255)
    adresse = models.URLField(max_length=255)
    authentifizierung_checked = models.BooleanField(default=False)
    benutzername = models.CharField(max_length=255)
    passwort = models.CharField(max_length=255)
    ausführen = models.DateTimeField(default=datetime.datetime.now())
    benachrichtigung_fehlschlag = models.BooleanField(default=False)
    benachrichtigung_erfolg = models.BooleanField(default=False)
    benachrichtigung_deaktivierung = models.BooleanField(default=False)
    antwort_speichern = models.BooleanField(default=False)