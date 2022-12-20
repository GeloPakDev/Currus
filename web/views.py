from django.views.generic import ListView, DetailView, CreateView
from .models import Car
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# View for starting page
class HomePageView(ListView):
    model = Car
    template_name = 'index.html'

    # Override get_context_data for passing CAR and CAR.CATEGORIES models
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = [e.value for e in Car.BodyStyle]
        context['colors'] = [e.value for e in Car.Color]
        return context


# View for retrieving result of the SEARCH
class SearchResultView(ListView):
    model = Car
    template_name = 'result-page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        context['categories'] = [e.value for e in Car.BodyStyle]
        context['colors'] = [e.value for e in Car.Color]
        return context

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
        # make filter section
        price = self.request.GET.get('price')
        mileage = self.request.GET.get('mileage')
        # body style filter section
        color = self.request.GET.get('color')
        body_style = self.request.GET.get('body_style')

        if (price is not None) and (mileage is not None):
            return Car.objects.filter(make__iexact=make, state__iexact=state, price__lte=price, mileage__lte=mileage)

        if (color is not None) or (body_style is not None):
            return Car.objects.filter(state__iexact=state, make__iexact=make, color__iexact=color,
                                      body_style__iexact=body_style)


# View for representing the details of the CAR
class CarDetailView(DetailView):
    model = Car
    template_name = "details-page.html"

    # Override get_context_data for passing individual CAR and list of CAR models
    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['car_list'] = Car.objects.filter(Q(make=context.get('car').make))
        return context


# View for full search
class FullSearchView(ListView):
    model = Car
    template_name = 'result-page.html'

    # Use possibilities of QuerySet to implement filtering
    def get_queryset(self):
        state = self.request.GET.get('state')
        make = self.request.GET.get('make')
        year_of_production = self.request.GET.get('year_of_production')
        price = self.request.GET.get('price')
        mileage = self.request.GET.get('mileage')
        body_style = self.request.GET.get('body_style')
        color = self.request.GET.get('color')
        fuel_type = self.request.GET.get('fuel_type')

        return Car.objects.filter(
            state__iexact=state,
            make__iexact=make,
            price__lte=price,
            production_year__lte=year_of_production,
            mileage__lte=mileage,
            body_style__iexact=body_style,
            color__iexact=color,
            fuel_type__iexact=fuel_type
        )


class AdvancedSearchView(ListView):
    template_name = 'advanced-search.html'
    model = Car


class CategoryFilterView(ListView):
    model = Car
    template_name = 'result-page.html'

    def get_queryset(self):
        body_style = self.request.GET.get('body_style')
        print("Body style : " + str(body_style))

        return Car.objects.filter(Q(body_style__iexact=body_style))


class UserProfile(ListView):
    model = get_user_model()
    template_name = 'profile.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
