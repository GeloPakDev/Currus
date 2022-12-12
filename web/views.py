from django.views.generic import TemplateView, ListView, DetailView
from .models import Car
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultView(ListView):
    model = Car
    template_name = 'result-page.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Car.objects.filter(
            Q(description__icontains=query) or Q(make__icontains=query) or Q(name__icontains=query)
        )


class CarDetailView(DetailView):
    model = Car
    template_name = "details-page.html"
