# Generated by Django 3.0.4 on 2020-04-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0015_auto_20200326_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shot_time',
            field=models.IntegerField(null=True),
        ),
    ]
