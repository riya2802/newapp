from django.shortcuts import render
from django.contrib.auth.models import User
from .models import employee,employeeFamily,employeeChildren,employeeHealth,Contact,Job
from . import personaldetails
from django.shortcuts import render, redirect
from . import validation_function
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@csrf_exempt
def isuserIdcorrect(request):
	strdata= request.POST.get('request_data')
	print('strdata',strdata)
	user_obj = employee.objects.filter(employeementId = strdata).first()
	if user_obj:
		return JsonResponse({'data':True})
	else:
		return JsonResponse({'data':False})


# def personalDetails(request):
# 	if request.method=="POST":
# 		form = personaldetails.personalDetails(request.POST,request.FILES)		 
# 		employeeId= request.POST.get('employeeid')
# 		firstName= request.POST.get('firstname',None)
# 		middelName= request.POST.get('middlename',None)
# 		lastName= request.POST.get('lastname',None)
# 		gender= request.POST.get('gender',None)
# 		birthDate= request.POST.get('birthdate',None)
# 		nationality= request.POST.get('nationality',None)
# 		passport= request.POST.get('passport',None)
# 		nationalId= request.POST.get('nationalid',None)
# 		ethnicity= request.POST.get('ethnicity',None)
# 		religion= request.POST.get('religion',None)
# 		photo=request.FILES.get('photo')
# 		print('photo',photo)
# 		#image = open('deer.gif', 'rb')
# 		if employeeId is None or employeeId ==""  or firstName is None or firstName=="" or lastName is None or lastName=="" or gender is None or gender=="" or birthDate is None or birthDate==""  or nationality=="" or nationality is None or nationalId is None or nationalId =="" :
# 			error = "This fields are required"
# 			return render(request, 'Employee.html',{'form':form,'error':error})
# 		data= employee.objects.filter(employeementId = employeeId).first()
# 		if data is not None:
# 			return render(request, 'Employee.html',{'form':form})
# 		msg = "Available"
# 		employeeUID = employee.objects.filter(employeeNationalId=nationalId).first()
# 		if employeeUID is not None:
# 			return render(request, 'Employee.html',{'form':form})
# 		passportcheck=passport.isalpha()
# 		if passportcheck :
# 			passmsg="It takes only numeric value "
# 			return render(request, 'Employee.html',{'form':form},{'passmsg':passmsg })
# 		nationalIdcheck =nationalId.isalpha()
# 		if nationalIdcheck:
# 			nationalmsg="It takes only numeric value "
# 			return render(request, 'Employee.html',{'form':form},{'nationalmsg':nationalmsg })
# 		employee.objects.create(employeementId=employeeId,employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
# 		return render(request, 'Employee.html',{'form':form,'msg':msg})
# 	else:
# 		print("get")
# 		form= personaldetails.personalDetails()
# 		return render(request, 'Employee.html',{'form':form,})


# def FamilyDetails(request,employeeid):
# 	if request.method=="POST":
# 		employee_obj =employee.objects.filter(employeementId = employeeid).first()
# 		obj=employeeFamily.objects.filter(employeeForeignId=employee_obj).first()
# 		familyform = personaldetails.familyDetails(request.POST) # create object of family form
# 		childform = personaldetails.childrenDetails(request.POST) #create object of children form
# 		maritalStatus=request.POST.get('maritalstatus',None)
# 		numberOfChild=request.POST.get('numbeofchild',None)
# 		spouseWorking=request.POST.get('spouseworking',None)
# 		spousefirstName= request.POST.get('spousefirstname',None)
# 		spousemiddelName= request.POST.get('spousemiddlename',None)
# 		spouselastName= request.POST.get('spouselastname',None)
# 		spousebirthDate= request.POST.get('spousebirthdate',None)
# 		spousenationality= request.POST.get('spousenationality',None)
# 		spousepassport= request.POST.get('spousepassport',None)
# 		spousenationalId= request.POST.get('spousenationalid',None)
# 		spouseethnicity= request.POST.get('spouseethnicity',None)
# 		spousereligion= request.POST.get('spousereligion',None)
# 		query_dict_childfirstname=request.POST.getlist('childfirstname')
# 		query_dict_childmiddlename=request.POST.getlist('childmiddlename')
# 		query_dict_childlastname=request.POST.getlist('childlastname')
# 		query_dict_childbirthdate=request.POST.getlist('childbirthdate')
# 		query_dict_childgender=request.POST.getlist('childgender')
# 		query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus')
# 		spousedob = validation_function.checkForNone(spousebirthDate)
# 		newspousepassport = validation_function.checkForNone(spousepassport)
# 		newspousenationalId	=validation_function.checkForNone(spousenationalId)
# 		employeeFamily.objects.create(employeeForeignId=employee_obj,employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
# 		for i in range(len(query_dict_childfirstname)):
# 			newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
# 			employeeChildren.objects.bulk_create([employeeChildren(employeeForeignId=employee_obj,employeeChildrenFirstName=query_dict_childfirstname[i],employeeChildrenMiddelName=query_dict_childmiddlename[i],employeeChildrenLastName=query_dict_childlastname[i],employeeChildrenBirthDate=newchildbirthdate,employeeChildrenGender=query_dict_childgender[i],employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]),])
# 		healthform= personaldetails.healthDetails()
# 		return render(request,"health.html",{'healthform':healthform})
# 	else:
# 		familyform = personaldetails.familyDetails()
# 		childform = personaldetails.childrenDetails()
# 		return render(request,"Family.html",{'familyform':familyform,'childform':childform})

