from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View, Template
from .models import Service
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

# class ServiceListView(ListView):
#     context_object_name = 'services'
#     model = Service
#     template_name = "index.html"

# class ServiceDetailView(DetailView):
#     context_object_name = 'service_detail'
#     model = Service
#     template_name = "index.html"

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})