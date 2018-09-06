# Generated by Django 2.1 on 2018-09-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20180831_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediapartner',
            name='logo_url',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='partner',
            name='logo_url',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='logo_url',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='full_name',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО или название'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='full_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название компании'),
        ),
    ]
