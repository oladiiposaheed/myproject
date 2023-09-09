from django.contrib import admin
from testapp.models import StudentInfo3
# Register your models here.
class StudentInfoAdmin3(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'gender', 'math', 'chem', 'phy', 'td', 'bio', 'eng']

admin.site.register(StudentInfo3, StudentInfoAdmin3)
