from django.views.generic import ListView,CreateView,DetailView
from .models import Code
class CodeListView(ListView):
    model = Code
    template_name = 'home.html'
    
class BlogCreateView(CreateView): # new
    model = Code
    template_name = 'post_new.html'
    fields = ['roll_no', 'message']
class BlogDetailView(DetailView): # new
    model = Code
    template_name = 'post_detail.html'

    