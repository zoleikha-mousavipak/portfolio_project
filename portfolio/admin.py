from django.contrib import admin
from .models import Experience, Education, Skills, PersonalProject, Task, Technology

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(PersonalProject)
admin.site.register(Task)
admin.site.register(Technology)