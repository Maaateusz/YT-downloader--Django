# Generated by Django 4.1.1 on 2022-10-03 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_rename_history_downloadhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadhistory',
            name='file_format',
        ),
        migrations.AddField(
            model_name='downloadhistory',
            name='file_author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
