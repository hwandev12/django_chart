# Generated by Django 4.0 on 2022-03-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='valus',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
