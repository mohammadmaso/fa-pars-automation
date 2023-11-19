# Generated by Django 4.2.4 on 2023-08-29 08:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0008_remove_call_is_answered_call_is_called_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="call",
            name="recall_date",
        ),
        migrations.AddField(
            model_name="service",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.customer",
                verbose_name="مشتری",
            ),
        ),
        migrations.AlterField(
            model_name="call",
            name="respond",
            field=models.CharField(
                choices=[
                    ("not_answered", "پاسخ داده نشد"),
                    ("set_time", "تعیین زمان صورت گرفته است."),
                    ("recall", "یادآوری دوباره شود"),
                    ("self", "خودم تعویض می\u200cکنم"),
                ],
                max_length=50,
                verbose_name="پاسخ",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="due_date_time",
            field=django_jalali.db.models.jDateTimeField(
                default=datetime.datetime(
                    2023, 8, 29, 8, 6, 21, 133034, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ و زمان تعیین شده",
            ),
        ),
    ]
