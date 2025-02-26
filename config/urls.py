from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from admin_dashboard import views as admin_views
from django.conf.urls.static import static
urlpatterns = [
    path('admins/', admin_views.custom_admin_view, name='custom_admin_dashboard'),
     path('admins/', include('admin_dashboard.urls')),
    path('comments/', include('comments.urls')),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('articles/', include("articles.urls")),
    path('',  include("pages.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
