from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
POSITION_CHOICES = (
    ('SL', 'SELECT'),
    ('JD', 'Junior Developer'),
    ('SD', 'Senior Developer'),
    ('DE', 'Devops Engineer'),
    ('TE', 'TEST Engineer'),
    ('PM', 'PROJECT Manager'),
)

class Position(models.Model):
    title = models.CharField(choices=POSITION_CHOICES, max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emp_no = models.PositiveIntegerField()
    mobile = models.CharField(max_length=15)
    place = models.CharField(max_length=128)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)