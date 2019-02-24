from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author' : 'PremK',
		'title' : 'blog post 1',
		'content' : 'first post content',
		'date_posted' : 'Aug,27,2018'
	},
	{
		'author' : 'SuseeK',
		'title' : 'blog post 2',
		'content' : 'second post content',
		'date_posted' : 'dec,27,2018'
	}
]

def home(request) :
	#return HttpResponse('<h1>Home page</h1>')
	context = {
		'posts'  : posts
	}
	return render(request, 'genom/home.html', context)

def about(request) :
	#return HttpResponse('<h1>About page </h1>')
	return render (request, 'genom/about.html',{'title': 'About'})

# Create your views here.
