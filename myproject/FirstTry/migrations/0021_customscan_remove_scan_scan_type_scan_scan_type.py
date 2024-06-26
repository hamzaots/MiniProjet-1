# Generated by Django 5.0.3 on 2024-05-24 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstTry', '0020_alter_scan_options_remove_scan_scan_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scan_Name', models.CharField(max_length=20)),
                ('script_types', models.CharField(choices=[('auth', 'Authentication'), ('broadcast', 'Broadcast'), ('brute', 'Brute Force'), ('default', 'Default'), ('discovery', 'Discovery'), ('dos', 'Denial of Service'), ('exploit', 'Exploitation'), ('external', 'External'), ('fuzzer', 'Fuzzer'), ('intrusive', 'Intrusive'), ('malware', 'Malware'), ('safe', 'Safe'), ('version', 'Version Detection'), ('vuln', 'Vulnerability')], max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='scan',
            name='scan_type',
        ),
        migrations.AddField(
            model_name='scan',
            name='scan_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FirstTry.nmapscripttype'),
            preserve_default=False,
        ),
    ]
