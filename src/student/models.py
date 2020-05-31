import datetime
import random

from django.db import models

# Create your models here.
from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True, db_index=True)
    birthdate = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # return str(self.__dict__)
        return f'{self.first_name},' \
               f'{self.last_name},' \
               f'{self.email},' \
               f'{self.birthdate}'

    @classmethod
    def generate_student(cls, groups=None):
        faker = Faker()

        if groups is None:
            groups = list(Group.objects.all())

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            group=random.choice(groups)
        )

        student.save()


    def save(self):
        # ...
        super().save()
        # ...