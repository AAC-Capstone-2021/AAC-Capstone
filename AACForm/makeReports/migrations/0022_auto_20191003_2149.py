# Generated by Django 2.2.5 on 2019-10-04 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0021_auto_20191003_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='beginData',
        ),
        migrations.RemoveField(
            model_name='report',
            name='endData',
        ),
    ]