# Generated by Django 3.1.7 on 2021-04-06 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navbar',
            old_name='nav',
            new_name='title',
        ),
    ]
