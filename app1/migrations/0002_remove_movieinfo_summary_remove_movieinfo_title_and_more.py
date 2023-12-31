# Generated by Django 4.2.6 on 2023-11-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfo',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='movieinfo',
            name='title',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='designed_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='developer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='language',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='os',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
