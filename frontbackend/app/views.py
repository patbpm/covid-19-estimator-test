from django.shortcuts import render

# Create your views here.

def homepage(request):
    
    context = {
        
    } 
    
    return render(request, 'app/templates/homepage.html', context)
