from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Get all properties from cache if available, otherwise fetch from database
    and cache for 1 hour (3600 seconds)
    """
    # Try to get properties from Redis cache
    cached_properties = cache.get('all_properties')
    
    if cached_properties is not None:
        # Properties found in cache, return them
        return cached_properties
    
    # Properties not in cache, fetch from database
    properties = Property.objects.all()
    
    # Store in Redis cache for 1 hour (3600 seconds)
    cache.set('all_properties', properties, 3600)
    
    return properties