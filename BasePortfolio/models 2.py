from django.db import models

#Imports

# Create your models here.

# Principal models
class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    date_creaction = models.DateField('Date of Creation', auto_now=False ,auto_now_add=True)
    date_modify = models.DateField('Date of Modify', auto_now=True, auto_now_add=False)
    date_delete = models.DateField('Date of Delete', auto_now=True, auto_now_add=False)

    class  Meta:
        abstract = True


# Author

class Author(ModeloBase):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=120)
    email = models.EmailField('email', max_length=200, unique = True) 
    description = models.TextField('Description')
    imagen = models.ImageField('Image', null=True, blank=True, upload_to= 'authors/')
    github = models.URLField('Github', null=True, blank=True)
    linkedin = models.URLField('Linkedin', null=True, blank=True)

    class  Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

# languages

class language(ModeloBase):
    acronym = models.CharField('Acronym', max_length=10, unique=True)
    name = models.CharField('Name', max_length=150, unique=True)

    class  Meta:
        verbose_name = 'language'
        verbose_name_plural = 'languages'


# Projects
class Project(ModeloBase):
    title = models.CharField('Title', max_length=150, unique=True)
    slug = models.SlugField('Slug', max_length=150, unique=True)
    description = models.TextField('description')
    information = models.TextField('information',null=True, blank=True)
    GitLink = models.URLField('Github repository',null=True, blank=True)
    YoutubeLink = models.URLField('Youtube',null=True, blank=True)
    LinkWeb = models.URLField('Link Web',null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='projects/', max_length=255)
    date_creaction_project = models.DateField('Date of Creation', blank=True, null=True)

    class  Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

# Tutorials
class Tutorial(ModeloBase):
    title = models.CharField('Title', max_length=150, unique=True)
    slugT = models.SlugField('Slug', max_length=150, unique=True)
    description = models.TextField('description')
    information = models.TextField('information',null=True, blank=True)
    GitLink = models.URLField('Github repository',null=True, blank=True)
    YoutubeLink = models.URLField('Youtube',null=True, blank=True)
    LinkWeb = models.URLField('Link Web',null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='tutorials/', max_length=255, null=True)
    date_creaction_tutorial = models.DateField('Date of Creation',blank=True, null=True)

    class  Meta:
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutorials'

# Tutorials
class pdf(ModeloBase):
    titlepdf = models.CharField('Title pdf', max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=150, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    namePdf = models.FileField('Pdf', upload_to='documents/')
    date_updatePdf = models.DateField('Date of Creation',blank=True, null=True)

    class  Meta:
        verbose_name = 'pdf'
        verbose_name_plural = 'pdfs'

# works

class jobs (ModeloBase):

    titleCompany = models.CharField('Title', max_length=150)
    slug = models.SlugField('Slug', max_length=150, unique=True)
    titleJob = models.CharField('TitleJob', max_length=150)
    descriptionJob =  models.TextField('description')
    beginJob = models.CharField('BeginJob', max_length=150)
    endJob = models.CharField('EndJob', max_length=150)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    date_creaction_job = models.DateField('Date of Creation',blank=True, null=True)

    class  Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

# Educations

class educations (ModeloBase):
    
    nameCollege = models.CharField('Name College', max_length=150)
    slug = models.SlugField('Slug', max_length=150, unique=True)
    titleEducations = models.CharField('Title Education', max_length=150)
    beginEducation = models.CharField('Begin Education', max_length=150)
    endEducation = models.CharField('End Education', max_length=150)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    date_creaction_education = models.DateField('Date of Creation',blank=True, null=True)

    class  Meta:
        verbose_name = 'education'
        verbose_name_plural = 'educations'

# institutions certificattions

class institutionsCertifications(ModeloBase):

    nameInstitute = models.CharField('Name Institute', max_length=150, unique=True)
    imageInstitute = models.ImageField('Image institute', upload_to='institute/', max_length=255, null=True)

    class  Meta:
        verbose_name = 'institute'
        verbose_name_plural = 'institutions'


class certification(ModeloBase):

    titleCertification = models.CharField('Title Certifications', max_length=150)
    institute = models.ForeignKey(institutionsCertifications, on_delete=models.CASCADE)
    LinkCertification = models.URLField('Link Certifications',null=True, blank=True)


    class  Meta:
        verbose_name = 'certification'
        verbose_name_plural = 'certifications'