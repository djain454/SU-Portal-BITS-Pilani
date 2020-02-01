from django.contrib import admin
from su.models import Coord, Student, Wear, Event, Wear_Student, Event_Student, DateMailStatus, Wear_Invalid_Students,Event_Invalid_Students

admin.site.register(Coord)
admin.site.register(Wear)
admin.site.register(Event)
admin.site.register(DateMailStatus)

class ItemStudentAdmin(admin.ModelAdmin):
    search_fields = ('student_id',)
admin.site.register(Wear_Student,ItemStudentAdmin)
admin.site.register(Event_Student,ItemStudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('bits_id',)
admin.site.register(Student,StudentAdmin)

class Wear_Invalid_StudentsAdmin(admin.ModelAdmin):
    search_fields = ('student_id',)
admin.site.register(Wear_Invalid_Students,Wear_Invalid_StudentsAdmin)

class Event_Invalid_StudentsAdmin(admin.ModelAdmin):
    search_fields = ('student_id',)
admin.site.register(Event_Invalid_Students,Event_Invalid_StudentsAdmin)
