from django.shortcuts import render
from django.http import HttpResponse


posts = [ {'author' : 'Name-1'}, {'author' : 'Name-2'} ]

def home(request) :
	#return HttpResponse('<h1>Home page</h1>')
	context = {
		'posts'  : posts
	}
	return render(request, 'genom/home.html', context)

def judge(request) :
	#return HttpResponse('<h1>About page </h1>')
	return render (request, 'genom/judge.html',{'title': 'Judge'})

