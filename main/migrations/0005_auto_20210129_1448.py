# Generated by Django 3.1.5 on 2021-01-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210129_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='imgurl',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='imgurl',
            field=models.CharField(default='', max_length=300),
        ),
    ]