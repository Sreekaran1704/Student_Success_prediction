from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def result(request):

    cls = joblib.load('finalized_model.sav')

    lis = []


    lis.append(request.POST.get("Application_mode"))
    lis.append(request.POST.get("Application_order"))
    lis.append(request.POST.get("Course"))
    lis.append(request.POST.get("Previous_qualification_(grade)"))
    lis.append(request.POST.get("Nationality"))
    lis.append(request.POST.get("Mothers_qualification"))
    lis.append(request.POST.get("Fathers_qualification"))
    lis.append(request.POST.get("Mothers_occupation"))
    lis.append(request.POST.get("Fathers_occupation"))
    lis.append(request.POST.get("Admission_grade"))
    lis.append(request.POST.get("Displaced"))
    lis.append(request.POST.get("Educational_special_needs"))
    lis.append(request.POST.get("Debtor"))
    lis.append(request.POST.get("Tuition_fees_up_to_date"))
    lis.append(request.POST.get("Male"))
    lis.append(request.POST.get("Scholarship_holder"))
    lis.append(request.POST.get("Age_at_enrollment"))
    lis.append(request.POST.get("Curricular_units_1st_sem_(credited)"))
    lis.append(request.POST.get("Curricular_units_1st_sem_(approved)"))
    lis.append(request.POST.get("Curricular_units_1st_sem_(grade)"))
    lis.append(request.POST.get("Curricular_units_2nd_sem_(credited)"))
    lis.append(request.POST.get("Curricular_units_2nd_sem_(approved)"))
    lis.append(request.POST.get("Curricular_units_2nd_sem_(grade)"))
    lis.append(request.POST.get("Total_missed_or_dropped_units"))
    lis.append(request.POST.get("Total_failed_units"))


    ans = cls.predict([lis])
    

    return render(request, 'result.html',{'ans':ans})

