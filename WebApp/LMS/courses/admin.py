from django.contrib import admin
from .models import Courses, Materials, Homeworks, StudentsHomeworks

admin.site.register(Courses)
admin.site.register(Materials)
admin.site.register(Homeworks)
admin.site.register(StudentsHomeworks)
