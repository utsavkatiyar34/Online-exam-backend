from django.contrib import admin
from .models import Course,Test,Question,Assigned
# Register your models here.
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Assigned)