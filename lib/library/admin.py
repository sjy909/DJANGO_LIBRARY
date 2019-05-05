from django.contrib import admin
from .models import Book, Student, History, Pic, Message
# Register your models here.

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(History)
admin.site.register(Pic)
admin.site.register(Message)
