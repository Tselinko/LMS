from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import AddHomeworkForm, MaterialForm, HomeworkForm
from .models import Courses, Materials, Homeworks, StudentsHomeworks
from django.db.models import Q


def courses_home(request):
    courses = Courses.objects.order_by('title')[:25]
    return render(request, 'courses/courses_home.html', {'courses': courses})


class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'courses/course.html'
    context_object_name = 'course'


class CourseMaterialView(DetailView):
    model = Courses
    template_name = 'courses/material_home.html'
    context_object_name = 'course_materials'


class CourseHomeworkView(DetailView):
    model = Courses
    template_name = 'courses/homework_home.html'
    context_object_name = 'course_homeworks'


class MaterialView(DetailView):
    model = Materials
    template_name = 'courses/material.html'
    context_object_name = 'material'


class HomeworkView(DetailView):
    model = Homeworks
    template_name = 'courses/homework.html'
    context_object_name = 'homework'
    ordering = ['date_of_beggining']


class AddHomeworkView(CreateView):
    model = StudentsHomeworks
    form_class = AddHomeworkForm
    template_name = 'courses/add_homework.html'
    context_object_name = 'adding_homework'

    def form_valid(self, form):
        variable = StudentsHomeworks.objects.filter(Q(author_id=self.request.user.id)).filter(Q(homework_id=self.kwargs['pk']))
        variable.delete()
        form.instance.homework_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homeworks-detail', args=(self.object.homework.id,))


class MaterialCreateView(CreateView):
    model = Materials
    form_class = MaterialForm
    template_name = 'courses/create_update_material.html'
    context_object_name = 'material'

    def form_valid(self, form):
        form.instance.course_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course_material_home', args=(self.object.course.id,))


class MaterialUpdateView(UpdateView):
    model = Materials
    form_class = MaterialForm
    template_name = 'courses/create_update_material.html'
    context_object_name = 'material'

    def get_success_url(self):
        return reverse('course_material_home', args=(self.object.course.id,))


class MaterialDeleteView(DeleteView):
    model = Materials
    template_name = 'courses/delete_material.html'
    context_object_name = 'material'

    def get_success_url(self):
        return reverse('course_material_home', args=(self.object.course.id,))


class HomeworkCreateView(CreateView):
    model = Homeworks
    form_class = HomeworkForm
    template_name = 'courses/create_update_homework.html'
    context_object_name = 'homework_create'

    def form_valid(self, form):
        form.instance.course_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course_homework_home', args=(self.object.course.id,))


class HomeworkUpdateView(UpdateView):
    model = Homeworks
    form_class = HomeworkForm
    template_name = 'courses/create_update_homework.html'
    context_object_name = 'homework'

    def get_success_url(self):
        return reverse('course_homework_home', args=(self.object.course.id,))


class HomeworkDeleteView(DeleteView):
    model = Homeworks
    template_name = 'courses/delete_homework.html'
    context_object_name = 'homework'

    def get_success_url(self):
        return reverse('course_homework_home', args=(self.object.course.id,))
