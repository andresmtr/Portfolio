# This documents is nwe, import all librerias and documents here

#Imports
from django.urls import path
from BasePortfolio import views
from .views import Beginning, ProjectDetail, TutorialDetail, AboutMe
from django.conf.urls import url 


#Import URL
urlpatterns = [

    path('',Beginning.index, name = 'index'),
    #path('<slug:slug>/',ProjectDetail.as_view(), name = 'project'),
    path('projects/',ProjectDetail.projects, name = 'project'),
    path('tutorials/',TutorialDetail.tutorials, name = 'tutorial'),
    path('about/',AboutMe.about, name = 'about'),
        
]
