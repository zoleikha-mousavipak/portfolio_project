# Generated by Django 2.0.1 on 2019-02-06 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalproject',
            name='period',
            field=models.DateField(default=datetime.datetime(2019, 2, 6, 19, 43, 36, 442330, tzinfo=utc)),
        ),
    ]
