from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Student,Category,Cycle,
    Course,CoursesPerCycle,
    Teacher,TeachersPerCourse,
    Enrollment,Class,
    Attendance,Test ,TestScore
)

from .serializers import(
    StudentSerializer,CategorySerializer,
    CourseSerializer,CycleSerializer,
    CoursesPerCycleSerializer,
    TeacherSerializer,
    TeachersPerCourseSerializer,
    EnrollmentSerializer,
    ClassSerializer,AttendanceSerializer,
    TestSerializer,TestScoreSerializer
)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursesPerCycleViewSet(viewsets.ModelViewSet):
    queryset = CoursesPerCycle.objects.all()
    serializer_class = CoursesPerCycleSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeachersPerCourseViewSet(viewsets.ModelViewSet):
    queryset = TeachersPerCourse.objects.all()
    serializer_class = TeachersPerCourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestScoreViewSet(viewsets.ModelViewSet):
    queryset = TestScore.objects.all()
    serializer_class = TestScoreSerializer
