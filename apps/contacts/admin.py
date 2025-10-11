from django.contrib import admin

from apps.contacts.models import Subject, Contact


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass