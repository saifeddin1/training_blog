from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def index(request):
	return render(request, 'posts/index.html')


def posts_list(request):
	query_list = Post.objects.order_by('created_at')
	context = {
			"query_list":query_list,
	}
	return render(request, 'posts/posts_list.html', context)

def post_create(request):
	form = PostForm()
	if request.method== 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('posts_list')

	context = {
		'form':form,
	}
	return render(request, 'posts/post_form.html', context)


def post_detail(request, post_id):
	instance = get_object_or_404(Post, id=post_id)

	context = {
		'instance':instance,
	}
	return render(request, 'posts/post_detail.html', context)


def post_update(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=instance)

	if form.is_valid():
		form.save()
		return redirect('posts_list')

	context = {
		'instance':instance,
		'form':form,
	}
	return render(request, 'posts/post_update.html', context)


def post_delete(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	instance.delete()
	return redirect('posts_list')
