from django.shortcuts import render
from .models import employee,employeeFamily,employeeChildren,employeeHealth
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
import re
def get_html_input_dict(query_dict, param):
        dictionary = {}
        regex = re.compile('%s\[([\w\d_]+)\]' % param)
        for key, value in query_dict.items():
            match = regex.match(key)
            if match:
                inner_key = match.group(1)
                dictionary[inner_key] = value                
        return dictionary

def FamilyDetails(request,employeeid):
	if request.method=="POST":
		familyform = personaldetails.familyDetails(request.POST) # create object of family form
		childform = personaldetails.childrenDetails(request.POST) #create object of children form
		employee_obj =employee.objects.filter(employeementId = employeeid).first()
		maritalStatus=request.POST.get('maritalstatus',None)
		numberOfChild=request.POST.get('numbeofchild',None)
		spouseWorking=request.POST.get('spouseworking',None)
		spousefirstName= request.POST.get('spousefirstname',None)
		spousemiddelName= request.POST.get('spousemiddlename',None)
		spouselastName= request.POST.get('spouselastname',None)
		spousebirthDate= request.POST.get('spousebirthdate',None)
		spousenationality= request.POST.get('spousenationality',None)
		spousepassport= request.POST.get('spousepassport',None)
		spousenationalId= request.POST.get('spousenationalid',None)
		spouseethnicity= request.POST.get('spouseethnicity',None)
		spousereligion= request.POST.get('spousereligion',None)
		if spousebirthDate is not None and spousebirthDate !="" and spousenationalId is not None and spousenationalId !="" and spousepassport is not None and spousepassport !="":
			print("in ")
			spousedob = spousebirthDate
			newspousepassport = spousepassport
			newspousenationalId	=spousenationalId
		else:
			spousedob = None
			newspousepassport= None
			newspousenationalId=None
		employeeFamily.objects.create(employeeForeignId=employee_obj,employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
		childFirstName= request.POST.get('childfirstname',None)
		print('childFirstName',childFirstName)
		childMiddelName= request.POST.get('childmiddlename',None)
		print('childMiddelName',childMiddelName)
		childLastName= request.POST.get('childlastname',None)
		print('childLastName',childLastName)
		childBirthDate= request.POST.get('childbirthdate',None)
		print('childBirthDate',childBirthDate)
		childGender= request.POST.get('childgender',None)
		print('childGender',childGender)
		childMaritalStatus=request.POST.get('childmaritalstatus',None)
		print('childMaritalStatus',childMaritalStatus)
		query_dict=request.POST.getlist('childfirstname[]')
		print('dic',len(query_dict),query_dict)
		healthform= personaldetails.healthDetails()
		return render('request','health.html',{'healthform',healthform} )
	else:
		familyform = personaldetails.familyDetails()
		childform = personaldetails.childrenDetails()
		return render(request,"Family.html",{'familyform':familyform,'childform':childform})

def HealthDetails(request,employeeid):
	if request.method== "POST":
		employee_obj =employee.objects.filter(employeementId = employeeid).first()
		check_user = employeeHealth.objects.filter(employeeForeignId=employee_obj)
		if check_user:
			return redirect('/newapp/persoanldetails' )
		healthform = personaldetails.healthDetails(request.POST)
		height=	request.POST.get('height',None)
		weight=request.POST.get('weight',None)
		bloodGroup=	request.POST.get('bloodgroup',None) 
		employeeHealth.objects.create(employeeForeignId=employee_obj,employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)
		return render(request,"health.html",{'healthform':healthform})
	else:
		healthform = personaldetails.healthDetails()
		return render(request,"health.html",{'healthform':healthform})

