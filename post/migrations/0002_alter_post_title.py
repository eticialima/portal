# Generated by Django 3.2.9 on 2021-12-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=70, verbose_name='Titulo'),
        ),
    ]
