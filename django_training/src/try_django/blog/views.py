from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostForm
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def blog_post_detail_page(request,slug):
    # try:
    #     obj = BlogPost.objects.get(id=id)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(BlogPost,slug=slug)
    # print(obj)
    # qs = BlogPost.objects.filter(slug=slug)
    # if qs.count() >= 1:
    #     obj = qs.first()
    template_name = "blog_post_detail_page.html"
    context = {"object" : obj}
    return render(request,template_name,context)

# Create your views here.

def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = "blog/list.html"
    context = {'object_list' : qs}
    return render(request,template_name,context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = "blog/form.html"
    context = {'form' : form}
    return render(request,template_name,context)

def blog_post_detail_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = "blog/detail.html"
    context = {"object" : obj}
    return render(request,template_name,context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        # Redirect or add a success message
        else:
            print(form.errors)
    else:
        print("GET method")
    # if form.is_valid():
    #     form.save()
    template_name = "blog/updateForm.html"
    context = {'form' : form, 'variable' : f"Update {obj.title}"}
    return render(request,template_name,context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/blogs")
    template_name = "blog/delete.html"
    context = {"object" : obj}
    return render(request,template_name,context)
