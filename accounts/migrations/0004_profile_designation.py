# Generated by Django 3.0.8 on 2020-07-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
