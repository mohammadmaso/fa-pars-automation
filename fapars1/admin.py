from admin_site_search.views import AdminSiteSearchView
from django.contrib import admin


class MyAdminSite(AdminSiteSearchView, admin.AdminSite):
    ...
