# Generated by Django 2.2.5 on 2019-09-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0010_auto_20190930_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradedrubric',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
