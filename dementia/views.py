from django.http import  HttpResponse
from django.shortcuts import render
import joblib 


def index(request):
    return render(request,"index.html")


def result(request):
    cls  = joblib.load(r'E:\django_projects\dementia_detector\random_forest_Classifier.sav')

    lis = []

    lis.append(request.GET['visit'])
    lis.append(request.GET['MR Delay'])
    lis.append(request.GET['Age'])
    lis.append(request.GET['Education'])
    lis.append(request.GET['SES'])
    lis.append(request.GET['MMSE'])
    lis.append(request.GET['CDR'])
    lis.append(request.GET['eTIV'])
    lis.append(request.GET['nWBV'])
    lis.append(request.GET['ASF'])

    
    ans = cls.predict([lis])


    return render(request,'result.html',{'ans': ans,'lis':lis})


