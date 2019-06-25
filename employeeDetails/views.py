from django.shortcuts import render
from .models import employee
from . import personaldetails
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def personalDetails(request):
	if request.method=="POST":
		form = personaldetails.personalDetails(request.POST,request.FILES)		 
		employeeId= request.POST.get('employeeid')
		firstName= request.POST.get('firstname',None)
		middelName= request.POST.get('middlename',None)
		lastName= request.POST.get('lastname',None)
		gender= request.POST.get('gender',None)
		birthDate= request.POST.get('birthdate',None)
		nationality= request.POST.get('nationality',None)
		passport= request.POST.get('passport',None)
		nationalId= request.POST.get('nationalid',None)
		ethnicity= request.POST.get('ethnicity',None)
		religion= request.POST.get('religion',None)
		photo=request.FILES.get('photo')
		if employeeId is None or employeeId ==""  or firstName is None or firstName=="" or lastName is None or lastName=="" or gender is None or gender=="" or birthDate is None or birthDate==""  or nationality=="" or nationality is None or nationalId is None or nationalId =="" :
			error = "This fields are required"
			return render(request, 'Employee.html',{'form':form,'error':error})
		data= employee.objects.filter(employeementId = employeeId).first()
		if data is not None:
			return render(request, 'Employee.html',{'form':form})
		msg = "Available"
		employeeUID = employee.objects.filter(employeeNationalId=nationalId).first()
		if employeeUID is not None:
			return render(request, 'Employee.html',{'form':form})
		passportcheck=passport.isalpha()
		if passportcheck :
			passmsg="It takes only numeric value "
			return render(request, 'Employee.html',{'form':form},{'passmsg':passmsg })
		nationalIdcheck =nationalId.isalpha()
		if nationalIdcheck:
			nationalmsg="It takes only numeric value "
			return render(request, 'Employee.html',{'form':form},{'nationalmsg':nationalmsg })
		employee.objects.create(employeementId=employeeId,employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
		return render(request, 'Employee.html',{'form':form,'msg':msg})
	else:
		print("get")
		form= personaldetails.personalDetails()
		return render(request, 'Employee.html',{'form':form,})

