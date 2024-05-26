# Generated by Django 5.0.3 on 2024-05-26 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstTry', '0025_resultats'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='open_end',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='run_until',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='task',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='recurrence',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('monthly', 'Mensuelle'), ('daily', 'Quotidienne'), ('weekly', 'Hebdomadaire'), ('yearly', 'Annuelle'), ('one', 'Only Once')], default='none', max_length=15),
        ),
    ]
