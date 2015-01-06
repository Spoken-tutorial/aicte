from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from institute.forms import *
from django.forms.models import inlineformset_factory

# Create your views here.

def home(request):
    form = CollegeForm()
    CollegeCourseInlineFormSet = inlineformset_factory(College, CollegeCourse)
    inlineform = CollegeCourseInlineFormSet
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        inlineform = CollegeCourseInlineFormSet(request.POST)
        if form.is_valid():
            if inlineform.is_valid():
                college = form.save()
                inlineform = CollegeCourseInlineFormSet(request.POST, instance=college)
                if inlineform.is_valid():
                    inlineform.save()
    context = {}
    context['form'] = form
    context['inlineform'] = inlineform
    return render(request, 'home.html', context)
