# Generated by Django 3.1.7 on 2021-04-06 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210406_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navbar',
            old_name='title',
            new_name='page1',
        ),
    ]