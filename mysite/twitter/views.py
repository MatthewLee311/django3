from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import PostForm


# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    username = Post.username
    pub_date = Post.pub_date
    template = loader.get_template('twitter/index.html')
    context = {
        'latest_post_list': latest_post_list,
        'username': username,
        'pub_date': pub_date,
    }
    return render(request, 'twitter/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'twitter/detail.html', {'post': post})

def get_post(request):
    # if this is a POST request we need to process the form data
    print("text")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(request.POST)
            p = Post(username = request.POST['username'], post_text = request.POST['postText'], pub_date = timezone.now())
            p.save()
            print(p)
            return HttpResponseRedirect('/twitter/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
    print(form)
    return render(request, 'twitter/index.html', {'form': form})

#def results(request,question_id):
    #question = get_object_or_404(Post, pk=post_id)
    #return render(request, 'twitter/results.html', {'post': post})

    # Add input box for new post

# class IndexView(generic.ListView):
#     template_name = 'twitter/index.html'
#     context_object_name = 'latest_post_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published posts (not including those set to be
#         published in the future).
#         """
#         return Post.objects.filter(
#         pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Post
#     template_name = 'twitter/detail.html'
#     def get_queryset(self):
#         """
#         Excludes any posts that aren't published yet.
#         """
#         return Post.objects.filter(pub_date__lte=timezone.now())
#
# class ResultsView(generic.DetailView):
#     model = Post
#     template_name = 'twitter/results.html'
