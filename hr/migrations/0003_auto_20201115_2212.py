# Generated by Django 3.1.2 on 2020-11-15 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20201115_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 15, 22, 12, 41, 688983), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 15, 22, 12, 41, 690057), null=True),
        ),
    ]
