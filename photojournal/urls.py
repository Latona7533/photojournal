from django.urls import path
from photojournal.views import main_page, PostDetailView, blog_post_like, model_pdf_view, PostUpdateView

urlpatterns = [
    path('', main_page),
    path('post-like/<int:pk>', blog_post_like, name="post_like"),
    path('p', model_pdf_view),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post_update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
]