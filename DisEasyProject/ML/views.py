from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
import sys
import math
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.utils import shuffle
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["POST", "GET"])
@csrf_exempt
def submit(request):
    # do ML analysis
    dataFile = "testDataSet_no_NA.csv"
    data = np.loadtxt(dataFile, delimiter=',', skiprows=1)
    normData = []

    rlen = len(data[0])
    m = [0] * rlen
    for row in range(len(data)) :
        for col in range(len(data[row])) :
            m[col] = m[col] + np.float32(data[row][col])
    for col in range(len(data[0])) :
        m[col] = m[col]/len(data)
    s = [0] * rlen
    for row in range(len(data)) :
        for col in range(len(data[row])) :
            s[col] = s[col] + (np.float32(data[row][col]) - m[col])**2
    for col in range(len(data[0])) :
        s[col] = math.sqrt(s[col]/len(data))

    for row in range(len(data)) :
        line = []
        for col in range(len(data[row])) :
            tempval = ((data[row][col])-m[col])/(s[col]+0.0001)
            val = int(tempval*1000)
            line.append(float(val/1000))
        normData.append(line)

    X = []
    y = []
    tempData = shuffle(normData)
    for row in tempData :
        X.append(row[0:rlen-1])
        y.append(row[rlen-1])

    dlen = len(tempData)
    X_train, X_test = X[:dlen*2/3], X[dlen*2/3:]
    y_train, y_test = y[:dlen*2/3], y[dlen*2/3:]

    mlp = MLPClassifier(solver='lbfgs', alpha=1e-4, hidden_layer_sizes=(5, 5), random_state=2)

    tempfit = mlp.fit(X_train, y_train)

    # extract and convert data
    age = float(request.POST.get('age','0'))
    gender = request.POST.get('gender','')
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

    if age == 0 or gender == -1 or weight == 0 or height == 0 or gh == 0 or albumin == 0:
        return HttpResponse("Invalid Input")
    
    # example of making a prediction for a sample
    testPoint = [age, gender, weight, height, gh, albumin]
    normPoint = []
    for item in range(len(testPoint)) :
        tempval = ((testPoint[item])-m[item])/(s[item]+0.0001)
        val = int(tempval*1000)
        normPoint.append(float(val/1000))
    
    #prediction score
    result = mlp.predict_proba(np.array(normPoint).reshape(1,-1))[0][0]
    accuracy = mlp.score(X_test, y_test)
    # set values - real version will take results of analysis
    figure = random.randint(0,100)
    supplementary = random.randint(0,100)
    score = random.randint(0,100)

    return HttpResponse("/result/%s-%s" % (accuracy * 100, result * 100))
