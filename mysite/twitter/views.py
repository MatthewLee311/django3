from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import PostForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
    form = LoginForm(request.POST)
    context = {
        'form': form
    }
    # Get method
    if form.is_valid():
        enteredUsername = request.POST['enteredUsername']
        enteredPassword = request.POST['enteredPassword']
        user = authenticate(username= enteredUsername, password= enteredPassword)
        if user is not None:
            login(user)
            # A backend authenticated the credentials
            HttpResponseRedirect('/twitter/')

        else:
            # No backend authenticated the credentials
            HttpResponseRedirect('')

    return render(request, 'twitter/login.html', context)

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    username = Post.username
    pub_date = Post.pub_date
    template = loader.get_template('twitter/index.html')
    form = PostForm
    context = {
        'latest_post_list': latest_post_list,
        'username': username,
        'pub_date': pub_date,
        'form': form,
    }
    return render(request, 'twitter/index.html', context)

def get_post(request):
    # if this is a POST request we need to process the form data
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
            return HttpResponseRedirect('/twitter/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
    return render(request, 'twitter/index.html', {'form': form})
