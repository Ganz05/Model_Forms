from django.contrib import admin
from app.models import *

# Register your models here.


class CustomizeSchool(admin.ModelAdmin):
    list_display=['sname','sloc','sprincipal']
    list_editable=['sprincipal']
    list_filter=['sname']

admin.site.register(School,CustomizeSchool)

class CustomizeBranch(admin.ModelAdmin):
    list_display=['sname','bname','subject']
    list_display_links=['bname']
    list_filter=['bname']
    list_editable=['subject']
    list_per_page=2

admin.site.register(Branch,CustomizeBranch)

class CustomizeStudent(admin.ModelAdmin):
    list_display=['sname','bname','student_name','DOB']
    list_display_links=['student_name']
    list_filter=['student_name']
    list_per_page=2
    

admin.site.register(Student,CustomizeStudent)


