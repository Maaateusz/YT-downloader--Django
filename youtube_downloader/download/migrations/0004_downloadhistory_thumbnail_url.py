# Generated by Django 4.1.1 on 2022-10-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0003_remove_downloadhistory_file_format_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadhistory',
            name='thumbnail_url',
            field=models.URLField(default='None'),
            preserve_default=False,
        ),
    ]
