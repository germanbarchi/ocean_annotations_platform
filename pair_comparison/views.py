from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from pair_comparison.form import AnnotationForm
from pair_comparison.models import Annotation, Audio
from IPython import embed
import datetime

class AnnotationView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    form_class = AnnotationForm
    template_name = 'pair_comparison/pair_annotation.html'
    success_url = '/pair_comparison/ann/form'

    def get_object(self, queryset=None):
        order = self.kwargs.get('order')
        anns = Annotation.objects.filter(user=self.request.user).exclude(submit=True)
        incomplete = anns.filter(submit=False).order_by('order')
        if order:
            return anns.get(order=order)
        if incomplete.exists():
            return incomplete.first()
        else:
            return anns.filter(submit=False).order_by('order').first()

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super(AnnotationView, self).get_context_data(**kwargs)
        context['audio_A'] = self.object.audio_A.audiofile.url
        context['audio_B'] = self.object.audio_B.audiofile.url
        context['order'] = self.object.order
        status = [str(a.submit) for a in Annotation.objects.order_by('order').all()]
        context['status'] = ','.join(status)
        context['total'] = Annotation.objects.filter(user=self.request.user).count()
        #context['mod_time']=datetime.datetime.now()
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        ann = Annotation.objects.filter(user=request.user).exclude(submit=True)
        if ann:
            return super(AnnotationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('pair_comparison:end'))

    def form_invalid(self, form):
        return super(AnnotationView, self).form_invalid(form)  

    def form_valid(self, form):
        print('valid')
        self.object.submit = True
        return super(AnnotationView, self).form_valid(form)
    
    
    
    
def end(request):
    logout(request)
    return render(request, 'pair_comparison/end.html', {})