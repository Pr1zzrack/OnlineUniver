from rest_framework import viewsets
from .models import Course, Student, Professor, Department, RegCourse
from .serializers import CourseSerializer, StudentSerializer, ProfessorSerializer, DepartmentSerializer, RegCourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['department', 'professor']
    search_fields = ['name', 'professor__user__username']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class RegCourseViewSet(viewsets.ModelViewSet):
    queryset = RegCourse.objects.all()
    serializer_class = RegCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'course']
