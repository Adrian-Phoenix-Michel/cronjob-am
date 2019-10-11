from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from . import models
from .models import cronjob
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "index.html")


def submit(request):
    if request.POST:
        data = request.POST.dict()
        titel = data.get("Titel")
        adresse = data.get("Adresse")
        authentifizierung_checked = data.get("UIcon")
        benutzername = data.get("Benutzername")
        passwort = data.get("Passwort")
        ausführung = data.get("Ausführung")
        benachrichtigung_fehlschlag = data.get("Benachrichtigungen_F")
        benachrichtigung_erfolgnachfehl = data.get("Benachrichtigungen_E")
        benachrichtigung_deaktivierung = data.get("Benachrichtigungen_D")
        antwort_speichern = data.get("Antworten_speichern")

        if ausführung == "0":
            minute = data.get("Minute")
        elif ausführung == "1":
            ""
        elif ausführung == "2":
            ""
        elif ausführung == "3":
            ""

        if authentifizierung_checked == "on":
            authentifizierung_checked = True
        else:
            authentifizierung_checked = False

        if benachrichtigung_fehlschlag == "on":
            benachrichtigung_fehlschlag = True
        else:
            benachrichtigung_fehlschlag = False

        if benachrichtigung_erfolgnachfehl == "on":
            benachrichtigung_erfolgnachfehl = True
        else:
            benachrichtigung_erfolgnachfehl = False

        if benachrichtigung_deaktivierung == "on":
            benachrichtigung_deaktivierung = True
        else:
            benachrichtigung_deaktivierung = False

        if antwort_speichern == "on":
            antwort_speichern = True
        else:
            antwort_speichern = False


        new_entry = cronjob(titel=titel, adresse=adresse, authentifizierung_checked=authentifizierung_checked,
                            benutzername=benutzername, passwort=passwort,
                            benachrichtigung_fehlschlag=benachrichtigung_fehlschlag,
                            benachrichtigung_erfolg=benachrichtigung_erfolgnachfehl,
                            benachrichtigung_deaktivierung=benachrichtigung_deaktivierung,
                            antwort_speichern=antwort_speichern)

        cronjob.save(new_entry)

        return render(request, "index.html")
    else:
        return render(request, "index.html")


def myjobs(request):
    return render(request, "myjobs.html")

def createjobs(request):
    return render(request, "createjobs.html")