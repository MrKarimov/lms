from django.db import models

class Category(models.Model):
    CategoryId = models.CharField(max_length=10, primary_key=True)
    CategoryDescr = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryDescr


class Course(models.Model):
    CourseId = models.CharField(max_length=10, primary_key=True)
    CourseDescription = models.CharField(max_length=100)
    Abstract = models.TextField()
    Bibliography = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseDescription


class Cycle(models.Model):
    CycleId = models.CharField(max_length=10, primary_key=True)
    CycleDescription = models.CharField(max_length=100)
    CycleStartDate = models.DateField()
    CycleEndDate = models.DateField()
    VacationStartDate = models.DateField(null=True, blank=True)
    VacationEndDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.CycleDescription


class CoursesPerCycle(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    CourseStartDate = models.DateField()
    CourseEndDate = models.DateField()

    class Meta:
        unique_together = ('Course', 'Cycle')

    def __str__(self):
        return f"{self.Course} - {self.Cycle}"


class Teacher(models.Model):
    TeacherId = models.CharField(max_length=10, primary_key=True)
    TeacherName = models.CharField(max_length=100)
    Email = models.EmailField(null=True, blank=True)
    PhoneNo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.TeacherName


class TeachersPerCourse(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Course', 'Cycle', 'Teacher')

    def __str__(self):
        return f"{self.Teacher} for {self.Course} in {self.Cycle}"


class Student(models.Model):
    StudentId = models.CharField(max_length=10, primary_key=True)
    StudentName = models.CharField(max_length=100)
    Email = models.EmailField(null=True, blank=True)
    BirthDate = models.DateField()
    PhoneNo = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.StudentName


class Enrollment(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    EnrollmentDate = models.DateField()
    Cancelled = models.BooleanField(default=False)
    CancellationReason = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ('Course', 'Cycle', 'Student')

    def __str__(self):
        return f"{self.Student} enrolled in {self.Course}"


class Class(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    ClassNo = models.IntegerField()
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    ClassTitle = models.CharField(max_length=100)
    ClassDate = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    class Meta:
        unique_together = ('Course', 'Cycle', 'ClassNo')

    def __str__(self):
        return f"Class {self.ClassNo} for {self.Course} in {self.Cycle}"


class Attendance(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    TimeArrive = models.TimeField(null=True, blank=True)
    TimeLeave = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ('Course', 'Cycle', 'Class', 'Student')

    def __str__(self):
        return f"{self.Student} attendance in {self.Class}"


class Test(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    TestNo = models.IntegerField()
    TestDate = models.DateField()
    TestTime = models.TimeField()
    Agenda = models.TextField()

    class Meta:
        unique_together = ('Course', 'Cycle', 'TestNo')

    def __str__(self):
        return f"Test {self.TestNo} for {self.Course} in {self.Cycle}"


class TestScore(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('Course', 'Cycle', 'Test', 'Student')

    def __str__(self):
        return f"Score for {self.Student} in {self.Test} for {self.Course}"
