"""
URL configuration for ontology_constructor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from ontology_auth.views import index,auth,profile, constructor, add_ontology, ontology_list_1, register,ontology_detail, add_subject, add_object, add_rdf_type, delete_ontology,login,logout_func, update_ontology
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('auth/',auth,name='auth'),
    path('logout/',logout_func,name='logout'),
    path('register/',register,name='register'),



    path('profile/',profile,name='profile'),
    path('constructor/',constructor,name='constructor'),
    path('ontology/list/',ontology_list_1,name='ontology_list_1'),
    path('ontology/<int:ontology_id>/',ontology_detail,name='ontology_detail'),
    path('ontology/new/', add_ontology, name='add_ontology'),
    path('ontology/new/subject/', add_subject, name='add_subject'),
    path('ontology/new/object/', add_object, name='add_object'),
    path('ontology/new/predicat/', add_rdf_type, name='add_rdf_type'),
    path('delete_ontology/<int:ontology_id>', delete_ontology, name='delete_ontology'),
    path('update_ontology/<int:ontology_id>', update_ontology, name='update_ontology'),
    # path('accounts/', include('django.contrib.auth.urls')),
        
]
