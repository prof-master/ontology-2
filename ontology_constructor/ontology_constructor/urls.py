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
from ontology_auth.views import index,auth,profile, constructor, add_ontology, ontology_list_1, register,ontology_detail, add_subject, add_object, add_rdf_type, login,logout_func, update_ontology, object_update, subject_detail, subject_update, rdf_type_detail, rdf_type_update
from ontology_auth.views import index,auth,profile, test_menu, constructor, add_ontology, ontology_list_1, register,ontology_detail, add_subject, add_object, add_rdf_type, login,logout_func, update_ontology, object_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('auth/',auth,name='auth'),
    path('logout/',logout_func,name='logout'),
    path('register/',register,name='register'),
    path('menu/',test_menu,name='menu'),

    path('profile/',profile,name='profile'),
    path('constructor/',constructor,name='constructor'),
    path('ontology/list/',ontology_list_1,name='ontology_list_1'),
    path('ontology/<int:ontology_id>/',ontology_detail,name='ontology_detail'),
    path('object/<int:object_id>/',object_detail,name='object_detail'),
    path('object/<int:object_id>/update',object_update,name='object_update'),
    path('subject/<int:subject_id>/',subject_detail,name='subject_detail'),
    path('subject/<int:subject_id>/update',subject_update,name='subject_update'),
    path('rdf_type/<int:rdf_type_id>/',rdf_type_detail,name='rdf_type_detail'),
    path('rdf_type/<int:rdf_type_id>/update',rdf_type_update,name='rdf_type_update'),
    path('ontology/new/', add_ontology, name='add_ontology'),
    path('ontology/new/subject/', add_subject, name='add_subject'),
    path('ontology/new/object/', add_object, name='add_object'),
    path('ontology/new/predicat/', add_rdf_type, name='add_rdf_type'),
    path('ontology/<int:ontology_id>/update', update_ontology, name='update_ontology'),

        
]
