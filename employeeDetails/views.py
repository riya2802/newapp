from django.shortcuts import render
from django.contrib.auth.models import User
from .models import country, employee,employeeFamily,employeeChildren,employeeHealth,Contact,Job,nationality
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
	checkUsername= validation_function.is_valid_username(strdata)
	if user_obj:
		return JsonResponse({'data':True})
	elif checkUsername is None:
			return JsonResponse({'data':'Invalid'})
	else:
		return JsonResponse({'data':False})

@csrf_exempt
def loginFun(request):
	print(request.method)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user_obj =User.objects.filter(username=username).first()
		# print(user_obj.username, user_obj.email)
		if user_obj is None:
			return redirect('/newapp/login')
		user = authenticate(username =user_obj.username, password= password )
		if user is not None:
			login(request,user)
			return redirect('/newapp/home')
		else:
			return render(request, 'login.html',)
	else:
		error="Method is not allow"
		return render(request,'login.html')
		#return render(request, 'error.html', {'error':error })

@csrf_exempt
def logoutFun(request):
    logout(request)
    return redirect('/newapp/login')

def home(request):
	return render(request,'home.html')

 ## --------------------------------------------------------------------------------------------------------

 # after
@csrf_exempt 
def editFun(request,employeementId):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	else:
		if request.method == "POST":
			print(employeementId)
			employee_obj =employee.objects.filter(employeementId = employeementId).first()
			if employee_obj  is None:
				print("user is not exist")
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
			passportcheck=passport.isalpha()
			if passportcheck :
				print('error2')
				passmsg="It takes only numeric value "
				return render(request ,'form1edit.html ',{'action':"/newapp/editFun" ,'spousepassport_error':"Only numeric values are allowed"}) 

			nationalIdcheck =nationalId.isalpha()
			if nationalIdcheck:
				print('error3')
				nationalmsg="It takes only numeric value"
				return render(request ,'form1edit.html ',{'action':"/newapp/editFun" ,'spousepassport_error':"Only numeric values are allowed"}) 
					
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
			if spousepassport is None or spousepassport =="":
				newspousepassport=None
			else:
				if spousepassport.isnumeric():
					newspousepassport=spousepassport
				else:
					print("in spousepassport")
					error ="Only numeric values are allowed "
					return render(request ,'form1edit.html ',{'action':"/newapp/editFun" ,'spousepassport_error':error}) 
			print('spousepassport-->',spousepassport, type(spousepassport),'newspousepassport',newspousepassport)
			if spousenationalId is None or spousenationalId =="":
				newspousenationalId=None
			else:
				if spousenationalId.isnumeric():
					newspousenationalId=spousenationalId
				else:
					print("in spousenationalid")
					error ="Only numeric values are allowed "
					return render(request,'form1edit.html',{'action':"/newapp/editFun",'newspousenationalId_error':error})
			print('spousenationalId-->',spousenationalId, type(spousenationalId),'newspousenationalId-->',newspousenationalId)
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
			SpouseJobStatus = request.POST.get('jobstatusdd',None)
			LeaveWorkflow = request.POST.get('leaveworkflowdd',None)
			Workdays = request.POST.get('workdays',None)
			Holidays = request.POST.get('holidaysdd',None)
			TermStart = request.POST.get('termstartdd',None)
			TermEnd = request.POST.get('termenddd',None)
			if DateJoined is not None or DateJoined != "" and Position is not None or Position != "" and JobStatusEffectiveDate is not None or JobStatusEffectiveDate != "" and EmploymentStatusEffectiveDate is not None or EmploymentStatusEffectiveDate != "":
			    if EndofProbation is not None and EndofProbation != '':
			   		newendofProbation=EndofProbation
			else:
				print("in EndofProbation")
				error= "This filed is required"
				return render(request,'form1edit.html',{'action':"/newapp/editFun",'joberror':error})
			print('newendofProbation',newendofProbation)
			Email = request.POST.get('email')
			BlogHomepage = request.POST.get('bloghomepage')
			Office = request.POST.get('office')
			OfficeExtention = request.POST.get('officeextention')
			Mobile = request.POST.get('mobile')
			print('Mobile',Mobile)
			Home = request.POST.get('home')
			print('Home',Home)
			Address1 = request.POST.get('address1')
			Address2 = request.POST.get('address2')
			City = request.POST.get('city')
			PostCode = request.POST.get('postcode')
			print('PostCode',PostCode)
			State = request.POST.get('state')
			Country = request.POST.get('countrydd')
			FirstName = request.POST.get('firstname')
			LastName = request.POST.get('lastname')
			MiddleName = request.POST.get('middlename')
			Relationship = request.POST.get('coerelationship')
			MobilePhone = request.POST.get('coemobile')
			HousePhone = request.POST.get('coehousephone')
			OfficePhone = request.POST.get('officephone')
			print(Email,"OfficePhone->", type(OfficePhone),OfficePhone,"HousePhone",HousePhone, type(HousePhone),MobilePhone,type(MobilePhone),PostCode,type(PostCode),Mobile,type(Mobile))
			if Country is not None or Country != "" and Mobile.isnumeric() and PostCode.isnumeric() and MobilePhone.isnumeric() and HousePhone.isnumeric() and OfficePhone.isnumeric():                
				res = validation_function.is_valid_phone(Office)
				if res is None or res != "errormsg":
					newOffice=res
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				res1 = validation_function.is_valid_phone(Mobile)
				if res1 is None or res1 != "errormsg":
					newMobile=res1
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				res2 = validation_function.is_valid_phone(Home)
				if res2 is None or res2 != "errormsg":
					newHome=res2
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				res3 = validation_function.is_valid_phone(MobilePhone)
				if res3 is None or res3 != "errormsg":
					newMobilePhone=res3
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				res4 = validation_function.is_valid_phone(HousePhone)
				if res4 is None or res4 != "errormsg":
					newHousePhone=res4
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				res5 = validation_function.is_valid_phone(OfficePhone)
				if res5 is None or res5 != "errormsg":
					newOfficePhone_edit=res5
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
				
				email_check = validation_function.is_valid_email(Email)
				if email_check is None or email_check != "errormsg":
					verifiedemail=email_check
				else:
					return render(request,'form1edit.html',{'contact_officeerror':"Enter valid number"})
			height=	request.POST.get('height',None)
			weight=request.POST.get('weight',None)
			bloodGroup=	request.POST.get('bloodgroup',None)
			print('newOffice---->',newOffice,'newMobile--->',newMobile,'newOfficePhone_edit-->',newOfficePhone_edit,'newPostCode---->',newPostCode,'newMobilePhone--->',newMobilePhone,'HousePhone-->',newHousePhone)
			employeeHealth.objects.filter(employeeForeignId=employee_obj).update(employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)
			Contact.objects.filter(employeeForeignId=employee_obj).update(email=verifiedemail,blogHomepage=BlogHomepage,office=newOffice,officeExtention=OfficeExtention,mobile=newMobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=newPostCode,state=State,country=Country, firstName=FirstName,lastName=LastName,middleName=MiddleName,relationship=Relationship,mobilePhone=newMobilePhone,housePhone=HousePhone,officePhone=newOfficePhone_edit)
			employee.objects.filter(employeementId=employee_obj).update(employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=newpassport,employeeEthnicity=ethnicity,employeeReligion=religion, employeePhoto=photo)
			employeeFamily.objects.filter(employeeForeignId=employee_obj).update(employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousedob,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=newspousenationalId,employeeFamilySpousePassport=newspousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
			Job.objects.filter(employeeForeignId=employee_obj).update(dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=SpouseJobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		
			for i in range(len(query_dict_childfirstname)):
				newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
				# employeeChildren.objects.bulk_update([employeeForeignId=employee_obj,[employeeChildrenFirstName=query_dict_childfirstname[i]],[employeeChildrenMiddelName=query_dict_childmiddlename[i]],[employeeChildrenLastName=query_dict_childlastname[i]],[employeeChildrenBirthDate=newchildbirthdate],[employeeChildrenGender=query_dict_childgender[i]],[employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]]])

##function for calling edit html form with data in text box 
def editHtmlForm(request,employeementId):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	objEmployeePersonal=employee.objects.filter(employeementId = employeementId).first()
	nationalityList = nationality.objects.filter(status="isactive")
	countryList = country.objects.filter(status="isactive")
	print('nationality ',objEmployeePersonal.employeeNationality)
	if objEmployeePersonal:
		objEmployeeFamily=employeeFamily.objects.filter(employeeForeignId=objEmployeePersonal)
		objEmployeeChildren=employeeChildren.objects.filter(employeeForeignId=objEmployeePersonal)
		objEmployeeHealth=employeeHealth.objects.filter(employeeForeignId=objEmployeePersonal)
		objEmployeeJob=Job.objects.filter(employeeForeignId=objEmployeePersonal)
		objEmployeeContact=Contact.objects.filter(employeeForeignId=objEmployeePersonal)
		objList= [objEmployeePersonal,objEmployeeFamily,objEmployeeChildren,objEmployeeHealth,objEmployeeJob,objEmployeeContact]
		print("objEmployeeJob",objEmployeeJob)
		
		# print("objEmployeeJob",dateJoined)
		return render(request,'form1edit.html',{'nationalityList':nationalityList,'action':"/newapp/editFun",'objEmployeePersonal':objEmployeePersonal,'objEmployeeFamily':objEmployeeFamily,'objEmployeeChildren':objEmployeeChildren,'objEmployeeHealth':objEmployeeHealth,'objEmployeeJob':objEmployeeJob,'objEmployeeContact':objEmployeeContact})
		# return render(request,'editform.html',{'obj':objList})
	else:
		return render(request,'error.html',{'error':'User not exist'})

##add new employee
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
		# employeeObj= employee.objects.filter(employeementId = employeeId).first()#check username is exist or not  
		# print(employeeObj)
		# if employeeObj:
		# 	print('error1')
		# 	return render(request, 'form.html',{'error':'user already exist'})#user already exist
		passportcheck=passport.isalpha()
		if passportcheck :
			print('error2')
			passmsg="It takes only numeric value "
			return render(request, 'form.html',{'passmsg':passmsg })
		elif passport == "":
			passport =None
		else:
			passport = passport

		print('passport',passport)
		nationalIdcheck =nationalId.isalpha()
		if nationalIdcheck:
			print('error3')
			nationalmsg="It takes only numeric value"
			return render(request, 'form.html',{'nationalmsg':nationalmsg })
		elif nationalId =="":
			nationalId = None
		else:
			nationalId =nationalId
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
		 
		
## show list of all employee
def employeeList(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	employeeObj= employee.objects.all()
	if employeeObj is None:## if no employee is addedd
		return render(request, 'Employee.html',{'form':form})
	return render(request, 'list.html',{'employeeObj':employeeObj})

def emplyeeDelete(request,employeementId ):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	emp_object = employee.objects.filter(employeementId=employeementId).first()
	if emp_object is None :
		return render(request,'Employee.html')
	employee.objects.filter(employeementId=employeementId).delete()
	return redirect('/newapp/employeeList')

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
        
