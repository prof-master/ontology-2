from django.contrib import admin
from .models import Object, Subject ,rdf_type,Post
# Register your models here.



@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject)
admin.site.register(rdf_type)
admin.site.register(Post)

# Register your models here.

