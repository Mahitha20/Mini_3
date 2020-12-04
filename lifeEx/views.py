from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Home


def home(request):
    form=Home()
    return render(request, 'home.html', {'form':form})

def result(request):
    if(request.method=='POST'):
        form=Home(request.POST)
        if form.isvalid():
            Year = request.GET['Year']
            Status= request.GET['Status']
            Adult_Mortality = request.GET['Adult_Morality']
            Infant_deaths = request.GET['Infant_deaths']
            Alcohol = request.GET['Alcohol']
            Expenditure= request.GET['Expenditure']
            Hepatitis_b=request.GET['Hepatitis_b']
            Measles = request.GET['Measles']
            BMI = request.GET['BMI']
            Under_five_deaths = request.GET['Under_five_deaths']
            Polio = request.GET['Polio']
            Total_expenditure = request.GET['Total_expenditure']
            Diphtheria = request.GET['Diphtheria']
            HIV_AIDS = request.GET['HIV_AIDS']
            GDP = request.GET['GDP']
            Population = request.GET['Population']
            Thinness_19_years = request.GET['Thinness_19_years']
            Thinness_9_years = request.GET['Thinness_9_years']
            Income_Composition = request.GET['Income_Composition']
            Schooling = request.GET['Schooling']

        result = predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b,
                             Measles, BMI, Under_five_deaths, Polio, Total_expenditure, Diphtheria, 
                             HIV_AIDS, GDP, Population, Thinness_19_years, Thinness_9_years,
                              Income_Composition, Schooling)

    return render(request, 'result.html', {'result':result})

def predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b, Measles, BMI, 
            Under_five_deaths, Polio, Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,
             Thinness_19_years, Thinness_9_years, Income_Composition, Schooling):
    import pickle
    import model
    input_model= pickle.loads(model)
    prediction = input_model.predict(sc.transform([[Year, Status, Adult_Mortality, Infant_deaths, 
                        Alcohol, Expenditure, Hepatitis_b, Measles, BMI, Under_five_deaths, Polio, 
                        Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,Thinness_19_years,
                         Thinness_9_years, Income_Composition, Schooling]]))
    return prediction







