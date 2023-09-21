from django.contrib import admin
from pair_comparison.models import Annotation, Audio


class AudioAdmin(admin.ModelAdmin):
    list_display = ['name']


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ['user', 'audio_A','audio_B', 'order', 'submit']



admin.site.register(Audio, AudioAdmin)
admin.site.register(Annotation, AnnotationAdmin)

