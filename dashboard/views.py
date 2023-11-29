from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
import jdatetime
from django.utils import timezone

from .models import Call, SoldProduct


def month_difference(jdate1, jdate2):
    return (
        ((jdate1.year - jdate2.year) * 12) * 360
        + (jdate1.month - jdate2.month) * 30
        + (jdate1.day + 7 - jdate2.day)
    ) / 30


now = jdatetime.datetime.fromgregorian(datetime=timezone.now())


@staff_member_required
@require_POST
def update_call(request):
    # Logic to update Call based on SoldProduct and Product
    for sold_product in SoldProduct.objects.all():
        product = sold_product.product
        filters = [
            product.filter1,
            product.filter2,
            product.filter3,
            product.filter4,
            product.filter5,
            product.filter6,
        ]

        current_date = jdatetime.date.today()
        months_since_sell = month_difference(current_date, sold_product.date_of_sell)
        detail = " "
        for index, filter_duration in enumerate(filters, 1):
            # Assuming `filter_duration` is the number of months after which the filter should be replaced

            detail += f"فیلتر {index} تعویض شود| "
            if months_since_sell != 0:
                if filter_duration // months_since_sell == 0:
                    call = Call(
                        customer=sold_product.customer, date=now, details=detail
                    )
                calls = Call.objects.filter(
                    customer=sold_product.customer, product=sold_product.product
                )
                if calls:
                    calls.update(
                        customer=sold_product.customer, date=now, details=detail
                    )
                else:
                    call.save()

    messages.success(request, "‌تماس‌ها با موفقیت بروزرسانی شدند")
    return redirect("admin:dashboard_call_changelist")
