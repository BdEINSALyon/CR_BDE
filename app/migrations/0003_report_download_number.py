# Generated by Django 2.2.2 on 2019-06-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190619_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='download_number',
            field=models.IntegerField(default=0),
        ),
    ]
