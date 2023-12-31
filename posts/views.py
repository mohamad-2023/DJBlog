from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostList(LoginRequiredMixin,generic.ListView):  # html post_list , context object_list or post_list 
    model = Post
    login_url = '/admin/login'


class PostDetail(generic.DetailView):  #html post_detail , context object or post
    model = Post


class PostNew(generic.CreateView):
    model = Post
    fields =['title','puplish_date','content','author','image','tags']
    success_url = '/blog/'

class PostEdit(generic.UpdateView):
    model = Post
    fields = ['title','puplish_date','content','author','image','tags']
    success_url = '/blog/'
    template_name = 'posts/edit.html'


class PostDelte(generic.DeleteView):
    model = Post
    success_url = '/blog/'


'''
def post_list(request):
    data= Post.objects.all()
    return render(request, 'posts/posts.html', {'posts':data})



def post_detail(request, post_id):
    data = Post.objects.get(id = post_id)
    return render(request, 'posts/detail.html', {'post':data})




def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form= PostForm()
    return render(request, 'posts/new.html', {'form':form})




def edit_post(request,post_id):
    data = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form= PostForm(instance=data)
    return render(request,'posts/edit.html',{'form':form})
    
'''
def delete_post(request,post_id):
    data= Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')