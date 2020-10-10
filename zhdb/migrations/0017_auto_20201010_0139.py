# Generated by Django 3.0.4 on 2020-10-10 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhdb', '0016_news_shot_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('m_address', models.CharField(max_length=255)),
                ('msg', models.CharField(max_length=255)),
                ('stats', models.CharField(max_length=255)),
                ('create_time', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]