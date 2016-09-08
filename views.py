from django.shortcuts import render,get_object_or_404
from .models import NewsPost
from django.core.paginator import Paginator,EmptyPage,\
                                  PageNotAnInteger
from .forms import CommentForm

# Create your views here.

def home(request):
	return render(request,
		          'home/homepage.html',
		          {'section':'home'})

def news(request):
	object_list = NewsPost.published.all()
	paginator = Paginator(object_list,6)
	page = request.GET.get('page')
	try:
		 posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,
				  'home/newspage.html',
				  {'section':'news',
				   'page':page,
				   'posts':posts})


def news_detail(request,year,month,day,slug):
	post = get_object_or_404(NewsPost,
							 publish__year = year,
							 publish__month = month,
							 publish__day = day, 
							 slug = slug )

		#list of active comments for this post
	comments = post.comments.filter(active = True)

	if request.method == 'POST':
		comment_form = CommentForm(data = request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request,
				  'home/newsdetail.html',
				  {'post':post,
				   'comments':comments,
				   'comment_form':comment_form,})
