# Generated by Django 4.2.6 on 2023-11-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_languageinfo_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageinfo',
            name='os',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
