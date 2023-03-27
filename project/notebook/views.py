from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse

from .models import *
from .forms import *


class MainNotebook(ListView):
    model = Note
    paginate_by = 10
    template_name = 'notebook/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои записи'
        context['notes'] = Note.objects.filter(user_id=self.request.user.id)
        return context


class DetailNotebook(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notebook/detail_note.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои записи'
        return context


class CreateNotebook(CreateView):
    model = Note
    template_name = 'notebook/create_note.html'
    # fields = ['title', 'content', 'category']
    form_class = AddNoteForm

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

    def get_success_url(self):
        return reverse_lazy('notebook_main')


class DeleteNotebook(DeleteView):
    model = Note
    template_name = 'notebook/delete_note.html'
    context_object_name = 'note'

    def get_success_url(self):
        return reverse_lazy('notebook_main')


class EditNotebook(UpdateView):
    model = Note
    template_name = 'notebook/edit_note.html'
    context_object_name = 'note'
    form_class = AddNoteForm

    def get_success_url(self):
        return reverse_lazy('notebook_main')


