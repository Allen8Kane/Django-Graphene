from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=10)
    job_name = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.group_name} ( id={self.job_name} )'

class Student(models.Model):
    name = models.CharField(max_length=25)
    gpa = models.DecimalField(decimal_places=2, max_digits=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ( id={self.id} )'

