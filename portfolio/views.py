# coding: utf-8
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import os
import json
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import *

try:
    data = {
        "experiences": [exp for exp in Experience.objects.all()],
        "educations": [education for education in Education.objects.all()],
        "skills": [skill for skill in Skills.objects.all()],
        "projects": [project for project in PersonalProject.objects.all()],
        "form_contact": ContactForm()

    }
except:
    data = {}


def home(request):
    return render(request, 'portefolio.html', data)


def send_mail_to_me(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject=subject,
                          message=message,
                          from_email=from_email,
                          recipient_list=['sadour.mehdi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'portefolio.html', data)
    return render(request, "portefolio.html", data)


def go_connexion(request, error=False):
    data['error'] = error
    form_connexion = ConnexionForm()
    data['form_connexion'] = form_connexion
    return render(request, 'connexion.html', data)


def authentification(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                return go_connexion(request, True)
    else:
        form = ConnexionForm()

    redirect('/cv/home')
    return home(request)


def decode_data(string):
    string = string\
        .replace('Ã©', 'é')\
        .replace('Ã¨', 'è')\
        .replace('â€™', '\'')\
        .replace('Â«', '«')\
        .replace('Â»', '»')\
        .replace('Ã', 'à')\
        .replace('àª', 'ê')\
        .replace('à´', 'ô')\
        .replace('à‰', 'É')

    return string


def load_database(request):
    #Delete all database records
    User.objects.all().delete()
    Task.objects.all().delete()
    Technology.objects.all().delete()
    Experience.objects.all().delete()
    Skills.objects.all().delete()
    Education.objects.all().delete()
    PersonalProject.objects.all().delete()

    current_directory = os.path.dirname(os.path.realpath(__file__))
    path_json_file = current_directory + "\\load_data.json"
    my_dict = json.load(open(path_json_file))
    for classe, datas in my_dict.items():
        if classe == 'PersonalProject':
            for data in datas:
                obj = PersonalProject(
                    name = decode_data(data['name']),
                    description = decode_data(data['description']),
                    github = data['github'],
                    link = data['link'],
                    period = data['period'],
                    num_project=data['num_project'])
                obj.save()

                for technologies_data in data['technologies']:
                    obj_techno = Technology(name=decode_data(technologies_data["name"]), is_main=technologies_data["is_main"])
                    obj_techno.save()
                    obj.technologies.add(obj_techno)
                obj.save()

        elif classe == 'Experience':
            for data in datas:
                obj = Experience(
                    company = data['company'],
                    job = decode_data(data['job']),
                    place = decode_data(data['place']),
                    description_mission = decode_data(data['description_mission']),
                    description_company = decode_data(data['description_company']),
                    type_experience = data['type_experience'],
                    date_begin = data['date_begin'],
                    date_end = data['date_end']
                )
                obj.save()

                for tasks_data in data['tasks']:
                    obj_task = Task(name=decode_data(tasks_data["name"]))
                    obj_task.save()
                    obj.tasks.add(obj_task)

                for technologies_data in data['technologies']:
                    obj_techno = Technology(name=decode_data(technologies_data["name"]), is_main=technologies_data["is_main"])
                    obj_techno.save()
                    obj.technologies.add(obj_techno)
                obj.save()

        elif classe == 'User':
            for data in datas:
                user = User.objects.create_user(
                    username = data["username"],
                    first_name = data["first_name"],
                    last_name = data["last_name"],
                    email = data["email"],
                    password = data["password"],
                    is_staff = data["is_staff"]
                )
                user.save()
        elif classe == 'Skills':
            for data in datas:
                obj = Skills(
                    name = decode_data(data["name"]),
                    level = data["level"]
                )
                obj.save()

        elif classe == 'Education':
            for data in datas:
                obj = Education(
                    name = decode_data(data["name"]),
                    option = decode_data(data["option"]),
                    school = decode_data(data["school"]),
                    year = data["year"],
                    place = decode_data(data["place"]),
                    description = decode_data(data["description"])
                )
                obj.save()
    return home(request)
    # return render(request, 'portefolio.html')
