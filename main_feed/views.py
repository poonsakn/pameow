from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import  TemplateView
from main_feed.models import Post
# Create your views here.

class MainFeedView(TemplateView):
    template_name = "main_feed/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all()[:5]
        return context