# Generated by Django 4.2.5 on 2023-09-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Avatar'),
        ),
    ]
