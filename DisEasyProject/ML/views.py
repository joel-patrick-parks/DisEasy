from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
import sys
import math
from models import TrainedModel
import pickle
import numpy as np
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["POST", "GET"])
@csrf_exempt
def submitDiabetes(request):
    # fetch model
    model = TrainedModel.objects.get(diseaseState="diabetes")

    # extract and convert data
    age = float(request.POST.get('age','7'))
    gender = request.POST.get('gender','').strip()
    if gender.lower() == 'male':
        gender = 1
    elif gender.lower() == 'female':
        gender = 0
    else:
        gender = -1
    weight = float(request.POST.get('weight','0')) / 2.2
    height = float(request.POST.get('height','0')) * 2.54
    gh = float(request.POST.get('testOne','0'))
    albumin = float(request.POST.get('testTwo','0'))
    
    if age == 0:
        return HttpResponse("Invalid Age")
    if gender == -1:
        return HttpResponse("Invalid Gender")
    if weight == 0:
        return HttpResponse("Invalid Weight")
    if height == 0:
        return HttpResponse("Invalid Height")
    if gh == 0:
        return HttpResponse("Invalid Glycohemoglobin Value")
    if albumin == 0:
        return HttpResponse("Invalid Albumin Value")

    # example of making a prediction for a sample
    testPoint = [age, gender, weight, height, gh, albumin]
    normPoint = []
    for item in range(len(testPoint)) :
        tempval = ((testPoint[item])-model.medians[item])/(model.standardDeviations[item]+0.0001)
        val = int(tempval*1000)
        normPoint.append(float(val/1000))
    
    #prediction score
    result = model.model.predict_proba(np.array(normPoint).reshape(1,-1))[0][0]

    # convert height to meters for BMI
    heightM = height / 100.;

    return HttpResponse("/diabetes/result/%s-%s-%s-%s-%s-%s-%s" % (
        round(model.accuracy * 100, 2),
        round(result * 100, 2),
        round(age, 2),
        gender,
        round(weight / (heightM * heightM), 2),
        round(albumin, 2),
        round(gh ,2),
        ))

@require_http_methods(["POST", "GET"])
@csrf_exempt
def submitThyroid(request):
    return HttpResponse("Coming soon!")
