from django.urls import path
from .views import CourseViewSet, StudentViewSet, ProfessorViewSet, DepartmentViewSet, RegCourseViewSet


urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='course-detail'),
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='student-detail'),
    path('professors/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='professor-list'),
    path('professors/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='professor-detail'),
    path('departments/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='department-list'),
    path('departments/<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='department-detail'),
    path('regcourses/', RegCourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='regcourse-list'),
    path('regcourses/<int:pk>/', RegCourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='regcourse-detail'),
]
