# Generated by Django 4.1 on 2022-09-03 13:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_alter_complent_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sector',
            new_name='Departiment',
        ),
    ]
