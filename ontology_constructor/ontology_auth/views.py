from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OntologyForm, SubjectForm, ObjectForm, rdf_typeForm, UserRegForm
from .models import Ontology, Subject, Object, rdf_type
import os
from django.contrib.auth import authenticate, login , logout



def index(request):
    template  = render_to_string("ontology_auth/index.html")
    return HttpResponse(template)

def test_menu(request):
    template  = render_to_string("ontology_auth/menu.html")
    print(request)
    return HttpResponse(template)


def auth(request):
    # print(request.user)
    # print(request)
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return(redirect("profile"))
    return render(request,"ontology_auth/auth.html")
   

def profile(request):
    print(request.user)
    template  = render_to_string("ontology_auth/profile.html")
    return render(request,"ontology_auth/profile.html", {'user': request.user})

def constructor(request):
    template  = render_to_string("ontology_auth/constructor.html")
    return HttpResponse(template)

def ontology_list_1(request, ontology_id=None):
    ontologys= Ontology.objects.all()
    context= {'ontologys': ontologys}
    if (request.GET.get('delete_ontology')):
        Ontology.objects.filter(id = request.GET.get('delete_ontology')).delete()
        return redirect('/ontology/list')
    return render(request, "ontology_auth/ontology_list.html", context)

def delete_ontology(request, ontology_id=None):
    object = Ontology.objects.get(id=ontology_id)
    object.delete()
    return redirect('/ontology/list')
    

def ontology_detail(request, ontology_id):
    ontology_cur= get_object_or_404(Ontology, id=ontology_id)
    rdf_types=rdf_type.objects.filter(ontology=ontology_cur)
    context= {'rdf_types': rdf_types, 'ontology': ontology_cur}
    return render(request, "ontology_auth/ontology_detail.html", context)
   
def add_ontology(request):
    if request.method == 'POST':
        form = OntologyForm(request.POST)
        if form.is_valid():
            form.save('ontology')
            form=OntologyForm()
            return redirect('/ontology/list')
    else:
        form=OntologyForm()
        return render(request, 'ontology_auth/add_ontology.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form_sub = SubjectForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('subject')
            form_sub = SubjectForm()
            return redirect('/ontology/list')
    else:
        form_sub=SubjectForm()
        return render(request, 'ontology_auth/add_subject.html', {'form': form_sub})

def add_object(request):
    if request.method == 'POST':
        form_sub = ObjectForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('object')
            form_sub = ObjectForm()
            return redirect('/ontology/list')
    else:
        form_sub=ObjectForm()
        return render(request, 'ontology_auth/add_object.html', {'form': form_sub})
    
def add_rdf_type(request):
    if request.method == 'POST':
        form_sub = rdf_typeForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('rdf_type')
            form_sub = rdf_typeForm()
            return redirect('/ontology/list')
    else:
        form_sub=rdf_typeForm()
        return render(request, 'ontology_auth/add_rdf_type.html', {'form': form_sub})




# Добавить сообщение о успещной регристрации ползователя.
def register(request):
    if request.method == 'POST':
        form_m = UserRegForm(request.POST)
        if form_m.is_valid():
            form_m.save('registration')
            username = form_m.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('profile')
        else:
            messages.success(request, f'Создан аккаунт {username}!')
    else:
        form_m = UserRegForm()
        return render(request, 'ontology_auth/register.html', {'form': form_m})


def logout_func(request):
    logout(request)
    return redirect("auth")

# @login_required
# def profile(request):
#     return render(request, 'ontology_auth/profile.html')