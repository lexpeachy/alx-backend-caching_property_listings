from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

@receiver(post_save, sender=Property)
def invalidate_cache_on_save(sender, instance, **kwargs):
    """
    Invalidate the all_properties cache when a Property is created or updated
    """
    print(f"🚀 Property saved (id: {instance.id}) - Invalidating cache...")
    cache.delete('all_properties')
    print("✅ Cache invalidated")

@receiver(post_delete, sender=Property)
def invalidate_cache_on_delete(sender, instance, **kwargs):
    """
    Invalidate the all_properties cache when a Property is deleted
    """
    print(f"🗑️ Property deleted (id: {instance.id}) - Invalidating cache...")
    cache.delete('all_properties')
    print("✅ Cache invalidated")