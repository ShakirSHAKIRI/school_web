from django.shortcuts import render,redirect
from .models import Section

# Create your views here.
def Home(request):
    return render(request,'home.html')

def Add_Section(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        description = request.POST.get('description')
        section = Section(label=label,description=description)
        section.save()
        return redirect("add_section")
    return render(request,'sections/add_section.html')
