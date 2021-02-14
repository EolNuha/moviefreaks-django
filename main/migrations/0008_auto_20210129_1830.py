# Generated by Django 3.1.5 on 2021-01-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_movies_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('seasons', models.IntegerField(default=0)),
                ('episodes', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='bigimgurl',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='bigimgurl',
            field=models.CharField(default='', max_length=300),
        ),
    ]