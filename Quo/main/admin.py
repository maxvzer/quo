# coding: utf-8
"""
    project: main
    module created: 16.03.2016

    Constants, that are used in the project
"""

from django.contrib import admin

from .models import Person, MilitaryCommissariat, Grade, DegreeOfFitness,  \
                    Faculty,  Group, Department, OKSO, Year, VUS


class PersonAdmin(admin.ModelAdmin):
    list_display=['name', 'get_military']
    search_fields = ('middle_name',)
    list_filter = ('is_learning', 'grade', 'military')

    def get_military(self, obj):
        return obj.military.get_title_display()

    def name(self, obj):
        return obj.middle_name + " " + obj.first_name

admin.site.register(Grade)
admin.site.register(DegreeOfFitness)
admin.site.register(OKSO)
admin.site.register(MilitaryCommissariat)
admin.site.register(Person, PersonAdmin)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(VUS)
admin.site.register(Year)
