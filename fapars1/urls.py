"""fapars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dashboard.views import update_call
from dashboard.admin import MyAdminSite


urlpatterns = [
    path("update_call/", update_call, name="update_call"),
    path("admin/", MyAdminSite.site.urls),
    # path("admin_tools_stats/", include("admin_tools_stats.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "فا پارس"  # default: "Django Administration"
admin.site.index_title = "اتوماسیون فاپارس"  # default: "Site administration".
admin.site.site_title = "پنل کاربری"  # default: "Django site admin"
