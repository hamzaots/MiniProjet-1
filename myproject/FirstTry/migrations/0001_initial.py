# Generated by Django 5.0.3 on 2024-04-23 22:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dateasyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15)),
                ('scan_type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('time_zone', models.CharField(default='UTC', max_length=32)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.CharField(choices=[('entire', 'Opération entière')], default='entire', max_length=10)),
                ('recurrence', models.CharField(choices=[('monthly', 'Mensuelle'), ('daily', 'Quotidienne'), ('weekly', 'Hebdomadaire'), ('yearly', 'Annuelle'), ('none', 'Une seule fois')], default='monthly', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_scan', models.CharField(max_length=20)),
                ('ip_address_scan', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulnerability', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=50)),
                ('host_ip', models.CharField(max_length=15)),
                ('host_name', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('ip_address', models.CharField(max_length=15)),
                ('scan_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
