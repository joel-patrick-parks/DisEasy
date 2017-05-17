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
    age = float(request.POST.get('age','0'))
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
    # extract and convert data
    age = float(request.POST.get('age','0'))
    gender = request.POST.get('gender','').strip()
    if gender.lower() == 'male':
        gender = 0
    elif gender.lower() == 'female':
        gender = 1
    else:
        gender = -1
    TSH = float(request.POST.get('testOne', '0'))
    T3 = float(request.POST.get('testTwo', '0'))
    TT4 = float(request.POST.get('testThree', '0'))
    
    if age == 0:
        return HttpResponse("Invalid Age")
    if gender == -1:
        return HttpResponse("Invalid Gender")
    if TSH == 0:
        return HttpResponse("Invalid TSH value.")
    if T3 == 0:
        return HttpResponse("Invalid T3 value.")
    if TT4 == 0:
        return HttpResponse("Invalid TT4 value.")

    return predictOneThyroid(age, gender, TSH, T3, TT4)

def predictOneThyroid(age, gender, TSH, T3, TT4):
    model = TrainedModel.objects.get(diseaseState="Thyroid MultiPart")
    
    testPoint = [age, gender, TSH, T3, TT4]
    normPoint = []
    for item in range(len(testPoint)):
        tempVal = ((testPoint[item])-model.medians[item])/(model.standardDeviations[item]+0.0001)
        val = int(tempVal*1000)
        normPoint.append(float(val/1000))

    #prediction score
    prediction = model.model.predict_proba(np.array(normPoint).reshape(1,-1))
    result = np.argmax(prediction)-3 #returns classification corresponding to data labels

    return HttpResponse("/thyroid/result/%s-%s-%s-%s-%s-%s-%s-%s" % (
        round(age, 2),
        gender,
        round(TSH, 2),
        round(T3, 2),
        round(TT4, 2),
        result,
        round(model.accuracy, 2),
        round(prediction, 2),
        ))

def predictAllThyroid(age, gender, TSH, T3, TT4):
    model = TrainedModel.objects.get(diseaseState = "Thyroid IndividalClassifications")

    testPoint = [age, gender, TSH, T3, TT4]
    normPoint = []
    for item in range(len(testPoint)):
        tempVal = ((testPoint[item])-model.medians[item])/(model.standarDeviations[item]+0.0001)
        val = int(tempVal*1000)
        normPoint.append(float(val/1000))

    result = np.argmax(prediction)-3 # returns max classification corresponding to data labels

    return HttpResponse("/thyroid/result/%s-%s-%s-%s-%s-%s" % (
        round(age, 2),
        gender,
        round(TSH, 2),
        round(T3, 2),
        round(TT4, 2),
        result,
        ))

