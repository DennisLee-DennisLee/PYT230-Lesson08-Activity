from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from rest_framework import viewsets
from blogging.models import Post, Category
from blogging.serializers import UserSerializer, GroupSerializer, PostSerializer, CategorySerializer
from blogging.forms import PostForm, CategoryForm

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)

def add_model(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, "my_template.html", {'form': form})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
