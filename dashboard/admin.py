from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter
from django.db.models import Q


from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


from .models import Customer

from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "number", "region_number")
    list_filter = ("region_number",)
    search_fields = ("first_name", "last_name", "number", "id_number", "ref")


admin.site.register(Customer, CustomerAdmin)

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "model_number",
        "model_name",
        "filter1",
        "filter2",
        "filter3",
        "filter4",
        "filter5",
        "filter6",
    )
    list_filter = (
        "filter1",
        "filter2",
        "filter3",
        "filter4",
        "filter5",
        "filter6",
    )
    search_fields = ("model_number",)


admin.site.register(Product, ProductAdmin)

from .models import Call, Customer


class CallAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "product",
        "get_address",
        "get_backup_number",
        "get_number",
        "get_id",
        "date",
        "is_called",
        "respond",
        "service",
        "details",
    )

    Product.short_description = "محصول"

    def get_address(self, obj):
        return obj.customer.address

    get_address.short_description = "آدرس مشتری"

    def get_backup_number(self, obj):
        return obj.customer.backup_number

    get_backup_number.short_description = "شماره تماس پشتیبان"

    def get_number(self, obj):
        return obj.customer.number

    get_number.short_description = "شماره تماس اصلی"

    def get_id(self, obj):
        return obj.customer.id_number

    get_id.short_description = "اشتراک"

    list_filter = ("is_called", "respond", "date", "service")
    list_editable = ("is_called", "respond", "service")
    # search_fields = [field.name for field in Call._meta.fields]
    change_list_template = "admin/change_list.html"
    autocomplete_fields = ["customer"]


admin.site.register(Call, CallAdmin)

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("customer", "due_date_time", "technician", "is_done", "product")
    list_filter = ("is_done",)
    list_editable = ("is_done",)

    search_fields = (
        "customer",
        "due_date_time",
        "technician__first_name",
        "technician__last_name",
    )


admin.site.register(Service, ServiceAdmin)

from .models import Technician


class TechnicianAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "region")
    list_filter = ("region",)
    search_fields = ("first_name", "last_name")


admin.site.register(Technician, TechnicianAdmin)


from .models import SoldProduct, NotSoldProduct


class SoldProductAdmin(admin.ModelAdmin):
    list_display = ("date_of_sell", "product", "customer")
    list_filter = (
        "date_of_sell",
        "product",
        "customer",
    )
    search_fields = "date_of_sell"

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(SoldProductAdmin, self).get_search_results(
            request, queryset, search_term
        )

        # If there's no search term, return the original queryset
        if not search_term:
            return queryset, use_distinct

        # Define search in related Author fields
        product_search = Q(product__model_name__icontains=search_term)
        # Add more conditions for other related fields if needed

        # Define search in Book fields
        firstname_search = Q(customer__first_name__icontains=search_term)
        lastname_search = Q(customer__last_name__icontains=search_term)

        # Add more conditions for other Book fields if needed

        # Combine queries
        queryset |= self.model.objects.filter(
            product_search | firstname_search | lastname_search
        )

        return queryset, use_distinct


admin.site.register(SoldProduct, SoldProductAdmin)


class NotSoldProductAdmin(admin.ModelAdmin):
    list_display = ("date_of_call", "product", "customer")
    list_filter = (
        "date_of_call",
        "product",
        "customer",
    )


admin.site.register(NotSoldProduct, NotSoldProductAdmin)
