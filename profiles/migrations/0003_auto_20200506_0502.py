# Generated by Django 3.0.5 on 2020-05-06 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20200506_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address1',
            field=models.CharField(default='lastname', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address2',
            field=models.CharField(default='lastname', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
