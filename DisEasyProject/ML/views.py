from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
import sys
import math
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.utils import shuffle

def submit(request):
    # get JSON out of request (ask Lucy when you get here)
    # <code here>

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
    
    #example of making a prediction for a sample
    testPoint = [34.16666667, 87.4, 164.7, 5.2, 4.8]
    normPoint = []
    for item in range(len(testPoint)) :
        tempval = ((testPoint[item])-m[item])/(s[item]+0.0001)
        val = int(tempval*1000)
        normPoint.append(float(val/1000))
    
    #prediction score
    probability = mlp.predict_proba(np.array(normPoint).reshape(1,-1))[0][0]
    result = int(probability + 0.5)
    # set values - real version will take results of analysis
    figure = random.randint(0,100)
    supplementary = random.randint(0,100)
    score = random.randint(0,100)

    return HttpResponseRedirect("/result/%s-%s" % (probability * 100, result))
