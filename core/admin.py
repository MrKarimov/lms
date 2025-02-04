from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Course, Cycle, CoursesPerCycle, Teacher, TeachersPerCourse, Student, Enrollment, Class, Attendance, Test, TestScore

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryId', 'CategoryDescr')
    search_fields = ('CategoryId', 'CategoryDescr')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseId', 'CourseDescription', 'Category')
    search_fields = ('CourseId', 'CourseDescription')
    list_filter = ('Category',)

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('CycleId', 'CycleDescription', 'CycleStartDate', 'CycleEndDate')
    search_fields = ('CycleId', 'CycleDescription')
    list_filter = ('CycleStartDate', 'CycleEndDate')

@admin.register(CoursesPerCycle)
class CoursesPerCycleAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'CourseStartDate', 'CourseEndDate')
    search_fields = ('Course__CourseId', 'Cycle__CycleId')
    list_filter = ('Cycle',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('TeacherId', 'TeacherName', 'Email', 'PhoneNo')
    search_fields = ('TeacherId', 'TeacherName')
    list_filter = ('PhoneNo',)

@admin.register(TeachersPerCourse)
class TeachersPerCourseAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'Teacher')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'Teacher__TeacherName')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentId', 'StudentName', 'Email', 'BirthDate', 'PhoneNo')
    search_fields = ('StudentId', 'StudentName', 'Email')
    list_filter = ('BirthDate',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'Student', 'EnrollmentDate', 'Cancelled')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'Student__StudentName')
    list_filter = ('Cancelled',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'ClassNo', 'Teacher', 'ClassTitle', 'ClassDate', 'StartTime', 'EndTime')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'Teacher__TeacherName')
    list_filter = ('ClassDate', 'StartTime', 'EndTime')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'Class', 'Student', 'TimeArrive', 'TimeLeave')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'Class__ClassNo', 'Student__StudentName')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'TestNo', 'TestDate', 'TestTime', 'Agenda')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'TestNo')
    list_filter = ('TestDate',)

@admin.register(TestScore)
class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Cycle', 'Test', 'Student', 'Score')
    search_fields = ('Course__CourseId', 'Cycle__CycleId', 'Test__TestNo', 'Student__StudentName')
    list_filter = ('Score',)
