from django.urls import path
from . import views

urlpatterns = [
    path('custom_admin/', views.custom_admin_view, name='custom_admin_view'),
    path('custom_admin/edit_article/<int:pk>/', views.edit_article, name='edit_article'),
    path('custom_admin/edit_custom_user/<int:pk>/', views.edit_custom_user, name='edit_custom_user'),
    path('custom_admin/edit_comment/<int:pk>/', views.edit_comment, name='edit_comment'),
]
