# Generated by Django 3.1.2 on 2020-10-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_mascota_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_mascota', models.CharField(max_length=50)),
            ],
        ),
    ]
