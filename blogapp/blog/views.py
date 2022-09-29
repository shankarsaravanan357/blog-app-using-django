from django.shortcuts import render


# Create your views here.

posts = [
	{
		'author':'Shanks',
		'title':'Blog Post 1',
		'content':'First Post Content',
		'date_posted':'September 28, 2022'
	},
	{
		'author':'Zoro',
		'title':'Blog Post 2',
		'content':'Second Post Content',
		'date_posted':'September 29, 2022'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html')