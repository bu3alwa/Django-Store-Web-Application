# Generated by Django 2.0.2 on 2018-05-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20180506_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='gotaptransactions',
            name='urlreponse',
            field=models.TextField(null=True),
        ),
    ]