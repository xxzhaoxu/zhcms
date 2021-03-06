# Generated by Django 3.0.4 on 2020-03-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0012_banner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('img_urls', models.CharField(max_length=255)),
                ('create_time', models.IntegerField()),
                ('banner_id', models.IntegerField()),
            ],
        ),
    ]
