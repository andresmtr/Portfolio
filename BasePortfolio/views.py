from django.shortcuts import render


#New imports
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.utils.translation import gettext as _
from .models import Author,language,Project,Tutorial, pdf, jobs, educations, institutionsCertifications, certification
from django.views.generic import ListView, View, DetailView

# Create your views here.


class Beginning():

    def index(request):

        ######### Get all projects for language
        english = Project.objects.filter(language_id = 1).order_by('-date_creaction_project')
        spanish = Project.objects.filter(language_id = 2).order_by('-date_creaction_project')
        french = Project.objects.filter(language_id = 3).order_by('-date_creaction_project')

        ######## Author
        author = Author.objects.filter(state = True).latest('date_creaction')

        ######## pdf
        
        english_pdf = pdf.objects.filter(language_id = 1)
        spanish_pdf = pdf.objects.filter(language_id = 2)
        french_pdf = pdf.objects.filter(language_id = 3)

        ######## Tutorials

        TuEnglish = Tutorial.objects.filter(language_id = 1).order_by('-date_creaction_tutorial')
        TuSpanish = Tutorial.objects.filter(language_id = 2).order_by('-date_creaction_tutorial')
        TuFrench = Tutorial.objects.filter(language_id = 3).order_by('-date_creaction_tutorial')

        context = { 
            # Projects            
            'english':english,
            'spanish': spanish,
            'french':french,

            #Author
            'author':author,

            #pdf
            'english_pdf':english_pdf,
            'spanish_pdf':spanish_pdf,
            'french_pdf':french_pdf,

            # Tutorials
            'TuEnglish':TuEnglish,
            'TuSpanish':TuSpanish,
            'TuFrench':TuFrench,
        }

        return render(request, 'base.html', context)  # 4


# class ProjectDetail(DetailView):
#     def get(self,request,slug,*args,**kwargs):

#         pj = Project.objects.get(slug = slug)

#         context = {
#             'pj':pj,
#         }

#         return render(request,'project.html',context)

class ProjectDetail(DetailView):
    def projects(request):

        #pj = Project.objects.get(slug = slug)
        ######### Get all projects for language
        english = Project.objects.filter(language_id = 1).order_by('-date_creaction_project')
        spanish = Project.objects.filter(language_id = 2).order_by('-date_creaction_project')
        french = Project.objects.filter(language_id = 3).order_by('-date_creaction_project')

        context = {
            #'pj':pj,
            'english':english,
            'spanish':spanish,
            'french':french,

        }
        return render(request,'project.html',context)

class TutorialDetail(DetailView):
    def tutorials(request):

        #pj = Project.objects.get(slug = slug)
        ######### Get all projects for language
        english = Tutorial.objects.filter(language_id = 1).order_by('-date_creaction_tutorial')
        spanish = Tutorial.objects.filter(language_id = 2).order_by('-date_creaction_tutorial')
        french = Tutorial.objects.filter(language_id = 3).order_by('-date_creaction_tutorial')
        
        context = {
            #'pj':pj,
            'english':english,
            'spanish':spanish,
            'french':french,

        }
        return render(request,'tutorial.html',context)

class AboutMe(DetailView):
    def about(request):

        # Jobs
        english = jobs.objects.filter(language_id = 1).order_by('-date_creaction_job')
        spanish = jobs.objects.filter(language_id = 2).order_by('-date_creaction_job')
        french = jobs.objects.filter(language_id = 3).order_by('-date_creaction_job')

        # Educations
        EduEnglish = educations.objects.filter(language_id = 1).order_by('-date_creaction_education')
        EduEpanish = educations.objects.filter(language_id = 2).order_by('-date_creaction_education')
        EduFrench = educations.objects.filter(language_id = 3).order_by('-date_creaction_education')

        # Certifications
        certificate = certification.objects.all().order_by('-id')

        context = {
            # jobs
            'english':english,
            'spanish':spanish,
            'french':french,

            # Education
            'EduEnglish':EduEnglish,
            'EduEpanish':EduEpanish,
            'EduFrench':EduFrench,

            #certificate
            'certificate':certificate,



        }
        return render(request,'about.html',context)



####### Tutoriales
# class listTutorials(DetailView):

#     def get(self,request,*args,**kwargs):

#         # listar proyectos
#         ListarProyectos = Tutorial.objects.get_queryset().order_by('id')

#         context = {
#             'ListarProyectos':ListarProyectos,
#         }

#         return render(request,'tutorialAll.html',context)

# class TutorialDetail(DetailView):
#     def callTutorial(self,request,slug,*args,**kwargs):

#         Tut = Tutorial.objects.get(slugT = slug)

#         context = {
#             'Tut':Tut,
#         }

#         return render(request,'tutorial.html',context)






