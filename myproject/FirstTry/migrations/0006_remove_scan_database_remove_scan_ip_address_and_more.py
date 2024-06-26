# Generated by Django 5.0.3 on 2024-05-02 13:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstTry', '0005_schedule_target'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scan',
            name='dataBase',
        ),
        migrations.RemoveField(
            model_name='scan',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='scan',
            name='name',
        ),
        migrations.RemoveField(
            model_name='scan',
            name='recurrence',
        ),
        migrations.RemoveField(
            model_name='scan',
            name='start_time',
        ),
        migrations.AddField(
            model_name='scan',
            name='Scan_Name',
            field=models.CharField(default='Default', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='target',
            name='Target_Name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('Creation_Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstTry.scan')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstTry.schedule')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstTry.target')),
            ],
        ),
    ]
