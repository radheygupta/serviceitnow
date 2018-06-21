from django.db.models import F

from .models import Features


def reorder_priorties(client, priority):
    Features.objects.filter(client=client, priority__gte=priority, status='Active').update(priority=F('priority')+1)
