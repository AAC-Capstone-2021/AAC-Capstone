# Generated by Django 3.1.6 on 2021-12-04 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0008_auto_20211203_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultcommunicate',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 4, 2, 0, 53, 239305, tzinfo=utc)),
        ),
    ]
