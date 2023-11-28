from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = "dashboard.admin.MyAdminSite"
    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboard"
    verbose_name = "داشبورد"
