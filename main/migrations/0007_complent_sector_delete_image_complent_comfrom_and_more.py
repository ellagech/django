# Generated by Django 4.1 on 2022-09-02 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_rename_user_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=b'I01\n', upload_to='picture')),
                ('uid', models.IntegerField(null=True)),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('memberS', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='complent',
            name='comfrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sector'),
        ),
        migrations.AddField(
            model_name='complent',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
