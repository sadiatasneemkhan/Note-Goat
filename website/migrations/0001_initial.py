# Generated by Django 4.0.3 on 2022-03-22 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('folder_name', models.CharField(default='New Folder', max_length=50, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file_name', models.CharField(default='New Note', max_length=50)),
                ('text', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.folder')),
            ],
        ),
        migrations.CreateModel(
            name='SharedWith',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('editor', models.BooleanField(default=False)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.note')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('person', 'note')},
            },
        ),
        migrations.AddField(
            model_name='note',
            name='sharing',
            field=models.ManyToManyField(related_name='shared_notes', through='website.SharedWith', to=settings.AUTH_USER_MODEL),
        ),
    ]
