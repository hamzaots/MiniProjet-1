# Generated by Django 5.0.3 on 2024-04-30 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstTry', '0003_resultattcp_resultvulners_delete_result_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultattcp',
            old_name='etat',
            new_name='state',
        ),
    ]
