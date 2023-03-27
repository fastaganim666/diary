from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .filters import TaskFilter


class MainPurpose(ListView):
    model = TaskDay
    paginate_by = 10
    template_name = 'planner/main.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TaskFilter(self.request.GET, queryset.filter(user=self.request.user.id))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['filterset'] = self.filterset
        return context


class DatePurpose(ListView):
    model = TaskDay
    paginate_by = 10
    ordering = 'date'
    template_name = 'planner/date_filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['tasks'] = TaskDay.objects.filter(user=self.request.user.id)
        print(self.kwargs['day'])
        context['tasks'] = context['tasks'].filter(date__day=self.kwargs['day'], date__month=self.kwargs['month'], date__year=self.kwargs['year'])
        return context


class CreateTask(CreateView):
    model = TaskDay
    # fields = ['name', 'date', 'tomatoes']
    form_class = AddTaskForm
    template_name = 'planner/create_task.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid((((((...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('planner_main')


class DetailTask(DetailView):
    model = TaskDay
    template_name = 'planner/detail_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['times'] = TimeDay.objects.filter(task_id=self.kwargs['pk'])
        return context


class DeleteTask(DeleteView):
    model = TaskDay
    template_name = 'planner/delete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        return context

    def get_success_url(self):
        return reverse_lazy('planner_main')


class EditTask(UpdateView):
    model = TaskDay
    template_name = 'planner/edit_task.html'
    fields = ['name', 'date', 'tomatoes', 'tomatoes_done', 'is_done']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        return context


class AddTime(CreateView):
    model = TimeDay
    fields = ['start', 'end', ]
    template_name = 'planner/add_time.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid((((((...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('task_detail', args=(self.kwargs['pk'],))


class DeleteTime(DeleteView):
    model = TimeDay
    template_name = 'planner/delete_time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        return context

    def get_success_url(self):
        return reverse_lazy('task_detail', args=(self.object.task_id,))
