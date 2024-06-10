from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    variable = "Welcome to Try Django"
    qs = BlogPost.objects.all()[:5]
    context = {"variable" : variable, 'blog_list' : qs}
    return render(request,"hello.html",context)

def about_page(request):
    return render(request, "about.html",{"variable" : "About us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "variable" : "Contact US",
        "form" : form
    }
    return render(request, "form.html",context)

def example_page(request):
    context = {"variable" : "example"}
    template_name = "hello.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))
