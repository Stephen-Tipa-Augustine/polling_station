# Generated by Django 2.2.1 on 2019-06-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestants',
            name='nomination',
            field=models.IntegerField(default=0, help_text='Student Nomination'),
        ),
    ]
