# Generated by Django 4.1 on 2022-09-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_sector_departiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255, null=True)),
                ('lname', models.CharField(max_length=255, null=True)),
                ('sid', models.CharField(max_length=255, unique=True)),
                ('age', models.DateField(null=True)),
                ('regdate', models.DateField(auto_now_add=True)),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('father', models.CharField(max_length=255, null=True)),
                ('focopation', models.CharField(max_length=255, null=True)),
                ('sregion', models.CharField(max_length=255, null=True)),
                ('zone', models.CharField(max_length=255, null=True)),
                ('woreda', models.CharField(max_length=255, null=True)),
                ('kebele', models.CharField(max_length=255, null=True)),
                ('currentposion', models.CharField(max_length=255, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('fphone', models.IntegerField(null=True)),
                ('fage', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('disablity', models.CharField(max_length=100, null=True)),
                ('dskind', models.CharField(max_length=255, null=True)),
                ('status', models.BooleanField()),
            ],
        ),
    ]