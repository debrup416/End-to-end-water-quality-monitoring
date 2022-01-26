from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Water
from .forms import WaterForm

import joblib

# Create your views here.



def getDataAndPredict(request):
    if request.method=='POST':
        form=WaterForm(request.POST)
        temp=[]
        dict={}
        for x in request.POST:
            print(request.POST[x])
            dict[x]=request.POST[x]
            temp.append(request.POST[x])

        temp.pop(0)
        test_data=[]
        test_data.append(temp)
        print(test_data)

        water=joblib.load("core/WATER.pkl")
        prediction=water[0].predict(test_data)
        del dict['csrfmiddlewaretoken']
        prediction=water[0].predict(test_data)
        return render(request,'core/index.html',{'form':form ,'ans':prediction[0]})

    
        

        print(dict)
    else:
        form=WaterForm()
         
    context={'form':form }
    
        
    return render(request,'core/index.html',context)


