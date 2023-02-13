from django.contrib import admin
from . models import Topic, Subtopic, Comments

# Register your models here.
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Comments)