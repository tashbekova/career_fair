# Generated by Django 2.1 on 2018-08-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FairInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('target', models.TextField(blank=True, null=True, verbose_name='Цель')),
                ('mission', models.TextField(blank=True, null=True, verbose_name='Миссии')),
                ('task', models.TextField(blank=True, null=True, verbose_name='Задачи')),
            ],
            options={
                'verbose_name': 'Information about Career fair',
                'verbose_name_plural': 'Information about Career fair',
            },
        ),
    ]
