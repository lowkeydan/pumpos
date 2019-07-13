from django.contrib import admin
from .models import Person, Work, Salary
# Register your models here.
admin.site.register(Person)
admin.site.register(Work)
admin.site.register(Salary)