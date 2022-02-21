from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import MainPageMenu, Comments
from .forms import CommentForm


class Mains(View):
    def get(self, request):
        main = MainPageMenu.objects.all
        context =  {
            "main_list": main
        }
        return render(request, 'index.html', context)


class Pk(View):
    def get(self, request, slug):
        main = MainPageMenu.objects.get(slug=slug)
        comments = Comments.objects.all().filter(posts=main)
        form = CommentForm()
        context =  {
            'form': form,
            "main_list": main,
            "comment": comments
        }
        return render(request, 'pk.html', context)

    def post(self, request, *args, **kwargs):
            com = request.POST['com']
            if com:  
                id = request.POST['com']  
                post = get_object_or_404(MainPageMenu, id=id)
                form = CommentForm(request.POST)
                if form.is_valid():
                    a = form.save()
                    a.user = request.user
                    a.posts = post
                    a.save()
                    return redirect(post)

                


        


