from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post, Comment
from .forms import PostForm, CommentForm
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


	paginator = Paginator(query_list, 8)
	page_request_var = 'page'
	page_number = request.GET.get(page_request_var)

	try:
		page_obj = paginator.get_page(page_number)
	except PageNotAnInteger:
		page_obj = paginator.get_page(1)
	except EmptyPage:
		page_obj = paginator.get_page(paginator.num_pages)

	user = request.user 
	context = {
			"page_obj":page_obj,
			"user": user,
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
	latest = Post.objects.order_by('created_at')[0:3]

	instance = get_object_or_404(Post, id=post_id)
	comments = instance.comment.all()
	comment_form = CommentForm()
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None, request.user)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.commented_post = instance			
			new_comment.name = request.user
			new_comment.save()
			return redirect('detail', post_id=instance.id)


	context = {
		'latest':latest,
		'instance':instance,
		'comment_form':comment_form,
		'all_comments':comments,
		'new_comment':new_comment,
	}
	return render(request, 'posts/post_detail.html', context)


def post_update(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	if not request.user.is_superuser or not request.user.is_staff:
		raise Http404()
	form = PostForm(request.POST or None, instance=instance)

	if form.is_valid():
		form.save()
		return redirect('detail', post_id=instance.id)

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



def delete_comment(request, comment_id, post_id):
	post_instance = get_object_or_404(Post, id=post_id)
	comment_instance = get_object_or_404(Comment, id=comment_id)
	if not request.user.is_superuser or not request.user.is_staff:
		raise Http404()
	comment_instance.delete()
	return redirect('detail', post_id=post_instance.id)

