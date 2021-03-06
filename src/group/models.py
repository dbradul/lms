import random

from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - Floor# {self.floor}'

    @classmethod
    def generate_classroom(cls):

        classroom = cls(
            name=f'Classroom - {random.choice(range(5))}',
            floor=random.choice(range(5))
        )

        classroom.save()


class Group(models.Model):
    name = models.CharField(max_length=64)
    course = models.CharField(max_length=128)
    classroom = models.ManyToManyField(
        to=Classroom,
        null=True,
        related_name='groups'
    )

    def __str__(self):
        return f'{self.name} - {self.course}'

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
