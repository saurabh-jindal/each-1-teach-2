# Generated by Django 3.1.1 on 2020-09-15 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='children',
            new_name='parent',
        ),
    ]
