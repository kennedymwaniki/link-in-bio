from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Profile, Link

# INTERNAL
# list out the links
# create a new link

# EXTERNAL
# see a profile (and it's links)


class LinkListView(ListView):
    model = Link
    # def template model_list.html


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # template - model_form.html
    # figure out what fields - could pass a list
    # success_url
    #           or specify fields
    #  fields = ['text', 'url', 'profile']
    # template_name = 'link_form.html'
    # success_url = '/'


class LinkUpdateView(UpdateView):
    # Shares same template as create view
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy('link-list')


class LinkDeleteView(DeleteView):
    # send a form with a single 'confirm delete btn'
    # template - model_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')

# external profile view - could be a ListView or a function view


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)


# class ProfileView(DetailView):
#     model = Profile
#     template_name = 'profile.html'
#     context_object_name = 'profile'
#     slug_field = 'slug'
#     slug_url_kwarg = 'profile_slug'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['links'] = self.object.links.all()
#         return context
