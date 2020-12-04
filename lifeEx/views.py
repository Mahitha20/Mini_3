from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Home

def home(request):
    form=Home()
    return render(request, 'home.html', {'form':form})

def result(request):
    if(request.method=='POST'):
        Year = request.POST['Year']
        Status= request.POST['Status']
        Adult_Mortality = request.POST['Adult_Mortality']
        Infant_deaths = request.POST['Infant_deaths']
        Alcohol = request.POST['Alcohol']
        Expenditure= request.POST['Expenditure']
        Hepatitis_b=request.POST['Hepatitis_b']
        Measles = request.POST['Measles']
        BMI = request.POST['BMI']
        Under_five_deaths = request.POST['Under_five_deaths']
        Polio = request.POST['Polio']
        Total_expenditure = request.POST['Total_expenditure']
        Diphtheria = request.POST['Diphtheria']
        HIV_AIDS = request.POST['HIV_AIDS']
        GDP = request.POST['GDP']
        Population = request.POST['Population']
        Thinness_19_years = request.POST['Thinness_19_years']
        Thinness_9_years = request.POST['Thinness_9_years']
        Income_Composition = request.POST['Income_Composition']
        Schooling = request.POST['Schooling']

    result = predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b,
                             Measles, BMI, Under_five_deaths, Polio, Total_expenditure, Diphtheria, 
                             HIV_AIDS, GDP, Population, Thinness_19_years, Thinness_9_years,
                              Income_Composition, Schooling)

    return render(request, 'result.html', {'result':result})

def predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b, Measles, BMI, 
            Under_five_deaths, Polio, Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,
             Thinness_19_years, Thinness_9_years, Income_Composition, Schooling):
    import pickle
    input_model= pickle.loads(model)
    prediction = input_model.predict(sc.transform([[Year, Status, Adult_Mortality, Infant_deaths, 
                        Alcohol, Expenditure, Hepatitis_b, Measles, BMI, Under_five_deaths, Polio, 
                        Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,Thinness_19_years,
                         Thinness_9_years, Income_Composition, Schooling]]))
    return prediction







