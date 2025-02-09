from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,Category,Cycle,Course,CoursesPerCycle,Teacher,TeachersPerCourse,Enrollment,Class,Attendance,Test ,TestScore

from .serializers import StudentSerializer,CategorySerializer,CourseSerializer,CycleSerializer,
CoursesPerCycleSerializer,TeacherSerializer,TeachersPerCourseSerializer,EnrollmentSerializer,ClassSerializer,AttendanceSerializer,TestSerializer,TestScoreSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.object.all()
    serializer_class = CategorySerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.object.all()
    serializer_class = CycleSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

class CoursesPerCycleViewSet(viewsets.ModelViewSet):
    queryset = CoursesPerCycle.object.all()
    serializer_class = CoursesPerCycleSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.object.all()
    serializer_class = TeacherSerializer

class TeachersPerCourseViewSet(viewsets.ModelViewSet):
    queryset = TeachersPerCourse.object.all()
    serializer_class = TeachersPerCourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.object.all()
    serializer_class = EnrollmentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.object.all()
    serializer_class = ClassSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.object.all()
    serializer_class = AttendanceSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.object.all()
    serializer_class = TestSerializer

classTestScoreViewSet(viewsets.ModelViewSet):
    queryset = TestScore.object.all()
    serializer_class = TestScoreSerializer
