from django.db import models
import datetime
import django.utils.timezone as tz


class Technology(models.Model):
    name = models.CharField(max_length=100)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description_mission = models.TextField()
    description_company = models.TextField()
    type_experience = models.CharField(max_length=100)
    date_begin = models.DateField()
    date_end = models.DateField()
    technologies = models.ManyToManyField(Technology)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.job + " - " + self.company


class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    option = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class PersonalProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    period = models.DateField(default=tz.now())
    technologies = models.ManyToManyField(Technology)
    num_project = models.IntegerField()

    def __str__(self):
        return self.name
    #img = models.CharField(max_length=100, default='')
