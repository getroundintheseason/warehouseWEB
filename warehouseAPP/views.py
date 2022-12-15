from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Collection

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'warehouseAPP/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('collections')

class RegisterPage(FormView):
    template_name = 'warehouseAPP/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('collections')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('collections')
        return super(RegisterPage, self).get(*args, **kwargs)

class CollectionList(LoginRequiredMixin, ListView):
    model = Collection
    context_object_name = 'collections'

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        contex['collections'] = contex['collections'].filter(user=self.request.user)
        contex['count'] = contex['collections'].filter(isBorrow=False).count()

        search_input = self.request.GET.get('search-area') or ''
        search_type_input = self.request.GET.get('search-type') or ''
        search_params = {
            '{}__icontains'.format(search_type_input): search_input,
        }
        if search_input:
            print(type(contex['collections']))
            contex['collections'] = contex['collections'].filter(**search_params)
            #contex['collections'] = contex['collections'].filter(title__icontains=search_input)

        contex['search_input'] = search_input
        return contex

class CollectionDetail(LoginRequiredMixin, DetailView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'warehouseAPP/collections.html'

class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['category', 'artist', 'title', 'desciption', 'bookcase', 'isBorrow', 'borrowWho']
    success_url = reverse_lazy('collections')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CollectionCreate, self).form_valid(form)

class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ['category', 'artist', 'title', 'desciption', 'bookcase', 'isBorrow', 'borrowWho']
    success_url = reverse_lazy('collections')

class CollectionDelete(LoginRequiredMixin, DeleteView):
    model = Collection
    fields = '__all__'
    success_url = reverse_lazy('collections')
