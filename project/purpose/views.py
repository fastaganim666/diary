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


class MainPurpose(ListView):
    model = Purpose
    paginate_by = 10
    template_name = 'purpose/main.html'
    context_object_name = 'purposes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои цели'
        return context


class CreatePurpose(CreateView):
    model = Purpose
    fields = ['name', 'main', 'people', 'priority', 'deadline']
    template_name = 'purpose/create_purpose.html'

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


class DetailPurpose(DetailView, FormView):
    model = Purpose
    context_object_name = 'purpose'
    template_name = 'purpose/detail_purpose.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['steps'] = Step.objects.filter(purpose=kwargs['object'])
        context['constraints'] = Constraint.objects.filter(purpose=kwargs['object'])
        context['skills'] = Skill.objects.filter(purpose=kwargs['object'])
        context['questions'] = Question.objects.filter(purpose=kwargs['object'])
        context['comments'] = Comment.objects.filter(purpose=kwargs['object'])
        return context

    def form_valid(self, form):
        Comment.objects.create(**form.cleaned_data, purpose_id=self.kwargs['pk'])
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse("form is invalid((((((...")

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.kwargs['pk'],))


class DeletePurpose(DeleteView):
    model = Purpose
    template_name = 'purpose/delete_purpose.html'
    context_object_name = 'purpose'

    def get_success_url(self):
        return reverse_lazy('purpose_main')


class EditPurpose(UpdateView):
    model = Purpose
    template_name = 'purpose/edit_purpose.html'
    fields = ['name', 'main', 'people', 'priority', 'deadline', 'achieved', 'achievement_date', ]

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.id,))


class CreateStep(CreateView):
    model = Step
    fields = ['name', ]
    template_name = 'purpose/create_step.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.purpose_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.purpose.id,))


class DeleteStep(DeleteView):
    model = Step
    template_name = 'purpose/delete_step.html'
    context_object_name = 'step'

    def get_success_url(self):
        print(self.object)
        purpose_id = self.object.purpose.id
        print(purpose_id)
        return reverse_lazy('purpose_detail', args=(purpose_id,))


def step_done(request, pk=None):
    step = Step.objects.get(id=pk)
    step.completed = True
    step.save()
    return HttpResponseRedirect(step.get_absolute_url())


def not_step_done(request, pk=None):
    step = Step.objects.get(id=pk)
    step.completed = False
    step.save()
    return HttpResponseRedirect(step.get_absolute_url())


class CreateConstraint(CreateView):
    model = Constraint
    fields = ['name', ]
    template_name = 'purpose/create_constraint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.purpose_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.purpose.id,))


class DeleteConstraint(DeleteView):
    model = Constraint
    template_name = 'purpose/delete_constraint.html'
    context_object_name = 'constraint'

    def get_success_url(self):
        print(self.object)
        constraint_id = self.object.purpose.id
        return reverse_lazy('purpose_detail', args=(constraint_id,))


def constraint_done(request, pk=None):
    constraint = Constraint.objects.get(id=pk)
    constraint.completed = True
    constraint.save()
    return HttpResponseRedirect(constraint.get_absolute_url())


def not_constraint_done(request, pk=None):
    constraint = Constraint.objects.get(id=pk)
    constraint.completed = False
    constraint.save()
    return HttpResponseRedirect(constraint.get_absolute_url())


class CreateSkill(CreateView):
    model = Skill
    fields = ['name', ]
    template_name = 'purpose/create_skill.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.purpose_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.purpose.id,))


class DeleteSkill(DeleteView):
    model = Skill
    template_name = 'purpose/delete_skill.html'
    context_object_name = 'skill'

    def get_success_url(self):
        print(self.object)
        constraint_id = self.object.purpose.id
        return reverse_lazy('purpose_detail', args=(constraint_id,))


def skill_done(request, pk=None):
    skill = Skill.objects.get(id=pk)
    skill.completed = True
    skill.save()
    return HttpResponseRedirect(skill.get_absolute_url())


def not_skill_done(request, pk=None):
    skill = Skill.objects.get(id=pk)
    skill.completed = False
    skill.save()
    return HttpResponseRedirect(skill.get_absolute_url())


class CreateQuestion(CreateView):
    model = Question
    fields = ['name', ]
    template_name = 'purpose/create_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.purpose_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.purpose.id,))


class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'purpose/delete_question.html'
    context_object_name = 'question'

    def get_success_url(self):
        print(self.object)
        constraint_id = self.object.purpose.id
        return reverse_lazy('purpose_detail', args=(constraint_id,))

class EditQuestion(UpdateView):
    model = Question
    template_name = 'purpose/edit_question.html'
    fields = ['answer', ]

    def get_success_url(self):
        print(self.object)
        constraint_id = self.object.purpose.id
        return reverse_lazy('purpose_detail', args=(constraint_id,))


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'purpose/delete_comment.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('purpose_detail', args=(self.object.purpose.id,))
