# Generated by Django 2.0.7 on 2018-12-03 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181128_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='operaciondetalle',
            name='status_code',
            field=models.CharField(blank=True, choices=[('201', '201'), ('409', '409')], max_length=15),
        ),
    ]
