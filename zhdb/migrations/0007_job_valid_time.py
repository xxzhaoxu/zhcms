# Generated by Django 3.0.4 on 2020-03-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0006_job_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='valid_time',
            field=models.IntegerField(null=True),
        ),
    ]