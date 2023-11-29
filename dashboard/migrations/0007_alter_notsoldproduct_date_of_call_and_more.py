# Generated by Django 4.2.4 on 2023-11-29 08:36

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_alter_notsoldproduct_date_of_call_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notsoldproduct",
            name="date_of_call",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 8, 36, 44, 808338, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ تماس",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter1",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 1 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter2",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 2 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter3",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 3 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter4",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 4 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter5",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 5 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="filter6",
            field=models.PositiveIntegerField(
                default=1, verbose_name="فیلتر 6 - دوره تعویض"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="due_date_time",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 8, 36, 44, 808338, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ و زمان تعیین شده",
            ),
        ),
        migrations.AlterField(
            model_name="soldproduct",
            name="date_of_sell",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 8, 36, 44, 808338, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ فروش",
            ),
        ),
    ]
