# Generated by Django 3.1.1 on 2020-10-11 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_auto_20201011_0439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='uname',
            new_name='u_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='tname',
            new_name='t_name',
        ),
    ]