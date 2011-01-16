from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from sponsors.models import Sponsor
# Create your views here.

def sponsor_list(request, paginate_by=100, **kwargs):
    return list_detail.object_list(
        request,
        queryset = Sponsor.objects.all().order_by('name'),
        paginate_by = paginate_by,
        **kwargs
    )
