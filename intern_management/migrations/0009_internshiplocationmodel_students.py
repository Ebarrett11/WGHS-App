# Generated by Django 2.1.10 on 2019-08-02 01:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intern_management', '0008_auto_20190802_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshiplocationmodel',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
