# Generated by Django 4.1 on 2022-09-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_lectur_alter_departiment_admin_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectur',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lectur',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
