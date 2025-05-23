"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#New imports
from django.conf.urls import include
# Import for render image
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    #Url internacionalización
    path('i18n/', include('django.conf.urls.i18n')),

    # link about all url of BasePortfolio
    path('', include(('BasePortfolio.urls', 'BasePortfolio'))),
]


# Use to render the image

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',serve, {
            'document_root':settings.MEDIA_ROOT,
        })
    ]
