from django.views.generic import DetailView
from .models import StudyGroups
from django.shortcuts import render


class StudyGroupView(DetailView):
    model = StudyGroups
    context_object_name = "study_group"
    template_name = 'groups/group-info.html'
