from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import NewPostForm

class PostListView(generic.ListView):
    # model =Post
    template_name = 'blog/list_post.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return  Post.objects.filter(status='pub').order_by('datetime_modifie')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name ='blog/post_create.html'
    form_class = NewPostForm


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('list_post')
    
    
    
# def list_post_views(request):
#     #post_list = Post.objects.all()
#     post_list = Post.objects.filter(status='pub').order_by('datetime_modifie')

#     return render(request, 'blog/list_post.html', {'post_list': post_list})
# # Create your views here.
    

# def list_post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     #try:
#         #post = Post.objects.get(pk=pk)
#     #except ObjectDoesNotExist:
#         #post = None

    # return render (request, 'blog/post_detail.html', {'post':post})
# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_post')
        

#     else:
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form':form} )
    
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None,instance=post)

#     if form.is_valid():
#         form.save()
#         return redirect('list_post')

#     return render(request, 'blog/post_create.html', context={'form':form})
    
# def post_delet_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('list_post')

#     return render(request, 'blog/post_delete.html',context={'post':post})


