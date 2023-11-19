# Generated by Django 4.2.4 on 2023-08-29 02:03

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_call_recall_date_customer_home_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="call",
            name="is_answered",
        ),
        migrations.AddField(
            model_name="call",
            name="is_called",
            field=models.BooleanField(
                default=False, verbose_name="تماس اول صورت گرفته است؟"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="due_date_time",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 8, 29, 2, 3, 36, 535877, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ و زمان تعیین شده",
            ),
        ),
    ]
