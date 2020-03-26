from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.db.models import Q


def index(request):
	return render(request, 'posts/index.html')


def posts_list(request):
	query_list = Post.objects.order_by('created_at')

	query = request.GET.get('q')
	if query:
		query_list = query_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)
			).distinct()
	user = request.user 
	context = {
			"user": user,
			"query_list":query_list,
	}
	return render(request, 'posts/posts_list.html', context)

def post_create(request):
	if not request.user.is_superuser or not request.user.is_staff:
		raise Http404()
	form = PostForm()
	if request.method== 'POST':
		form = PostForm(request.POST or None, request.user)
		if form.is_valid():
			instance = form.save(commit=False) 
			instance.user = request.user #if you remove this it causes integrity error
			instance.save()
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
	if not request.user.is_superuser or not request.user.is_staff:
		raise Http404()
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
	if not request.user.is_superuser or not request.user.is_staff:
		raise Http404()
	instance.delete()
	return redirect('posts_list')
