from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from models import Visualization

# display homepage
def home(request):
    return render(request, 'UI/home.html')

def formDiabetes(request):
    return render(request, 'UI/diabetes/form.html')

# display results page
def resultDiabetes(request, 
        uprob = 0, 
        ures = 0, 
        age = 0, 
        gender = -1, 
        bmi = 0, 
        albu = 0,
        glyco = 0):

    visualizations = []
    for visualization in Visualization.objects.filter(FeatureType="All"):
        visualizations.append(visualization)

    for visualization in Visualization.objects.filter(FeatureType="Diabetic"):
        visualizations.append(visualization)

    if age > 0:
        for visualization in Visualization.objects.filter(
                FeatureType="Age",
                FeatureValue=ageRange(age)):
            visualizations.append(visualization)

    if gender > -1:
        for visualization in Visualization.objects.filter(
                FeatureType="Gender",
                FeatureValue=genderVal(gender)):
            visualizations.append(visualization)
        
    if bmi > 0:
        for visualization in Visualization.objects.filter(
                FeatureType="BMI",
                FeatureValue=bmiRange(bmi)):
            visualizations.append(visualization)

    context = {
            'visualizations': visualizations,
            'probability': uprob,
            'result': ures,
            'albumin': albu,
            'glycohemoglobin': glyco,
            }

    return render(request, 'UI/diabetes/result.html', context)

def formThyroid(request):
    return render(request, 'UI/thyroid/form.html')

def resultThyroid(request, age, gender, TSH, T3, TT4, result, accuracy, probability):
    # visualizations = []
    # for visualization in Visualization.objects.filter(FeatureType="All"):
    #     visualizations.append(visualization)

    # for visualization in Visualization.objects.filter(FeatureType="Diabetic"):
    #     visualizations.append(visualization)

    # if age > 0:
    #     for visualization in Visualization.objects.filter(
    #             FeatureType="Age",
    #             FeatureValue=ageRange(age)):
    #         visualizations.append(visualization)

    # if gender > -1:
    #     for visualization in Visualization.objects.filter(
    #             FeatureType="Gender",
    #             FeatureValue=genderVal(gender)):
    #         visualizations.append(visualization)

    context = {
            # 'visualizations' : visualizations,
            'TSH': TSH,
            'T3': T3,
            'TT4': TT4,
            'result': result,
            'accuracy': accuracy,
            'probability': probability,
            }

    return render(request, 'UI/thyroid/result.html', context)

def ageRange(age):
    if float(age)<31:
        return "18-30"
    elif float(age)<41:
        return "31-40"
    elif float(age)<56:
        return "41-55"
    elif float(age)<71:
        return "55-70"
    else:
        return "71-85"

def genderVal(gender):
    if int(gender) == 0:
        return "Female"
    elif int(gender) == 1:
        return "Male"

def bmiRange(bmi):
    if float(bmi)<18.6:
        return "0-18.5"
    elif float(bmi)<25:
        return "18.6-24.9"
    elif float(bmi)<29.9:
        return "25-29.9"
    else:
        return "30-50"

# about page
def about(request):
    return render(request, 'UI/about.html')

# login
def login(request):
    return render(request, 'UI/login.html')

def treatmentDiabetes(request):
    return render(request, 'UI/diabetes/treatment.html')

def treatmentHypoThyroid(request):
    return render(request, 'UI/thyroid/treatment-hypothyroidism.html')

def treatmentHyperThyroid(request):
    return render(request, 'UI/thyroid/treatment-hyperthyroidism.html')
