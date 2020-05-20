from django.db import models


class Сurriculum(models.Model):
    name = models.CharField(max_length=64)


    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128, null=True)
    curriculums = models.ManyToManyField(
        to=Сurriculum,
        related_name='courses',
    )

    def __str__(self):
        return f'{self.title} - {self.description}'


    # @classmethod
    # def generate_classroom(cls):
    #
    #     classroom = cls(
    #         name=f'Classroom - {random.choice(range(5))}',
    #     )
    #
    #     classroom.save()
