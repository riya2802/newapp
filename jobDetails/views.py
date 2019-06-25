from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from . models import Job, Contact
#from . forms import ImageForm
from django.core.files.storage import FileSystemStorage
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def job(request):
	try:
		print("we are in the job function")
		if request.method=='POST':

			DateJoined = request.POST.get('datejoin')
			EndofProbation = request.POST.get('endofprobation')
			Position = request.POST.get('positiondd')
			JobStatusEffectiveDate = request.POST.get('jobstatuseffectivedate')
			LineManager = request.POST.get('linemanagedd')
			Department = request.POST.get('departmentdd')
			Branch = request.POST.get('branchdd')
			Level = request.POST.get('leveldd')
			JobType = request.POST.get('jobtypedd')
			EmploymentStatusEffectiveDate = request.POST.get('employmentstatuseffectivedate')
			JobStatus = request.POST.get('jobstatusdd')
			LeaveWorkflow = request.POST.get('leaveworkflowdd')
			Workdays = request.POST.get('workdays')
			Holidays = request.POST.get('holidaysdd')
			TermStart = request.POST.get('termstartdd')
			TermEnd = request.POST.get('termenddd')
			print(DateJoined,EndofProbation,Position,JobStatusEffectiveDate,LineManager,Department,Branch,Level,JobType,EmploymentStatusEffectiveDate,JobStatus,LeaveWorkflow,Workdays,Holidays,TermStart,TermEnd)
			if DateJoined is not None or DateJoined != "" and Position is not None or Position != "" and JobStatusEffectiveDate is not None or JobStatusEffectiveDate != "" and EmploymentStatusEffectiveDate is not None or EmploymentStatusEffectiveDate != "":
				print("hi am assigning value")
				jobobj = Job()
				print(jobobj, "this is the job object")
				jobobj.dateJoined =DateJoined
				if EndofProbation is not None and EndofProbation != '':
					print('in')
					jobobj.endofProbation=EndofProbation
				jobobj.position =Position
				jobobj.jobStatusEffectiveDate =JobStatusEffectiveDate
				jobobj.lineManager =LineManager
				jobobj.department =Department
				jobobj.branch =Branch
				jobobj.level =Level
				jobobj.jobType=JobType
				jobobj.employmentStatusEffectiveDate =EmploymentStatusEffectiveDate
				jobobj.jobStatus =JobStatus
				jobobj.leaveWorkflow =LeaveWorkflow
				jobobj.workdays =Workdays
				jobobj.holidays =Holidays
				jobobj.termStart =TermStart
				jobobj.termEnd =TermEnd
				jobobj.save()
				print('data is saved')
			else:
				print('data is not saved')
				# return redirect('newapp/job')
		return render(request,'JOB.html')
	except Exception as e:
		print(e,"error")
		messages.error(request, 'Fill the date')
		storage = messages.get_messages(request)
		storage.used = True
		# msg="fill"
		return render(request,'JOB.html')

def contact(request):
	try:
		print("we are in the contact function")
		if request.method=='POST':

			Email = request.POST.get('email')
			BlogHomepage = request.POST.get('bloghomepage')
			Office = request.POST.get('office')
			OfficeExtention = request.POST.get('officeextention')
			Mobile = request.POST.get('mobile')
			Home = request.POST.get('home')
			Address1 = request.POST.get('address1')
			Address2 = request.POST.get('address2')
			City = request.POST.get('city')
			PostCode = request.POST.get('postcode')
			State = request.POST.get('state')
			Country = request.POST.get('countrydd')
			FirstName = request.POST.get('firstname')
			LastName = request.POST.get('lastname')
			MiddleName = request.POST.get('middlename')
			Relationship = request.POST.get('relationship')
			MobilePhone = request.POST.get('mobilephone')
			HousePhone = request.POST.get('housephone')
			OfficePhone = request.POST.get('officephone')
			print(Email,BlogHomepage,Office,OfficeExtention,Mobile,Home,Address1,Address2,City,PostCode,State,Country,FirstName,LastName,MiddleName,Relationship,MobilePhone,HousePhone,OfficePhone)
			if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():				
				print("hi am assigning value")
				contactobj = Contact()
				contactobj.email =Email
				contactobj.blogHomepage =BlogHomepage
				contactobj.office =Office
				contactobj.officeExtention =OfficeExtention
				contactobj.mobile =Mobile
				contactobj.home =Home
				contactobj.address1 =Address1
				contactobj.address2 =Address2
				contactobj.city=City
				contactobj.postCode =PostCode
				contactobj.state =State
				contactobj.country =Country
				contactobj.firstName =FirstName
				contactobj.lastName =LastName
				contactobj.middleName =MiddleName
				contactobj.relationship =Relationship
				contactobj.mobilePhone =MobilePhone
				contactobj.housePhone =HousePhone
				contactobj.officePhone =OfficePhone
				contactobj.save()
				print('data is saved')
			else:
				print('data is not saved')
				# return redirect('newapp/job')
		return render(request,'Contact.html')
	except Exception as e:
		print(e,"error")
		messages.error(request, 'enter numeric values')
		storage = messages.get_messages(request)
		storage.used = True
		# msg="fill"
		return render(request,'Contact.html')