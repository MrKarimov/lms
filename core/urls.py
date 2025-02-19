from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LessonViewSet, CourseViewSet, EnrollmentViewSet,
    CategoryViewSet, CustomUserViewSet
)

router = DefaultRouter()
router.register(r'lessons',LessonViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
