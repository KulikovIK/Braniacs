from django.contrib import admin
from mainapp.models import News, Course, Lesson, CoursesTeacher, CourseFeedback



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted')
    list_filter = ('deleted', 'created_at')
    list_per_page = 10
    search_fields = ('title', 'preview', 'body')
    actions = ('mark_as_deleted',)

    def mark_as_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_deleted.short_description = 'Пометить удаленными'

    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'num', 'title', )
    list_filter = ('deleted', 'course', )
    list_per_page = 10
    actions = ('mark_as_deleted', )

    def mark_as_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_deleted.short_description = 'Пометить удаленными'
    


@admin.register(CoursesTeacher)
class CoursesTeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseFeedback)
class CourseFeedbackAdmin(admin.ModelAdmin):
    pass