from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^articles', TemplateView.as_view(template_name='articles.html'), name='articles'),
    url(r'^scripts', TemplateView.as_view(template_name='scripts.html'), name='scripts'),
    url(r'^script', TemplateView.as_view(template_name='script.html'), name='script'),
    url(r'^profiles', TemplateView.as_view(template_name='profiles.html'), name='profiles'),
    url(r'^profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^articles', TemplateView.as_view(template_name='articles.html'), name='articles'),
    url(r'^article', TemplateView.as_view(template_name='article.html'), name='article'),
    url(r'^questions', TemplateView.as_view(template_name='questions.html'), name='questions'),
    url(r'^question', TemplateView.as_view(template_name='question.html'), name='question'),
]
