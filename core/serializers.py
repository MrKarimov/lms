from rest_framework import serializers
from .models import (
   Category,Lesson,Enrollment,
    Course, CustomUser
    
)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # Barcha maydonlarni qo'shish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Barcha maydonlarni qo'shish

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Barcha maydonlarni qo'shish


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Barcha maydonlarni qo'shish


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'  # Barcha maydonlarni qo'shish
