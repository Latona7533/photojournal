from django.urls import path
from photojournal.views import MainPageView, PostDeteilView, blog_post_like, model_pdf_view

urlpatterns = [
    path('', MainPageView.as_view()),
    path('post-like/<int:pk>', blog_post_like, name="post_like"),
    path('p', model_pdf_view),

]