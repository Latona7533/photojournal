from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from photojournal.models import Blog, Theme
from .utils import render_to_pdf
from django.views.generic import View

def blog_post_like(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect('/')


class PostDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'

    def get_cotnext_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Blog, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('templates/test.html')
        return HttpResponse(pdf, content_type='application/pdf')

class PostUpdateView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = 'title', 'description'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Data was updated!')
        return HttpResponseRedirect('/')


def main_page(request):
    user = request.user

    if Theme.objects.filter(user=user.username).exists():
            color = Theme.objects.get(user=user.username).color
    else:
        color = 'blue'

    post = Blog.objects.all()


    context = {
                'color': color,
                'post': post,
              }

    return render(request, 'main.html', context)

def theme(request):
    color = request.GET.get('color')
    if color == 'dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme = Theme.objects.get(user=request.user.username)
            user_theme.user = request.user.username
            user_theme.color = 'grey'
            user_theme.save()
        else:
            user2 = Theme(user=request.user.username, color='grey')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user.username).exists():
                user_theme1 = Theme.objects.get(user=request.user.username)
                user_theme1.user = request.user.username
                user_theme1.color = 'white'
                user_theme1.save()
        else:
            user4 = Theme(user=request.user.username, color='white')
            user4.save()
    return redirect('/')


class MainsPageView(ListView):
    model = Blog
    template_name = 'main.html'
    context_object_name = 'blogs'

def model_pdf_view(request):
    template = 'test.html'
    model = Blog.objects.all()
    return render_to_pdf(template, {'model': model,})
































