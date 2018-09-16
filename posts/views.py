from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts, Amice
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AmiceForms
# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
	#return HttpResponse('Works')

	Posts = posts.objects.all()[:10]

	context = {
		'title' : 'Activiteiten',
		'Posts' : Posts
	}

	return render(request, 'posts/index.html', context)

@login_required(login_url="/accounts/login/")
def details(request, id):
	post = posts.objects.get(id=id)
	Amici = Amice.objects.select_related().filter(post=post.id)

	context = {
		'post': post,
		'Amici': Amici
	}

	return render(request, 'posts/details.html', context)

@login_required(login_url="/accounts/login/")
def upvote(request, id):
	post = posts.objects.get(pk=id)
	post.count += 1
	post.save()
	context = {
		'post': post
	}
	return render(request, 'posts/upvote.html', context)

@login_required(login_url="/accounts/login/")
def meld_u_aan(request, pk):
	post = posts.objects.get(pk=pk)

	if request.method=='POST':
		form = AmiceForms(request.POST)
		if form.is_valid():
			amice = form.save(commit=False)
			amice.post = post
			amice.save()
			return redirect('/posts')

	else:
		form = AmiceForms()
	return render(request, 'posts/amice_form.html', {'form': form})



