from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Department)
class DepartmentTranslation(TranslationOptions):
    fields = ("name", "description")

@register(Professor)
class ProfessorTranslation(TranslationOptions):
    fields = ("user", "department", "title", "bio")

@register(Student)
class StudentTranslation(TranslationOptions):
    fields = ("user", "department", "enrollment_date", "graduation_date")

@register(Course)
class CourseTranslation(TranslationOptions):
    fields = ("name", "code", "description", "department", "professor")

@register(Room)
class RoomTranslation(TranslationOptions):
    fields = ("room_number", "building", "capacity")

@register(Schedule)
class ScheduleTranslation(TranslationOptions):
    fields = ("course", "classroom", "start_time", "end_time", "day_of_week")

@register(RegCourse)
class RegCourseTranslation(TranslationOptions):
    fields = ("student", "course", "date_enrolled", "grade")

@register(HomeWork)
class HomeWorkTranslation(TranslationOptions):
    fields = ("course", "title", "description", "due_date")

@register(HandingHomeWork)
class HandingHomeWorkTranslation(TranslationOptions):
    fields = ("assignment", "student", "submission_date", "grade", "feedback")

