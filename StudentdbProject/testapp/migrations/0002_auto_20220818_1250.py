# Generated by Django 3.2.6 on 2022-08-18 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo3',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='studentinfo3',
            old_name='l_name',
            new_name='last_name',
        ),
    ]