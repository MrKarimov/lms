from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, TeacherViewSet, CourseViewSet, EnrollmentViewSet,
    AttendanceViewSet, TestViewSet, TestScoreViewSet, ClassViewSet,
    CycleViewSet, CategoryViewSet, CoursesPerCycleViewSet, TeachersPerCourseViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test-scores', TestScoreViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'cycles', CycleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'courses-per-cycle', CoursesPerCycleViewSet)
router.register(r'teachers-per-course', TeachersPerCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
