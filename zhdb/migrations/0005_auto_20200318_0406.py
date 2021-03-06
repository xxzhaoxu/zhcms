# Generated by Django 3.0.4 on 2020-03-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0004_auto_20200317_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=20)),
                ('job_desc', models.CharField(max_length=255)),
                ('professional', models.CharField(max_length=255)),
                ('education_level', models.CharField(max_length=255)),
                ('work_address', models.CharField(max_length=255)),
                ('people_number', models.CharField(max_length=255)),
                ('work_age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('people_age', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=10)),
                ('work_range', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
