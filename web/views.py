from django.views.generic import TemplateView, ListView, DetailView
from .models import Car
from django.db.models import Q


# View for starting page
class HomePageView(ListView):
    model = Car
    template_name = 'index.html'

    # Override get_context_data for passing CAR and CAR.CATEGORIES models
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = [e.value for e in Car.BodyStyle]
        return context


# View for retrieving result of the SEARCH
class SearchResultView(ListView):
    model = Car
    template_name = 'result-page.html'

    # function to search car by name
    def get_queryset(self):
        # get 'query' from the input in the navbar search section
        query = self.request.GET.get('query')
        return Car.objects.filter(
            Q(name__icontains=query)
        )


# View for retrieving result of FILTERING
class FilterResultView(ListView):
    model = Car
    template_name = 'result-page.html'

    # Use possibilities of QuerySet to implement filtering
    def get_queryset(self):
        state = self.request.GET.get('state')
        make = self.request.GET.get('make')
        price = self.request.GET.get('price')
        mileage = self.request.GET.get('mileage')
        return Car.objects.filter(
            Q(state__iexact=state) and Q(make__iexact=make) and Q(price__lte=price) or Q(mileage__lte=mileage)
        )


# View for representing the details of the CAR
class CarDetailView(DetailView):
    model = Car
    template_name = "details-page.html"
    # Override get_context_data for passing individual CAR and list of CAR models
    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['car_list'] = Car.objects.all()
        return context
