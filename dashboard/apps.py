from django.apps import AppConfig

from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = "fapars1.admin.MyAdminSite"
    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboard"
    verbose_name = "داشبورد"
