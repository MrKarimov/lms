from rest_framework import serializers
from .models import (
    Student,Category,Cycle,
    Course,CoursesPerCycle,
    Teacher,TeachersPerCourse,
    Enrollment,Class,
    Attendance,Test ,TestScore
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Barcha maydonlarni qo'shish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Barcha maydonlarni qo'shish

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Barcha maydonlarni qo'shish


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'  # Barcha maydonlarni qo'shish


class CoursesPerCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesPerCycle
        fields = '__all__'  # Barcha maydonlarni qo'shish


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'  # Barcha maydonlarni qo'shish


class TeachersPerCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersPerCourse
        fields = '__all__'  # Barcha maydonlarni qo'shish


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'  # Barcha maydonlarni qo'shish



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'  # Barcha maydonlarni qo'shish

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields='__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields='__all__'

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields='__all__'










