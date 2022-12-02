from django.views.generic import TemplateView, ListView
from .models import Car


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultPage(ListView):
    model = Car
    template_name = 'result-page.html'

