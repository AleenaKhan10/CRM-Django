from django.shortcuts import redirect, render
from .models import Lead
from .forms import LeadModelForm

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

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lead-list')
    context = {
        'form' : form
    }
    return render(request, 'lead_create.html', context=context)
