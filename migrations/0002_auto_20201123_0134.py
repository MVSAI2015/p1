# Generated by Django 3.0 on 2020-11-22 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='ingredents',
            new_name='ingredients',
        ),
    ]
