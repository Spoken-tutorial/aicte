from django.contrib import admin
from institute.models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    fields = ['name']

class StateAdmin(admin.ModelAdmin):
    fields = ['name']

class CityAdmin(admin.ModelAdmin):
    fields = ['name', 'state']

class DistrictAdmin(admin.ModelAdmin):
    fields = ['name', 'state']

class UniversityAdmin(admin.ModelAdmin):
    fields = ['name']

class CollegeCourseInline(admin.TabularInline):
    model = CollegeCourse
    extra = 0

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'district', 'website')
    inlines = [CollegeCourseInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(College, CollegeAdmin)
