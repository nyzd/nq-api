from django.contrib import admin

from .models import Request, PhraseValues, Phrase

# Register your models here.
admin.site.register(Request)
admin.site.register(PhraseValues)
admin.site.register(Phrase)
