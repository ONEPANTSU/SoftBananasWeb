from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import ArticlesForm
from .models import Articles

# Create your views here.


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/create_news.html"
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = "news/delete_news.html"


def news(request):
    news = Articles.objects.order_by("-date")
    return render(request, "news/news.html", {"news": news})


def create_news(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            error = "WRONG FORM!"

    form = ArticlesForm()
    data = {
        "form": form,
        "error": error,
    }
    return render(request, "news/create_news.html", data)
