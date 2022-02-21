from django.shortcuts import render
from .models import Profile
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'Profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'Profile/create_profile.html'
    fields = ['profile_pic']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    