# def HealthDetails(request,employeeid):
# 	if request.method== "POST":
# 		employee_obj =employee.objects.filter(employeementId = employeeid).first()
# 		check_user = employeeHealth.objects.filter(employeeForeignId=employee_obj)
# 		if check_user:
# 			return redirect('/newapp/persoanldetails' )
# 		healthform = personaldetails.healthDetails(request.POST)
# 		height=	request.POST.get('height',None)
# 		weight=request.POST.get('weight',None)
# 		bloodGroup=	request.POST.get('bloodgroup',None) 
# 		employeeHealth.objects.create(employeeForeignId=employee_obj,employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)
# 		return render(request,"health.html",{'healthform':healthform})
# 	else:
# 		healthform = personaldetails.healthDetails()
# 		return render(request,"health.html",{'healthform':healthform})

@csrf_exempt
def loginFun(request):
	print(request.method)
	if request.method =="POST":
		login_form=personaldetails.login_class(request.POST)
		username = request.POST.get('username')
		password = login_form['password'].value()
		user_obj =User.objects.filter(username=username).first()
		if user_obj is None:
			redirect('/login')
		user = authenticate(username =user_obj.username, password= password )
		if user is not None:
   			login(request,user)
   			return redirect('/newapp/persoanldetails')
		else:
			login_form = personaldetails.login_class()
			return render(request, 'login.html', {'form': login_form})
	else:
		login_form = personaldetails.login_class()
		return render(request, 'login.html', {'form': login_form})

@csrf_exempt
def logoutFun(request):
    logout(request)
    return redirect('/register/login')

