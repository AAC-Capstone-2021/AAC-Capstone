# Generated by Django 2.2.5 on 2019-10-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0029_auto_20191009_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentversion',
            name='sampleDescription',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]