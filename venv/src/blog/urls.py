from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import post

urlpatterns = patterns('', 
	url(r'^$',ListView.as_view(
		queryset=post.objects.all().order_by("-date")[:10],template_name='blog.html')), 
	url(r'^(?P<pk>\d+)$',DetailView.as_view(
		model = post,template_name= "post.html")), 





	)

# Create your views here.
