from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles
from django.views.generic import DetailView, UpdateView, DeleteView




# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def news(request):

    newsobject = Articles.objects.order_by('date')

    return render(request,'core/news_startpage.html', {'newsobject' : newsobject})


def addnews(request):


    if request.method=='POST':

        form = ArticlesForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('mainnews')

    return render(request, 'core/addnews.html')

class NewsDetailView(DetailView):

    model= Articles

    template_name = 'core/details_view.html'

    context_object_name = 'article'

class NewsUpdateView(UpdateView):
        model = Articles

        template_name = 'core/addnews.html'

        form_class = ArticlesForm

class NewsDeleteView(DeleteView):

    model = Articles

    template_name= 'core/NewsDelete.html'

    success_url = '/mainnews/'


