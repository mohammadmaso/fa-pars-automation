# Generated by Django 4.2.4 on 2023-11-28 10:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Call",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    django_jalali.db.models.jDateField(
                        default=datetime.date(2023, 11, 28), verbose_name="تاریخ تماس"
                    ),
                ),
                (
                    "is_called",
                    models.BooleanField(
                        default=False, verbose_name="تماس اول صورت گرفته است؟"
                    ),
                ),
                (
                    "respond",
                    models.CharField(
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
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
            ],
            options={
                "verbose_name": "تماس",
                "verbose_name_plural": "تماس\u200cها",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_number",
                    models.CharField(default=-1, max_length=10, verbose_name="اشتراک"),
                ),
                (
                    "number",
                    models.CharField(
                        default=-1, max_length=20, verbose_name="شماره موبایل"
                    ),
                ),
                (
                    "home_number",
                    models.CharField(
                        default=-1, max_length=20, verbose_name="شماره تلفن"
                    ),
                ),
                (
                    "backup_number",
                    models.CharField(
                        max_length=20, null=True, verbose_name="شماره تلفن پشتیبان"
                    ),
                ),
                ("address", models.TextField(verbose_name="آدرس")),
                (
                    "region_number",
                    models.IntegerField(default=-1, verbose_name=" منطقه"),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="نام خانوادگی"),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
                (
                    "attitude",
                    models.TextField(
                        blank=True, null=True, verbose_name="ویژگی\u200cهای شخصیتی"
                    ),
                ),
                (
                    "reff",
                    models.CharField(default=-1, max_length=10, verbose_name="معرف"),
                ),
            ],
            options={
                "verbose_name": "مشتری",
                "verbose_name_plural": "مشتریان",
            },
        ),
        migrations.CreateModel(
            name="LogModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "فعالیت کارکنان",
                "verbose_name_plural": "فعالیت\u200cهای کارکنان",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model_number",
                    models.CharField(
                        default=-1, max_length=50, verbose_name="شماره مدل"
                    ),
                ),
                (
                    "model_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="نام"
                    ),
                ),
                (
                    "filter1",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 1 - دوره تعویض"
                    ),
                ),
                (
                    "filter2",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 2 - دوره تعویض"
                    ),
                ),
                (
                    "filter3",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 3 - دوره تعویض"
                    ),
                ),
                (
                    "filter4",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 4 - دوره تعویض"
                    ),
                ),
                (
                    "filter5",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 5 - دوره تعویض"
                    ),
                ),
                (
                    "filter6",
                    models.SmallIntegerField(
                        default=-1, verbose_name="فیلتر 6 - دوره تعویض"
                    ),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
            ],
            options={
                "verbose_name": "محصول",
                "verbose_name_plural": "محصولات",
            },
        ),
        migrations.CreateModel(
            name="Technician",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="نام خانوادگی"),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
                (
                    "region",
                    models.IntegerField(
                        default=-1, verbose_name="منطقه\u200cی محل زندگی"
                    ),
                ),
            ],
            options={
                "verbose_name": "تکنسین",
                "verbose_name_plural": "تکنسین\u200cها",
            },
        ),
        migrations.CreateModel(
            name="SoldProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_of_sell",
                    django_jalali.db.models.jDateTimeField(
                        default=datetime.datetime(
                            2023,
                            11,
                            28,
                            10,
                            8,
                            56,
                            401784,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="تاریخ فروش",
                    ),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
                (
                    "calls",
                    models.ManyToManyField(
                        blank=True, to="dashboard.call", verbose_name="تماس\u200cها"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.customer",
                        verbose_name="مشتری",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.product",
                        verbose_name="محصول",
                    ),
                ),
            ],
            options={
                "verbose_name": "محصول فروخته شده",
                "verbose_name_plural": "محصولات فروخته شده",
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "due_date_time",
                    django_jalali.db.models.jDateTimeField(
                        default=datetime.datetime(
                            2023,
                            11,
                            28,
                            10,
                            8,
                            56,
                            401784,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="تاریخ و زمان تعیین شده",
                    ),
                ),
                (
                    "is_done",
                    models.BooleanField(default=False, verbose_name="انجام شده؟"),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.customer",
                        verbose_name="مشتری",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.product",
                        verbose_name="محصول مرتبط",
                    ),
                ),
                (
                    "technician",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.technician",
                        verbose_name="تکنسین",
                    ),
                ),
            ],
            options={
                "verbose_name": "سرویس",
                "verbose_name_plural": "سرویس\u200cها",
            },
        ),
        migrations.CreateModel(
            name="NotSoldProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_of_call",
                    django_jalali.db.models.jDateTimeField(
                        default=datetime.datetime(
                            2023,
                            11,
                            28,
                            10,
                            8,
                            56,
                            401784,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="تاریخ تماس",
                    ),
                ),
                (
                    "details",
                    models.TextField(blank=True, null=True, verbose_name="جزئیات"),
                ),
                (
                    "calls",
                    models.ManyToManyField(
                        blank=True, to="dashboard.call", verbose_name="تماس\u200cها"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.customer",
                        verbose_name="مشتری",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.product",
                        verbose_name="محصول",
                    ),
                ),
            ],
            options={
                "verbose_name": "محصول تعویق فروش",
                "verbose_name_plural": "محصولات تعویق فروش",
            },
        ),
        migrations.AddField(
            model_name="call",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.customer",
                verbose_name="مشتری",
            ),
        ),
        migrations.AddField(
            model_name="call",
            name="service",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.service",
                verbose_name="سرویس مرتبط",
            ),
        ),
    ]
