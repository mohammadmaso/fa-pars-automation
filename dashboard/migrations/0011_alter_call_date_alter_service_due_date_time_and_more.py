# Generated by Django 4.2.4 on 2023-10-19 06:33

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0010_call_customer_alter_service_due_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="call",
            name="date",
            field=django_jalali.db.models.jDateField(
                default=datetime.date(2023, 10, 19), verbose_name="تاریخ تماس"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="due_date_time",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 10, 19, 6, 33, 0, 749341, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ و زمان تعیین شده",
            ),
        ),
        migrations.AlterField(
            model_name="soldproduct",
            name="date_of_sell",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 10, 19, 6, 33, 0, 749341, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ فروش",
            ),
        ),
    ]
