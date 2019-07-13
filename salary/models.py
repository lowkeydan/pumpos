from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Work(models.Model):
    work_detail = models.CharField(max_length=30)
    unit_price = models.FloatField()

    def __str__(self):
        return self.work_detail


class Salary(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    work_detail = models.ForeignKey(Work, on_delete=models.CASCADE)
    date_recorded = models.DateTimeField(auto_now=True)
    unit = models.IntegerField(default=0)
    salary_today = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.person)
