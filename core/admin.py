from django.contrib import admin

from .models import ErrorLog, PhraseValues, Phrase

# Register your models here.
admin.site.register(ErrorLog)
admin.site.register(PhraseValues)
admin.site.register(Phrase)
