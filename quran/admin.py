from django.contrib import admin
from .models import (
    RasmOlMushaf,
    Surah,
    Ayah,
    AyahTranslation,
    Translation,
    Word,
    WordBreaker,
    AyahBreaker,
    Transmission,
)

# Register your models here.
admin.site.register(RasmOlMushaf)
admin.site.register(Transmission)
admin.site.register(Surah)
admin.site.register(Ayah)
admin.site.register(AyahTranslation)
admin.site.register(Translation)
admin.site.register(Word)
admin.site.register(WordBreaker)
admin.site.register(AyahBreaker)
