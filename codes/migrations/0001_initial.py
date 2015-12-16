# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 14:55
from __future__ import unicode_literals

import codes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passes', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(unique=True)),
                ('score', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=models.SET(codes.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IOTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField()),
                ('output_data', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_text', models.TextField()),
                ('access_flag', models.IntegerField(choices=[(1, 'Hidden'), (2, 'Readable'), (3, 'Writable')])),
            ],
        ),
        migrations.CreateModel(
            name='SnippetSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.Snippet')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
                ('date', models.DateTimeField(verbose_name='creation date')),
                ('author', models.ForeignKey(on_delete=models.SET(codes.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('snippets', models.ManyToManyField(through='codes.SnippetSource', to='codes.Snippet')),
            ],
        ),
        migrations.AddField(
            model_name='snippetsource',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.Source'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sources',
            field=models.ManyToManyField(to='codes.Source'),
        ),
        migrations.AddField(
            model_name='answer',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.Exercise'),
        ),
        migrations.AddField(
            model_name='answer',
            name='sources',
            field=models.ManyToManyField(to='codes.Source'),
        ),
    ]