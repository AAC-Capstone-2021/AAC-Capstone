# Generated by Django 3.1.6 on 2021-12-05 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0011_auto_20211205_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultcommunicate',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 5, 20, 44, 20, 558541, tzinfo=utc)),
        ),
    ]
