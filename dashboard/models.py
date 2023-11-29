from django.db import models
from django_jalali.db import models as jmodels

from django.utils import timezone
from django.db import models
import datetime
import jdatetime

from auditlog.models import AuditlogHistoryField

from auditlog.registry import auditlog


now = jdatetime.datetime.fromgregorian(datetime=timezone.now())


class LogModel(models.Model):
    class Meta:
        verbose_name = "فعالیت کارکنان"
        verbose_name_plural = "فعالیت‌های کارکنان"

    pass


auditlog.register(LogModel)


class Customer(models.Model):
    id_number = models.CharField(default=-1, max_length=10, verbose_name="اشتراک")
    number = models.CharField(default=-1, max_length=20, verbose_name="شماره موبایل")
    home_number = models.CharField(default=-1, max_length=20, verbose_name="شماره تلفن")
    backup_number = models.CharField(
        null=True, blank=True, max_length=20, verbose_name="شماره تلفن پشتیبان"
    )
    address = models.TextField(verbose_name="آدرس")
    region_number = models.IntegerField(default=-1, verbose_name=" منطقه")
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")
    attitude = models.TextField(blank=True, null=True, verbose_name="ویژگی‌های شخصیتی")
    reff = models.CharField(default=-1, max_length=10, verbose_name="معرف")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Product(models.Model):
    model_number = models.CharField(default=-1, max_length=50, verbose_name="شماره مدل")
    model_name = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="نام"
    )
    filter1 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 1 - دوره تعویض"
    )
    filter2 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 2 - دوره تعویض"
    )
    filter3 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 3 - دوره تعویض"
    )
    filter4 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 4 - دوره تعویض"
    )
    filter5 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 5 - دوره تعویض"
    )
    filter6 = models.PositiveIntegerField(
        default=1, verbose_name="فیلتر 6 - دوره تعویض"
    )
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")

    def __str__(self):
        return f"{self.model_name}"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class SoldProduct(models.Model):
    date_of_sell = jmodels.jDateTimeField(default=now, verbose_name="تاریخ فروش")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="محصول"
    )
    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, verbose_name="مشتری"
    )
    calls = models.ManyToManyField("Call", verbose_name="تماس‌ها", blank=True)
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")

    def __str__(self):
        return f"فروش محصول به {self.customer} در تاریخ {self.date_of_sell}"

    class Meta:
        verbose_name = "محصول فروخته شده"
        verbose_name_plural = "محصولات فروخته شده"


class Call(models.Model):
    customer = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True, verbose_name="مشتری"
    )
    date = jmodels.jDateField(default=now, verbose_name="تاریخ تماس")
    is_called = models.BooleanField(
        default=False, verbose_name="تماس اول صورت گرفته است؟"
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="محصول",
    )
    respond = models.CharField(
        max_length=50,
        choices=[
            ("not_answered", "پاسخ داده نشد"),
            ("set_time", "تعیین زمان صورت گرفته است."),
            ("recall", "یادآوری دوباره شود"),
            ("self", "خودم تعویض می‌کنم"),
        ],
        verbose_name="پاسخ",
    )
    # recall_date = jmodels.jDateField(null=True,verbose_name='تاریخ تماس دوباره')
    details = models.TextField(verbose_name="جزئیات", null=True, blank=True)
    operator = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="اپراتور مسئول"
    )
    service = models.OneToOneField(
        "Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="سرویس مرتبط",
    )

    def __str__(self):
        return f"تماس در تاریخ {self.date}"

    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس‌ها"


class Service(models.Model):
    customer = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True, verbose_name="مشتری"
    )
    due_date_time = jmodels.jDateTimeField(
        default=now, verbose_name="تاریخ و زمان تعیین شده"
    )
    technician = models.ForeignKey(
        "Technician", on_delete=models.SET_NULL, null=True, verbose_name="تکنسین"
    )
    is_done = models.BooleanField(default=False, verbose_name="انجام شده؟")
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, verbose_name="محصول مرتبط"
    )
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")

    def __str__(self):
        return f"سرویس برای {self.technician}"

    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس‌ها"


class Technician(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")
    region = models.IntegerField(default=-1, verbose_name="منطقه‌ی محل زندگی")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "تکنسین"
        verbose_name_plural = "تکنسین‌ها"


class NotSoldProduct(models.Model):
    date_of_call = jmodels.jDateTimeField(default=now, verbose_name="تاریخ تماس")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="محصول"
    )
    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, verbose_name="مشتری"
    )
    calls = models.ManyToManyField("Call", verbose_name="تماس‌ها", blank=True)
    details = models.TextField(null=True, blank=True, verbose_name="جزئیات")

    def __str__(self):
        return f"فروش محصول به {self.customer} در تاریخ {self.date_of_call}"

    class Meta:
        verbose_name = "محصول تعویق فروش"
        verbose_name_plural = "محصولات تعویق فروش"
