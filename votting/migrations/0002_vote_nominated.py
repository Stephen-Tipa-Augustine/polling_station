# Generated by Django 2.2.1 on 2019-06-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='nominated',
            field=models.BooleanField(default=False, help_text='Nominated Candidate'),
        ),
    ]
