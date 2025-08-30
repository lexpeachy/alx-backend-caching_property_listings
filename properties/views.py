from django.shortcuts import render
# Create your views here.
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15) #cache for 15 minutes(60 seconds * 15)
def property_list(request):
    #views to display all the properties cached for 15 minutes
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})