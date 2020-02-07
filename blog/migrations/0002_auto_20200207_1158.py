# Generated by Django 2.2.9 on 2020-02-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='charge',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='flgStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='introMethod',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='ionKind',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='ionMethod',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='mass',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='remarks',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='resolution',
            field=models.CharField(default='', max_length=20),
        ),
    ]
