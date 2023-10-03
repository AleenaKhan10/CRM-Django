from django.shortcuts import render
from .models import Lead

# Create your views here.

def lead_list(request):
    lead = Lead.objects.all()
    context = {
        'leads' : lead
    }
    return render(request, 'lead_list.html', context=context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead' : lead
    }
    return render(request, 'lead_detail.html', context=context)
