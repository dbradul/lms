import datetime
import random

from django.db import models

from course.models import Course


class Classroom(models.Model):
    name = models.CharField(null=True, max_length=64)
    floor = models.SmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name} - Floor #{self.floor}'


class Group(models.Model):
    name = models.CharField(max_length=64)
    # course = models.CharField(max_length=128)
    course_a = models.ForeignKey(
        to=Course,
        null=True,
        on_delete=models.SET_NULL,
        related_name='groups'
    )

    classroom = models.ManyToManyField(
        to=Classroom,
        null=True,
        related_name='groups'
    )

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def generate_group(cls):

        group = cls(
            name=f'Group - {random.choice(range(5))}',
            course=random.choice([
                "IT 210: Web Application Development.",
                "IT 226: Enterprise Information Systems.",
                "IT 227: E-Commerce Technologies.",
                "IT 238: Networking and Client/Server Computing.",
                "IT 280: Internet Security.",
                "IT 295: IT-Based Application Project.",
                "IT 299: Graduate Seminar.",
            ])
        )

        group.save()
