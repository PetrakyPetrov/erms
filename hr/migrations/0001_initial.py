# Generated by Django 3.1.2 on 2020-11-14 12:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 14, 14, 33, 44, 241123), null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('salary', models.FloatField()),
                ('salary_type', models.CharField(choices=[('m', 'monthly'), ('a', 'annually')], max_length=1)),
                ('address', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 14, 14, 33, 44, 242244), null=True)),
                ('comment_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hr.comment')),
                ('department_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='hr.department')),
                ('job_position_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='hr.jobposition')),
                ('manager_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hr.employee')),
            ],
            options={
                'permissions': (('add', 'Add'), ('edit', 'Edit'), ('delete', 'Delete')),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='employee_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hr.employee'),
        ),
    ]
