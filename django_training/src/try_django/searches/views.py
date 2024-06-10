from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost

# Create your views here.
def search_view(request):
    query = request.GET.get('q',None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query" : query}

    if query is not None:
        SearchQuery.objects.create(user=user,query=query)
        qs = BlogPost.objects.search(query)
        context['blog_list'] = qs
    return render(request,'searches/view.html', context)

