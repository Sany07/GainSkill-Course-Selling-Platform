# Generated by Django 3.0.8 on 2020-07-23 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.EmailField(max_length=13)),
                ('address', models.CharField(max_length=50)),
                ('Street_addreess', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Billing',
                'verbose_name_plural': 'Billings',
                'db_table': 'billing',
            },
        ),
    ]
