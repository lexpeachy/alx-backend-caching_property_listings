from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties  # Import the utility function
import json

@cache_page(60 * 15)  # Keep the page-level cache for 15 minutes too
def property_list(request):
    """
    View to return all properties as JSON, using cached queryset
    """
    # Use our utility function to get properties (cached or from DB)
    properties = get_all_properties()
    
    # Convert properties to JSON-serializable format
    properties_data = [
        {
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),
            'location': property.location,
            'created_at': property.created_at.isoformat()
        }
        for property in properties
    ]
    
    return JsonResponse({
        'data': properties_data,
        'count': len(properties_data),
        'status': 'success',
        'source': 'cache' if cache.get('all_properties') is not None else 'database'
    })