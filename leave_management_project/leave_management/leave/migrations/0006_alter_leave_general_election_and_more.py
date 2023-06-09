# Generated by Django 4.2.1 on 2023-05-31 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_alter_leave_casual_leave_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='general_election',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='leave',
            name='paternity_leave',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='leave_balance',
            name='paternity_leave_balance',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
