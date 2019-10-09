from django.shortcuts import render
from . import models
from .models import cronjob


# Create your views here.

def index(request):
    return render(request, "index.html")


def submit(request):
    if (request.POST):
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
