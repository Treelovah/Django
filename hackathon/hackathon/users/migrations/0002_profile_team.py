# Generated by Django 3.1.1 on 2020-10-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.CharField(choices=[('kss', 'kryptsec'), ('hsh', 'hashdump'), ('mum', 'hackerMums'), ('fac', 'faculty')], default=None, max_length=30),
        ),
    ]
