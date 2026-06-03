from django.contrib import admin
from .models import Publication

#admin.site.register(Publication)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = ["title","user","created_at","updated_at"]

 
