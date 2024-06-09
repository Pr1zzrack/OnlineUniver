from rest_framework import serializers
from .models import Course, Student, Professor, Department, RegCourse, HomeWork, HandingHomeWork


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegCourse
        fields = '__all__'


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = '__all__'


class HandingHomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandingHomeWork
        fields = '__all__'
