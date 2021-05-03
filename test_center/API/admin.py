from django.contrib import admin
from .models import Student, EnglishTest, Attempt


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', ]
    ordering = ['name']


@admin.register(EnglishTest)
class TestAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', ]
    ordering = ['name']

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    search_fields = ['test', 'student']
    list_display = ['student', 'test', 'score', 'created_at', ]
    ordering = ['test']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
