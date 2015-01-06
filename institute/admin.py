from django.contrib import admin
from institute.models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    fields = ['name']

class DistrictAdmin(admin.ModelAdmin):
    fields = ['name']

class UniversityAdmin(admin.ModelAdmin):
    fields = ['name']

class InstituteTypeAdmin(admin.ModelAdmin):
    fields = ['name']

class YearAdmin(admin.ModelAdmin):
    fields = ['name']
    
class CollegeCourseInline(admin.TabularInline):
    model = CollegeCourse
    extra = 0

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'institute_type', 'district', 'website')
    inlines = [CollegeCourseInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(InstituteType, InstituteTypeAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(College, CollegeAdmin)
