# Generated by Django 5.0.3 on 2024-05-24 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstTry', '0022_remove_customscan_script_types_customscan_scan_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customscan',
            name='scan_type',
        ),
        migrations.AddField(
            model_name='customscan',
            name='scan_type',
            field=models.ManyToManyField(to='FirstTry.nmapscripttype'),
        ),
    ]