# @csrf_exempt
# def editFun(request)
# 	if not request.user.is_authenticated:
# 		return redirect('/newapp/login')
# 	else:
# 		if request.method == "POST":
# 			employee_obj =employee.objects.filter(employeementId = employeeid).first()
#             if employee_obj  is None:
#             	return redirect('/newapp/login')
# 			firstName= request.POST.get('firstname',None)
# 			middelName= request.POST.get('middlename',None)
# 			lastName= request.POST.get('lastname',None)
# 			gender= request.POST.get('gender',None)
# 			birthDate= request.POST.get('birthdate',None)
# 			nationality= request.POST.get('nationality',None)
# 			passport= request.POST.get('passport',None)
# 			nationalId= request.POST.get('nationalid',None)
# 			ethnicity= request.POST.get('ethnicity',None)
# 			religion= request.POST.get('religion',None)
# 			photo=request.FILES.get('photo')
#             maritalStatus=request.POST.get('maritalstatus',None)
# 			numberOfChild=request.POST.get('numbeofchild',None)
# 			spouseWorking=request.POST.get('spouseworking',None)
# 			spousefirstName= request.POST.get('spousefirstname',None)
# 			spousemiddelName= request.POST.get('spousemiddlename',None)
# 			spouselastName= request.POST.get('spouselastname',None)
# 			spousebirthDate= request.POST.get('spousebirthdate',None)
# 			spousenationality= request.POST.get('spousenationality',None)
# 			spousepassport= request.POST.get('spousepassport',None)
# 			spousenationalId= request.POST.get('spousenationalid',None)
# 			spouseethnicity= request.POST.get('spouseethnicity',None)
# 			spousereligion= request.POST.get('spousereligion',None)
# 			query_dict_childfirstname=request.POST.getlist('childfirstname')
# 			query_dict_childmiddlename=request.POST.getlist('childmiddlename')
# 			query_dict_childlastname=request.POST.getlist('childlastname')
# 			query_dict_childbirthdate=request.POST.getlist('childbirthdate')
# 			query_dict_childgender=request.POST.getlist('childgender')
# 			query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus')
# 			spousedob = validation_function.checkForNone(spousebirthDate)
# 			newspousepassport = validation_function.checkForNone(spousepassport)
# 			newspousenationalId	=validation_function.checkForNone(spousenationalId)
# 			DateJoined = request.POST.get('datejoin')
#             EndofProbation = request.POST.get('endofprobation')
#             Position = request.POST.get('positiondd')
#             JobStatusEffectiveDate = request.POST.get('jobstatuseffectivedate')
#             LineManager = request.POST.get('linemanagedd')
#             Department = request.POST.get('departmentdd')
#             Branch = request.POST.get('branchdd')
#             Level = request.POST.get('leveldd')
#             JobType = request.POST.get('jobtypedd')
#             EmploymentStatusEffectiveDate = request.POST.get('employmentstatuseffectivedate')
#             JobStatus = request.POST.get('jobstatusdd')
#             LeaveWorkflow = request.POST.get('leaveworkflowdd')
#             Workdays = request.POST.get('workdays')
#             Holidays = request.POST.get('holidaysdd')
#             TermStart = request.POST.get('termstartdd')
#             TermEnd = request.POST.get('termenddd')
#             if DateJoined is not None or DateJoined != "" and Position is not None or Position != "" and JobStatusEffectiveDate is not None or JobStatusEffectiveDate != "" and EmploymentStatusEffectiveDate is not None or EmploymentStatusEffectiveDate != "":
#                 if EndofProbation is not None and EndofProbation != '':
#                		endofProbation=EndofProbation
#             Email = request.POST.get('email')
#             BlogHomepage = request.POST.get('bloghomepage')
#             Office = request.POST.get('office')
#             OfficeExtention = request.POST.get('officeextention')
#             Mobile = request.POST.get('mobile')
#             Home = request.POST.get('home')
#             Address1 = request.POST.get('address1')
#             Address2 = request.POST.get('address2')
#             City = request.POST.get('city')
#             PostCode = request.POST.get('postcode')
#             State = request.POST.get('state')
#             Country = request.POST.get('countrydd')
#             FirstName = request.POST.get('firstname')
#             LastName = request.POST.get('lastname')
#             MiddleName = request.POST.get('middlename')
#             Relationship = request.POST.get('relationship')
#             MobilePhone = request.POST.get('mobilephone')
#             HousePhone = request.POST.get('housephone')
#             OfficePhone = request.POST.get('officephone')
# 			if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():                
#                 if Office is not None and Office != '':
#                     Office =Office
#                 if Mobile is not None and Mobile != '':
#                     Mobile =Mobile
#                 if Home is not None and Home != '':
#                    	PostCode =PostCode
#                 if MobilePhone is not None and MobilePhone != '':
#                     MobilePhone=MobilePhone
#                 if HousePhone is not None and HousePhone != '':
#                     HousePhone =HousePhone
#                 if OfficePhone is not None and OfficePhone != '':
#                     OfficePhone =OfficePhone
#             Contact.objects.filter(employeeForeignId=employee_obj).update(email=Email,blogHomepage=BlogHomepage,office=Office,officeExtention=OfficeExtention,mobile=Mobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=PostCode,state=State,country=Country,  firstName=FirstName,lastName=LastName,middleName=MiddleName,relationship=Relationship,mobilePhone=MobilePhone,housePhone=HousePhone,officePhone=OfficePhone)
#             employee.objects.filter(employeementId=employee_obj).update(employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
# 			employeeFamily.objects.filter(employeeForeignId=employee_obj).update(employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
# 			for i in range(len(query_dict_childfirstname)):
# 				newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
# 				employeeChildren.objects.bulk_create([employeeChildren(employeeForeignId=employee_obj,employeeChildrenFirstName=query_dict_childfirstname[i],employeeChildrenMiddelName=query_dict_childmiddlename[i],employeeChildrenLastName=query_dict_childlastname[i],employeeChildrenBirthDate=newchildbirthdate,employeeChildrenGender=query_dict_childgender[i],employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]),])
# 			Job.objects.filter(employeeForeignId=employee_obj).update(dateJoined=DateJoined,endofProbation=EndofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=jobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		

# @csrf_exempt
# def forgotPassword(request):
#     username = request.POST.get('username', None)
#     if username is None or username == '':
#         return redirect('/newapp/login')
#     user= User.objects.filter(username=username).first()
#     if user is None :
#         return render(request,'login.html',{''})
#     else:
#         if user.userMetaEmailVerified is not None:
#             mailsend.forgotMail(user)
#             return Response({'message': 'Reset Link send successfully '})
#         else:
#             return Response({'message': 'Email verification Fail'},status= HTTP_400_BAD_REQUEST)

#befor
 ## --------------------------------------------------------------------------------------------------------

 # after

