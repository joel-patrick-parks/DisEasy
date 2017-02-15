from django.shortcuts import render
from django.http import HttpResponseRedirect
import random

def submit(request):
    # get JSON out of request (ask Lucy when you get here)
    # <code here>

    # do ML analysis
    # <code here>

    # set values - real version will take results of analysis
    figure = random.randint(0,100)
    supplementary = random.randint(0,100)
    score = random.randint(0,100)

    return HttpResponseRedirect("/result/%s-%s-%s" % (figure, supplementary, score))
