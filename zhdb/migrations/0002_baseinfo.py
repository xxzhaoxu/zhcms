# Generated by Django 3.0.4 on 2020-03-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_side_name', models.CharField(max_length=50)),
                ('logo_url', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('record_number', models.CharField(max_length=20)),
            ],
        ),
    ]