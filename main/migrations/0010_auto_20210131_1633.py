# Generated by Django 3.1.5 on 2021-01-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210130_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodes',
            name='imgurl',
            field=models.CharField(default='http://192.46.232.232/static/images/TvseriesImg/Friends%20Season%201.webp', max_length=1000),
        ),
        migrations.AddField(
            model_name='episodes',
            name='suburl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='episodes',
            name='vidurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='movies',
            name='suburl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='movies',
            name='vidurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='suburl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='vidurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='movies',
            name='bigimgurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='movies',
            name='imgurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='tvshows',
            name='bigimgurl',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='tvshows',
            name='imgurl',
            field=models.CharField(default='', max_length=1000),
        ),
    ]