def editFun(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	else:
		if request.method == "POST":
			employee_obj =employee.objects.filter(employeementId = employeeid).first()
			if employee_obj  is None:
				return render(request,'error.html',{'error':'User not exist'})
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
			query_dict_childfirstname=request.POST.getlist('childfirstname')
			query_dict_childmiddlename=request.POST.getlist('childmiddlename')
			query_dict_childlastname=request.POST.getlist('childlastname')
			query_dict_childbirthdate=request.POST.getlist('childbirthdate')
			query_dict_childgender=request.POST.getlist('childgender')
			query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus')
			spousedob = validation_function.checkForNone(spousebirthDate)
			newspousepassport = validation_function.checkForNone(spousepassport)
			newspousenationalId	=validation_function.checkForNone(spousenationalId)
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
			if DateJoined is not None or DateJoined != "" and Position is not None or Position != "" and JobStatusEffectiveDate is not None or JobStatusEffectiveDate != "" and EmploymentStatusEffectiveDate is not None or EmploymentStatusEffectiveDate != "":
			    if EndofProbation is not None and EndofProbation != '':
			   		newendofProbation=EndofProbation
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
			if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():                
				if Office is not None and Office != '':
				    newOffice =Office
				if Mobile is not None and Mobile != '':
				    newMobile =Mobile
				if Home is not None and Home != '':
				   	newPostCode =PostCode
				if MobilePhone is not None and MobilePhone != '':
				    newMobilePhone=MobilePhone
				if HousePhone is not None and HousePhone != '':
				    newHousePhone =HousePhone
				if OfficePhone is not None and OfficePhone != '':
				        newOfficePhone =OfficePhone
			height=	request.POST.get('height',None)
			weight=request.POST.get('weight',None)
			bloodGroup=	request.POST.get('bloodgroup',None) 
			employeeHealth.objects.filter(employeeForeignId=employee_obj).update(employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)
			Contact.objects.filter(employeeForeignId=employee_obj).update(email=Email,blogHomepage=BlogHomepage,office=newOffice,officeExtention=OfficeExtention,mobile=newMobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=newPostCode,state=State,country=Country,  firstName=FirstName,lastName=LastName,middleName=MiddleName,relationship=Relationship,mobilePhone=newMobilePhone,housePhone=HousePhone,officePhone=newOfficePhone)
			employee.objects.filter(employeementId=employee_obj).update(employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
			employeeFamily.objects.filter(employeeForeignId=employee_obj).update(employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
			# for i in range(len(query_dict_childfirstname)):
			# 	newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
			# 	# employeeChildren.objects.bulk_update([employeeForeignId=employee_obj,[employeeChildrenFirstName=query_dict_childfirstname[i]],[employeeChildrenMiddelName=query_dict_childmiddlename[i]],[employeeChildrenLastName=query_dict_childlastname[i]],[employeeChildrenBirthDate=newchildbirthdate],[employeeChildrenGender=query_dict_childgender[i]],[employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]]])
			Job.objects.filter(employeeForeignId=employee_obj).update(dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=jobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		

##function for calling edit html form with data in text box 
def editHtmlForm(request,employeeid):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	objEmployeePersonal=employee.objects.filter(employeementId = employeeid).first()
	if objEmployee:
		objEmployeeFamily=mployeeFamily.objects.filter(employeeForeignId=employee_obj)
		objEmployeeChildren=employeeChildren.objects.filter(employeeForeignId=employee_obj)
		objEmployeeHealth=employeeHealth.objects.filter(employeeForeignId=employee_obj)
		objEmployeeJob=Job.objects.filter(employeeForeignId=employee_obj)
		objEmployeeContact=Contact.objects.filter(employeeForeignId=employee_obj)
		return render(request,'editform.html',{'objEmployeePersonal':objEmployeePersonal,'objEmployeeFamily':objEmployeeFamily,'objEmployeeChildren':objEmployeeChildren,'objEmployeeHealth':objEmployeeHealth,'objEmployeeJob':objEmployeeJob,'objEmployeeContact':objEmployeeContact})
	else:
		return render(request,'error.html',{'error':'User not exist'})

##add new employee
@csrf_exempt
def addFun(request):
	if request.method=="POST":
		print("post")		 
		employeeId= request.POST.get('employeeid')
		fname= request.POST['fname']
		print(fname)
		firstName= request.POST.get('fname',None)
		print('firstName',firstName)
		middelName= request.POST.get('middlename',None)
		lastName= request.POST.get('lname',None)
		gender= request.POST.get('gender',None)
		birthDate= request.POST.get('birthdate',None)
		nationality= request.POST.get('nationality',None)
		passport= request.POST.get('passport',None)
		nationalId= request.POST.get('nationalid',None)
		ethnicity= request.POST.get('ethnicity',None)
		religion= request.POST.get('religion',None)
		photo=request.FILES.get('photo')
		print('employeeId',employeeId)
		if employeeId is None or employeeId ==""  or firstName is None or firstName=="" or lastName is None or lastName=="" or gender is None or gender=="" or birthDate is None or birthDate==""  or nationality=="" or nationality is None or nationalId is None or nationalId =="" :
			error = "This field is required"
			print(employeeId)
			print(firstName)
			print(lastName)
			print(gender)
			print(nationalId)
			print(nationality)
			return render(request, 'form.html',{'error':error})
		employeeObj= employee.objects.filter(employeementId = employeeId).first()#check username is exist or not  
		# if employeeObj is not None and employeeObj != "":
		# 	return render(request, 'form.html',{'form':form})#user already exist
		#employeeNationalID = employee.objects.filter(employeeNationalId=nationalId).first()
		# if employeeNationalID is not None:
		# 	return render(request, 'form.html',{'form':form})#user already exist
		passportcheck=passport.isalpha()
		if passportcheck :
			passmsg="It takes only numeric value "
			return render(request, 'Employee.html',{'form':form},{'passmsg':passmsg })
		nationalIdcheck =nationalId.isalpha()
		if nationalIdcheck:
			nationalmsg="It takes only numeric value"
			return render(request, 'Employee.html',{'form':form},{'nationalmsg':nationalmsg })
		# employeeFamilyObj=employeeFamily.objects.filter(employeeForeignId=employeeObj).first()#check user is exist in family table
		# if employeeFamilyObj is not None :
		# 	return render(request, 'form.html')
		print('personal done')
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
		query_dict_childfirstname=request.POST.getlist('childfirstname')
		query_dict_childmiddlename=request.POST.getlist('childmiddlename')
		query_dict_childlastname=request.POST.getlist('childlastname')
		query_dict_childbirthdate=request.POST.getlist('childbirthdate')
		query_dict_childgender=request.POST.getlist('childgender')
		query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus')
		spousedob = validation_function.checkForNone(spousebirthDate)
		newspousepassport = validation_function.checkForNone(spousepassport)
		newspousenationalId	=validation_function.checkForNone(spousenationalId)
		#employeeHealthObj= employeeHealth.objects.filter(employeeForeignId=employeeObj)#check user is exist in Health table
		# if employeeHealthObj is not None :
		# 	print('health')
		# 	print('employeeHealthObj',employeeHealthObj)
		# 	return render(request, 'form.html')
		height=	request.POST.get('height',None)
		weight=request.POST.get('weight',None)
		bloodGroup=	request.POST.get('bloodgroup',None)
		# employeeJobObj= Job.objects.filter(employeeForeignId=employeeObj)#check user is exist in Job table
		# if employeeJobObj is not None:
		# 	print("job")
		# 	return render(request, 'form.html')
		print('family done')
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
			if EndofProbation is not None and EndofProbation != '':
				newendofProbation=EndofProbation
		# employeeContactObj=Contact.objects.filter(employeeForeignId=employeeObj)
		# if employeeContactObj is not None:
		# 	return render(request, 'Employee.html',{'form':form})
		print('Job done')
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
		if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():                
			if Office is not None and Office != '':
				newOffice =Office
			else:newOffice=None
			if Mobile is not None and Mobile != '':
			    newMobile =Mobile
			else:newMobile=None
			if Home is not None and Home != '':
			   	newPostCode =PostCode
			else:newPostCode=None
			if MobilePhone is not None and MobilePhone != '':
			    newMobilePhone=MobilePhone
			else:newMobilePhone=None
			if HousePhone is not None and HousePhone != '':
			    newHousePhone =HousePhone
			else:newHousePhone=None
			if OfficePhone is not None and OfficePhone != '':
			    newOfficePhone =OfficePhone
			else:newOfficePhone=None
		print('Contact done')
		obj = employee.objects.create(employeementId=employeeId,employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
		employeeHealth.objects.create(employeeForeignId=obj,employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)	
		employeeFamily.objects.create(employeeForeignId=obj,employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
		inser_list=[]
		for i in range(len(query_dict_childfirstname)):
			newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
			inser_list.append(employeeChildren(employeeForeignId=obj,employeeChildrenFirstName=query_dict_childfirstname[i],employeeChildrenMiddelName=query_dict_childmiddlename[i],employeeChildrenLastName=query_dict_childlastname[i],employeeChildrenBirthDate=newchildbirthdate,employeeChildrenGender=query_dict_childgender[i],employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]),)
			employeeChildren.objects.bulk_create(inser_list)
		Job.objects.create(employeeForeignId=obj,dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=jobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		
		Contact.objects.create(employeeForeignId=obj,email=Email,blogHomepage=BlogHomepage,office=newOffice,officeExtention=OfficeExtention,mobile=newMobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=newPostCode,state=State,country=Country,  firstName=FirstName,lastName=LastName,middleName=MiddleName,relationship=Relationship,mobilePhone=newMobilePhone,housePhone=HousePhone,officePhone=newOfficePhone)
		return redirect('/newapp/login')
	else: 
		print("get")
		 
		
## show list of all employee
def employeeList(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	employeeObj= employee.objects.all()
	if employeeObj is None:## if no employee is addedd
		return render(request, 'Employee.html',{'form':form})
	return render(request, 'list.html',{'employeeObj':employeeObj})

def emplyeeDelete(request,employeeid ):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	emp_object = employee.objects.filter(employeementId=employeeId).first()
	if emp_object is None :
		return render(request,'Employee.html')
	employee.objects.filter(employeementId=employeeId).delete()
	return render(request, 'list.html')

def addEmployee(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	action = "addFun"
	return render(request,'form.html' , {'action':action})

# @csrf_exempt
# def forgotPassword(request):
#     username = request.POST.get('username', None)
#     if username is None or username == '':
#         return redirect('/newapp/login')
#     user= User.objects.filter(username=username).first()
#     if user is None :
#         return render(request,'login.html')
#     else:
# 		return render(request, 'newpassword.html' )
        


## addFunDuplicate or addFunCopy
@csrf_exempt
def addFun(request,):
	if not request.user.is_authenticated:
		print("no one is login")
		return redirect('/newapp/login')
	if request.method=="POST":
		print("post")		 
		employeeId= request.POST.get('employeeid')
		print(employeeId)
		firstName= request.POST.get('firstname',None)
		print(firstName)
		middelName= request.POST.get('middlename',None)
		print(middelName)
		lastName= request.POST.get('lastname',None)
		print(lastName)
		gender= request.POST.get('gendern',None)
		print(gender)
		birthDate= request.POST.get('birthdate',None)
		print(birthDate)
		nationality= request.POST.get('nationalitydd',None)
		print(nationality)
		passport= request.POST.get('passport',None)
		print(passport)
		nationalId= request.POST.get('nationalid',None)
		print(nationalId)
		ethnicity= request.POST.get('ethnicity',None)
		religion= request.POST.get('religion',None)
		photo=request.FILES.get('photo')
		if employeeId is None or employeeId ==""  or firstName is None or firstName=="" or lastName is None or lastName=="" or gender is None or gender=="" or birthDate is None or birthDate==""  or nationality=="" or nationality is None or nationalId is None or nationalId =="" :
			print('error')
			return render(request, 'form.html', {'errorrequired':"This field is required"})
		try:
			employeeObj= employee.objects.filter(employeementId = employeeId).first() 
		except:
			if employeeObj:
				print('error1')
				return render(request, 'form.html',{'error':'user already exist'})
		else:
			if employeeObj:
				print('error1')
				return render(request, 'form.html',{'error':'user already exist'})

		validate_username = validation_function.is_valid_username(employeeId)
		if validate_username is None: ## true when name contain spaces
			return render(request,'form.html',{'username_errorq':'Enter Valid user name'})
		validfirstname=validation_function.check_is_valid_name(firstName)
		if 	validfirstname is None : 
			return render(request, 'form.html',{'firstname_error':'Invalid name' })
		validlastname=validation_function.check_is_valid_name(lastName)
		if 	validlastname is None : 
			return render(request, 'form.html',{'lastname_error':'Invalid name' })
		validmiddelname=validation_function.check_is_valid_name(middelName)
		if 	validmiddelname is None : 
			return render(request, 'form.html',{'middelname_error':'Invalid  name' })		
		# passport validation
		if str(passport).isnumeric():
		    if len(str(passport)) == 12:
		        passport=passport
		        print(passport)
            else:
		       	passportmsg="Invalid number"
		       	print(passportmsg)
                return render(request, 'form.html',{'passportmsg':passportmsg })
		elif passport== "":
		    passport = None
		else:
		    passportmsg="Enter number"
		    print(nationalmsg)
		    return render(request, 'form.html',{'passportmsg':passportmsg })
		## national validation
		if str(nationalId).isnumeric()
			if len(str(nationalId)) == 8 :
				nationalId =nationalId
			else: 
				nationalmsg="Enter valid number"
				print(nationalmsg)
				return render(request, 'form.html',{'nationalmsg':nationalmsg })
		elif nationalId =="":
				nationalId = None
		else:
			print('error3')
    		nationalmsg="It takes only numeric value"
    		print(nationalmsg)
			return render(request, 'form.html',{'nationalmsg':nationalmsg })
		print('personal done')
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
		query_dict_childfirstname=request.POST.getlist('childfirstname')
		print(query_dict_childfirstname)
		query_dict_childmiddlename=request.POST.getlist('childmiddlename')
		print(query_dict_childmiddlename)
		query_dict_childlastname=request.POST.getlist('childlastname')
		print('query_dict_childlastname',query_dict_childlastname)
		query_dict_childbirthdate=request.POST.getlist('childbirthdate')
		print('query_dict_childbirthdate',query_dict_childbirthdate)
		query_dict_childgender=request.POST.getlist('childgender')
		print('query_dict_childbirthdate',query_dict_childbirthdate)
		query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus')
		print('query_dict_childmaritalstatus',query_dict_childmaritalstatus)
		spousedob = validation_function.checkForNone(spousebirthDate)
		validspousefirstname=validation_function.check_is_valid_name(spousefirstName)
		if 	validspousefirstname is None : 
			return render(request, 'form.html',{'spousefirstname_error':'Invalid name' })
		validspouselastname=validation_function.check_is_valid_name(spouselastName)
		if 	validspouselastname is None : 
			return render(request, 'form.html',{'spouselastname_error':'Invalid name' })
		validspousemiddelname=validation_function.check_is_valid_name(spousemiddelName)
		if 	validspousemiddelname is None : 
			return render(request, 'form.html',{'spousemiddelname_error':'Invalid  name' })

		# if spousepassport is not None and spousepassport.isalpha():
		# 		#newspousepassport=spousepassport.isalpha()
		# 	print('spousepassport',spousepassport,'spousenationalId',spousenationalId)
		# 		#if newspousepassport :
		# 	print('error4')
		# 	passmsg="It takes only numeric value "
		# 	return render(request, 'form.html',{'passmsg':passmsg })
		# elif spousepassport is not None and spousepassport.isnumeric():
		# 	spousepassport=spousepassport
		# else:
		# 	spousepassport = None

		# if spousenationalId is not None and  spousenationalId.isalpha():
		# 	print('error5')
		# 	nationalmsg="It takes only numeric value"
		# 	return render(request, 'form.html',{'nationalmsg':nationalmsg })
		# if spousenationalId is not None and  spousenationalId.isnumeric():
		# 	spousenationalId=spousenationalId
		# else:
		# 	spousenationalId = None	
		spousepassportcheck=spousepassport.isalpha()
		if spousepassportcheck :
			print('error4')
			passmsg="It takes only numeric value "
			return render(request, 'form.html',{'passmsg':passmsg })
		elif spousepassport =="":
			spousepassport = None
		else:
			spousepassport =spousepassport

		spousenationalIdcheck =spousenationalId.isalpha()
		if spousenationalIdcheck:
			print('error5')
			nationalmsg="It takes only numeric value"
			return render(request, 'Employee.html',{'nationalmsg':nationalmsg })
		elif spousenationalId =="":
			spousenationalId = None
		else:
			spousenationalId =spousenationalId
		print('personal done')
		height=	request.POST.get('height',None)
		weight=request.POST.get('weight',None)
		bloodGroup=	request.POST.get('bloodgroup',None)
		print('family done')
		DateJoined = request.POST.get('datejoin',None)
		EndofProbation = request.POST.get('endofprobation',None)
		Position = request.POST.get('positiondd',None)
		JobStatusEffectiveDate = request.POST.get('jobstatuseffectivedate',None)
		LineManager = request.POST.get('linemanagedd',None)
		Department = request.POST.get('departmentdd',None)
		Branch = request.POST.get('branchdd',None)
		Level = request.POST.get('leveldd',None)
		JobType = request.POST.get('jobtypedd',None)
		EmploymentStatusEffectiveDate = request.POST.get('employmentstatuseffectivedate',None)
		JobStatus = request.POST.get('jobstatusdd',None)
		LeaveWorkflow = request.POST.get('leaveworkflowdd',None)
		Workdays = request.POST.get('workdays',None)
		Holidays = request.POST.get('holidaysdd',None)
		TermStart = request.POST.get('termstartdd',None)
		TermEnd = request.POST.get('termenddd',None)
		print(DateJoined,EndofProbation,Position,JobStatusEffectiveDate,LineManager,Department,Branch,Level,JobType,EmploymentStatusEffectiveDate,JobStatus,LeaveWorkflow,Workdays,Holidays,TermStart,TermEnd)
		if DateJoined is not None or DateJoined != "" and Position is not None or Position != "" and JobStatusEffectiveDate is not None or JobStatusEffectiveDate != "" and EmploymentStatusEffectiveDate is not None or EmploymentStatusEffectiveDate != "":
			newendofProbation=validation_function.checkForNone(EndofProbation)
		else:
			error6 = "This field is required"
			print('error6')
			return render(request,'form.html',{'error6':error6})
		print('Job done')
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
		Relationship = request.POST.get('coerelationship')
		MobilePhone = request.POST.get('coemobile')
		HousePhone = request.POST.get('coehousephone')
		OfficePhone = request.POST.get('officephone')
		if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():                
			print("valiate contact fields")
			# newOffice =validation_function.is_valid_phone(Office)
			# print('Office',Office)
			# print('newOffice',newOffice)
			# newMobile =validation_function.is_valid_phone(Mobile)
			# print('newMobile',newMobile)
			
			# newMobilePhone=validation_function.is_valid_phone(str(MobilePhone))
			# newHousePhone =validation_function.is_valid_phone(str(HousePhone))
			# newOfficePhone =validation_function.is_valid_phone(str(OfficePhone))
			# validEmail=validation_function.is_valid_email(Email)
			# if validEmail is None:
			# 	emailfild=None
			# elif validEmail :
			# 	emailfild=Email
			# else:
			# 	print("error7")
			# 	return render(request, 'form.html',{'emailerror':'Invalid Email'})
			# if newOffice is None:
			# 	officefield=None
			# elif newOffice:
			# 	officefield=Office
			# else:
			# 	print("error8")
			# 	return render(request, 'form.html',{'mobileerror':"Invalid Mobile no"})

			# if newMobile is None:
			# 	mobilefield=None
			# elif newMobile:
			# 	mobilefield=mobile
			# else:
			# 	print("error9")
			# 	return render(request,'form.html',{'mobileerror':"Invalid Mobile no  "})
			# if newMobilePhone is None:
			# 	mobilePhonefield=None
			# elif newMobilePhone:
			# 	mobilePhonefield=mobilephone
			# else:
			# 	print("error10")
			# 	return render(request, 'form.html',{'mobileerror':"Invalid Mobile no "})
			# if newHousePhone is None:
			# 	housephonefield=None
			# elif newHousePhone:
			# 	housephonefield=housephone
			# else:
			# 	print("error11")
			# 	return render(request, 'form.html',{'mobileerror':"Invalid Mobile no  "})
			# if newOfficePhone is None:
			# 	officephonefield=None
			# elif newOfficePhone:
			# 	officephonefield=officephone
			# else:
			# 	print("error12")
			# 	return render('request', form.html,{'mobileerror':"Invalid Mobile no "})
			res = validation_function.is_valid_phone(str(Office))
			if res is None or res != "errormsg" :
				officefield=res
				print(officefield, res)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			res1 = validation_function.is_valid_phone(str(Mobile))
			if res1 is None or res1 != "errormsg":
				mobilefield=res1
				print(mobilefield,res1)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			res2 = validation_function.is_valid_phone(str(Home))
			if res2 is None or res2 != "errormsg":
				home=res2
				print(home,res2)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			res3 = validation_function.is_valid_phone(str(MobilePhone))
			if res3 is None or res3 != "errormsg":
				mobilePhonefield=res3
				print(mobilePhonefield,res3)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			res4 = validation_function.is_valid_phone(str(HousePhone))
			if res4 is None or res4 != "errormsg":
				housephonefield=res4
				print(housephonefield,res4)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			res5 = validation_function.is_valid_phone(str(OfficePhone))
			if res5 is None or res5 != "errormsg":
				officephonefield=res5
				print(officephonefield,res5)
			else:
				return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			
			email_check = validation_function.is_valid_email(Email)
			if email_check is None or email_check != "errormsg":
				emailfild=email_check
				print(emailfild,email_check)
			else:
				return render(request,'form.html',{'contact_officeerror':"Enter valid number"})
			
			newPostCode =validation_function.checkForNone(PostCode)
			print('newPostCode',newPostCode)
		print('Contact done')
		obj = employee.objects.create(employeementId=employeeId,employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
		employeeHealth.objects.create(employeeForeignId=obj,employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)	
		employeeFamily.objects.create(employeeForeignId=obj,employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=spousenationalId ,employeeFamilySpousePassport=spousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
		insert_list=[]
		print("obj", obj)
		for i in range(len(query_dict_childfirstname)):
			newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
			insert_list.append(employeeChildren(employeeForeignId=obj,employeeChildrenFirstName=query_dict_childfirstname[i],employeeChildrenMiddelName=query_dict_childmiddlename[i],employeeChildrenLastName=query_dict_childlastname[i],employeeChildrenBirthDate=newchildbirthdate,employeeChildrenGender=query_dict_childgender[i],employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]),)
		employeeChildren.objects.bulk_create(insert_list)
		print('insert_list',insert_list)
		Job.objects.create(employeeForeignId=obj,dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=JobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		
		Contact.objects.create(employeeForeignId=obj,email=emailfild,blogHomepage=BlogHomepage,office=officefield,officeExtention=OfficeExtention,mobile=mobilefield,home=Home,address1=Address1,address2=Address2,city=City,postCode=newPostCode,state=State,country=Country,  firstName=FirstName,lastName=LastName,middleName=MiddleName,relationship=Relationship,mobilePhone=mobilePhonefield,housePhone=housephonefield,officePhone=officephonefield)
		return redirect('/newapp/home')
	else: 
		print("get")




# @csrf_exempt
# def forgotPassword(request):
#     username = request.POST.get('username', None)
#     if username is None or username == '':
#         return redirect('/newapp/login')
#     user= User.objects.filter(username=username).first()
#     if user is None :
#         return render(request,'login.html')
#     else:
# 		return render(request, 'newpassword.html' )