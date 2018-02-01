# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class House(Base):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class StudentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Get a real name, one with more than 1 character"
        if len(postData['email']) < 8:
            errors["email"] = "Email more than 8 characters"
        if len(postData['password']) < 6:
            errors["password"] = "password too short"
        if postData['password'] != postData["password"]:
            errors["confirm_pw"] = "confirm does not match"
        # if len(self.filter(email=post_data['email'])) > 0:
        #     errors['one_email'] = "you're email is not unique"
        return errors


class Student(Base):
    name = models.CharField(max_length=254)
    cult = models.ForeignKey(House, related_name="peeps")
    #wand = models.OneToOneField(Wand)

    def __str__(self):
        return self.name

    objects = StudentManager()


def build_houses():
    houses = ["Thunderbird", "Wampus", "Horned Serpent", "Pukwudgie"]
    for house in houses:
        neo = House(name=house)
        neo.save()



def build_students():
    names = [
        "Alan",
        "Brian",
        "Bernardo",
        "Robb",
        "Mags",
        "Manjula",
        "Rachel",
        "Scott",
        "Tyler",
        "Bob",
        "Ross",
        "Bobbert",
        "ROss",
        "Rob",
        "Boss",
        "Tim",
        "Noelle",
        "Graham",
        "Donovan",
    ]
    houses = House.objects.all()
    for n in names:
        neo = Student(name=n)
        h = houses[random.randint(0, 3)]
        neo.cult = h
        neo.save()


    print "You tried to create a student"
    
# def studentShazam():
#     peep = request.POST['name']
#     bob = Student(name=peep)
#     bob.cult = House.objects.all()[random.randint(0,3)]
#     bob.save()
#     request.session['peep'] = peep
#     students = Student.objects.all()



class Course(Base):
    title = models.CharField(max_length=255)
    description = models.TextField(default="A Class")
    members = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

# def build_courses():
# courses = ["Potions", "Curses", "Hexes", "Spells"]
# for course in courses:
#     neo = Course(name=course)
#     neo.save()
