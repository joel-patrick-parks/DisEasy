from django.shortcuts import render

from models import Visualization

# display homepage
def home(request):
    return render(request, 'UI/index.html')

# display form
def form(request):
    return render(request, 'UI/form.html')

# display results page
def result(request, figure=0, supplementary=0,score=0):
    context = {
            'figure': figure,
            'supplementary': supplementary,
            'score': score,
            'visualizations': Visualization.objects.all(),
            }
    return render(request, 'UI/result.html', context)
