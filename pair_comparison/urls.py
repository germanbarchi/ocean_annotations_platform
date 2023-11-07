from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from pair_comparison.views import AnnotationView, end, audio_check
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'instructions',
         login_required(TemplateView.as_view(template_name='pair_comparison/instructions.html'), login_url='/'),
         name='instructions'),
    path(r'instructions_recording', audio_check, name='instructions_recording'),
    path(r'form', AnnotationView.as_view(), name='form'),
    path(r'form/<int:order>', AnnotationView.as_view(), name='form'),
    path(r'end', end, name='end'),
]