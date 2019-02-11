from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home', views.home),
    path('', views.home),
    #authentification
    path('go_connexion', views.go_connexion),
    path('authentification', views.authentification),

    #contact
    path('send_mail_to_me', views.send_mail_to_me, name='send_mail_to_me'),

    #database
    path('load_database', views.load_database)
]