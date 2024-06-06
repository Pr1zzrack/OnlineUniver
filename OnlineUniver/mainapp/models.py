from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=42, verbose_name='Названия факультета', unique=True)
    description = models.TextField(verbose_name='Описания факультета')

    def __str__(self) -> str:
        return self.name

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Профессор')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Факультет')
    title = models.CharField(max_length=32, verbose_name='Уроки')
    bio = models.TextField(verbose_name='Биография профессора')

    def __str__(self) -> str:
        return self.user

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Студент')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Факультет')
    enrollment_date = models.DateField(verbose_name='Дата начала обучения')
    graduation_date = models.DateField(verbose_name='Дата окончания обучения')

    def __str__(self) -> str:
        return self.user

class Course(models.Model):
    name = models.CharField(max_length=42, verbose_name='Название курса')
    code = models.CharField(max_length=42, verbose_name='Код доступа к курсу')
    description = models.TextField(verbose_name='Описания курса')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Факультет')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Профессор')

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    room_number = models.PositiveSmallIntegerField(unique=True, default=0)
    building = models.PositiveSmallIntegerField(default=1)
    capacity = models.PositiveSmallIntegerField(default=10)

    def __str__(self) -> str:
        return self.room_number

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Кабинет')
    start_time = models.TimeField()
    end_time = models.TimeField()
    DAY_OF_WEEK = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]
    day_of_week = models.CharField(max_length=20, choices=DAY_OF_WEEK)

    def __str__(self) -> str:
        return self.course

class RegCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self) -> str:
        return f"Студент: {self.student} Курс: {self.course}"

class HomeWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=42, verbose_name='Название задания')
    description = models.TextField(verbose_name='Описания задания')
    due_date = models.DateTimeField(verbose_name='Дедлайн')

    def __str__(self) -> str:
        return f"{self.course} - {self.title}"

class HandingHomeWork(models.Model):
    assignment = models.ForeignKey(HomeWork, on_delete=models.CASCADE, verbose_name='Задание')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    submission_date = models.DateTimeField(verbose_name='Время сдачи')
    grade = models.CharField(max_length=5, verbose_name='Оценка')
    feedback = models.TextField(verbose_name='Комментарий')

    def __str__(self) -> str:
        return f"{self.student} - {self.assignment}"




# Аззам:
# regist, google + github
# ru en ky
# docker + aws


# Актан:
# crud
# filter(depart, proffes (course))
# search (cou name,stud name, prof name)