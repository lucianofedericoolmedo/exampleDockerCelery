# Generated by Django 2.0.7 on 2018-12-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181203_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacion',
            name='representacion_json',
            field=models.TextField(blank=True),
        ),
    ]