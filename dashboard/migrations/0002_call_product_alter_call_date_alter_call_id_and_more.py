# Generated by Django 4.2.4 on 2023-11-29 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="call",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.product",
            ),
        ),
        migrations.AlterField(
            model_name="call",
            name="date",
            field=django_jalali.db.models.jDateField(
                default=datetime.date(2023, 11, 29), verbose_name="تاریخ تماس"
            ),
        ),
        migrations.AlterField(
            model_name="call",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="logmodel",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="notsoldproduct",
            name="date_of_call",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 6, 19, 35, 206241, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ تماس",
            ),
        ),
        migrations.AlterField(
            model_name="notsoldproduct",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="due_date_time",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 6, 19, 35, 206241, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ و زمان تعیین شده",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="soldproduct",
            name="date_of_sell",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 6, 19, 35, 206241, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ فروش",
            ),
        ),
        migrations.AlterField(
            model_name="soldproduct",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="technician",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
