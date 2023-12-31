from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
import jdatetime
from django.utils import timezone

from .models import Call, SoldProduct
from django.contrib.auth.models import User


def month_difference(jdate1, jdate2):
    return (
        (jdate1.year - jdate2.year) * 360
        + (jdate1.month - jdate2.month) * 30
        + (jdate1.day + 7 - jdate2.day)
    ) / 30


now = jdatetime.datetime.fromgregorian(datetime=timezone.now())


@staff_member_required
@require_POST
def update_call(request):
    # Logic to update Call based on SoldProduct and Product

    # تعداد اپراتورها = تعداد یوزر ها - ۲
    operator_count = User.objects.count() - 2

    counter = 1
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
        months_since_sell = int(
            month_difference(current_date, sold_product.date_of_sell)
        )
        print(months_since_sell, "kiiiiiiiiiiiiir")
        detail = " "
        for index, filter_duration in enumerate(filters, 1):
            # Assuming `filter_duration` is the number of months after which the filter should be replaced
            print(filter_duration)
            if months_since_sell != 0:
                if months_since_sell % filter_duration == 0:
                    detail += f"فیلتر {index} تعویض شود| "
                    call = Call(
                        customer=sold_product.customer,
                        date=now,
                        details=detail,
                        product=sold_product.product,
                        operator=counter % operator_count,
                    )
                    calls = Call.objects.filter(customer=sold_product.customer)
                    if calls:
                        calls.update(
                            customer=sold_product.customer,
                            date=now,
                            details=detail,
                            operator=(counter % operator_count) + 1,
                        )
                    else:
                        call.save()
                    counter += 1

    messages.success(request, "‌تماس‌ها با موفقیت بروزرسانی شدند")
    return redirect("admin:dashboard_call_changelist")
