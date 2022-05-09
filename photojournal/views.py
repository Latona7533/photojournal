from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from photojournal.models import Blog
from .utils import render_to_pdf
from django.contrib.auth.mixin import LoginRequiredMixin
from .mixins import StaffAuthMixin


def blog_post_like(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect('/')

class MainsPageView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'main.html'
    context_object_name = 'blogs'

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


def model_pdf_view(request):
    template = 'test.html'
    model = Blog.objects.all()
    return render_to_pdf(template, {'model': model,})





































