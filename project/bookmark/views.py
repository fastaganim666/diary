from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class IndexView(FormView, ListView):
    model = Bookmark
    paginate_by = 10
    template_name = 'bookmark/main.html'
    form_class = AddBookmarkForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['active_category'] = 'Все закладки'
        return context

    def get_success_url(self):
        return reverse_lazy('index_view')


class CategoryView(FormView, ListView):
    model = Bookmark
    paginate_by = 10
    template_name = 'bookmark/main.html'
    form_class = AddBookmarkForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=User.objects.get(id=self.request.user.id),
                                                       category_id=self.kwargs['pk'])
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['active_category'] = Category.objects.get(id=self.kwargs['pk']).name
        return context

    def get_success_url(self):
        return reverse_lazy('index_view')


class EditBookmark(UpdateView):
    model = Bookmark
    fields = ['url', 'description', 'aliace', 'category']
    template_name_suffix = '_update_form'


def delete_post(request, bookmark_id=None):
    bookmark_to_delete = Bookmark.objects.get(id=bookmark_id)
    bookmark_to_delete.delete()
    return HttpResponseRedirect(reverse('index_view'))


def delete_category(request, category_id=None):
    bookmark_to_delete = Category.objects.get(id=category_id)
    bookmark_to_delete.delete()
    return HttpResponseRedirect(reverse('index_view'))


class CreateCategory(CreateView):
    model = Category
    fields = ['name', ]
    template_name = 'bookmark/create.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        return context
