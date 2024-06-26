from django import forms
from django.forms import ModelForm
from .models import Object, Subject ,rdf_type, Ontology
from django.contrib.auth.models import User

class OntologyForm(ModelForm):
    class Meta:
        model = Ontology
        fields = ['name', 'access']
    def __init__(self, *args, **kwargs):
        super(OntologyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['access'].widget.attrs.update({"length": "40", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['description'].widget.attrs.update({"size": "80", "width": "40", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")
        
class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ['name', 'description']
    def __init__(self, *args, **kwargs):
        super(ObjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['description'].widget.attrs.update({"size": "80", "width": "40", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")
        
class rdf_typeForm(ModelForm):
    class Meta:
        model = rdf_type
        fields = ['name', 'description', 'object', 'subject', 'ontology']
    def __init__(self, *args, **kwargs):
        super(rdf_typeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['description'].widget.attrs.update({"size": "200", "width": "80", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")




from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None




# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']