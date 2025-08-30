from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
import json

@cache_page(60 * 15)  # Cache for 15 minutes (60 seconds * 15)
def property_list(request):
    """
    View to return all properties as JSON, cached for 15 minutes
    """
    properties = Property.objects.all()
    
    # Convert properties to JSON-serializable format
    properties_data = [
        {
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),  # Convert Decimal to string for JSON
            'location': property.location,
            'created_at': property.created_at.isoformat()  # Convert DateTime to ISO string
        }
        for property in properties
    ]
    
    return JsonResponse({
        'data': properties_data,
        'count': len(properties_data),
        'status': 'success'
    })