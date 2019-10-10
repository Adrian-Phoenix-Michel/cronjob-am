# Generated by Django 2.2.6 on 2019-10-10 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cronjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('adresse', models.URLField(max_length=255)),
                ('authentifizierung_checked', models.BooleanField(default=False)),
                ('benutzername', models.CharField(max_length=255)),
                ('passwort', models.CharField(max_length=255)),
                ('ausführen', models.DateTimeField(default=datetime.datetime(2019, 10, 10, 9, 2, 22, 105756))),
                ('benachrichtigung_fehlschlag', models.BooleanField(default=False)),
                ('benachrichtigung_erfolg', models.BooleanField(default=False)),
                ('benachrichtigung_deaktivierung', models.BooleanField(default=False)),
                ('antwort_speichern', models.BooleanField(default=False)),
            ],
        ),
    ]
