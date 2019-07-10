from django.shortcuts import render
from django.contrib.auth.models import User
from .models import numberOfChild, maritalStatus,bloodGroup,department, branch, position,level,lineManager, holiDays,leaveWorkFlow,workDays,jobStatus, jobType, religion, ethnicity, country, employee,employeeFamily,employeeChildren,employeeHealth,Contact,Job,nationality
from . import personaldetails
from django.shortcuts import render, redirect
from . import validation_function
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from datetime import date,datetime
from django.contrib.auth import authenticate, login, logout
import json
from django.core.paginator import Paginator
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
import reportlab
from django.template.loader import get_template
from . import createpdf
from createpdf import render_to_pdf

# accept ajax request to check username is valid
@csrf_exempt
def isuserIdcorrect(request):
	strdata= request.POST.get('request_data')
	print('strdata',strdata)
	print("requestcome")
	user_obj = employee.objects.filter(employeementId = strdata).first()
	checkUsername= validation_function.is_valid_username(strdata)
	if user_obj:
		return JsonResponse({'data':True})
	elif checkUsername is None:
			return JsonResponse({'data':False})
	else:
		return JsonResponse({'data':False})

@csrf_exempt
def loginFun(request):
	print(request.method)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user_obj =User.objects.filter(username=username).first()
		if user_obj is None:
			return redirect('/newapp/login')
		user = authenticate(username =user_obj.username, password= password )
		if not user:
			return render(request, 'login.html',)
		login(request,user)
		return redirect('/newapp/home')
		# print(request.user.username)
		# return JsonResponse({'msg':'login user','status':200})
	else:
		error="Method is not allow"
		return render(request,'login.html')
		#return render(request, 'error.html', {'error':error })

@csrf_exempt
def logoutFun(request):
    logout(request)
    return redirect('/newapp/home')

def home(request):
	if not request.user.is_authenticated:
		return render(request,'home.html',{'login_button_url':'/newapp/login','button_text':'Login'})
	return render(request,'home.html',{'login_button_url':'/newapp/logout','button_text':'Logout'})

 ## --------------------------------------------------------------------------------------------------------
#persondetails validation 
@csrf_exempt
def personalAjaxRequest(request):
	# if not request.user.is_authenticated:
	# 	print('not authenticate')
	# 	#return redirect('/newapp/login')
	# 	return JsonResponse({'msg':'User is not authenticated','status':400})
	print(request.POST)
	if request.method == "POST":
		employeementId= request.POST.get('employeeid',None)
		print('employeementId',employeementId)
		firstName= request.POST.get('firstname',None)
		print('firstName',firstName)
		middelName= request.POST.get('middlename',None)
		print('middelName',middelName)
		lastName= request.POST.get('lastname',None)
		print('lastName',lastName)
		gender= request.POST.get('gendern',None)
		print('gender',gender)
		birthDate= request.POST.get('birthdate',None)
		print('birthDate',birthDate)
		print('birthDate',birthDate, type(birthDate))
		nationality= request.POST.get('nationalitydd',None)
		print('nationality',nationality)
		passport= request.POST.get('passport')
		print('passport',passport)
		nationalId= request.POST.get('nationalid',None)
		print('nationalId',nationalId)
		ethnicity= request.POST.get('ethnicity',None)
		print('ethnicity',ethnicity)
		religion= request.POST.get('religion',None)
		print('religion',religion)
		photo=request.FILES.get('image')

		print('photo',photo)
		print("passport",passport)
		print('nationalId',nationalId)
		print('middelName',middelName)
		if employeementId is None or employeementId ==""  or firstName is None or firstName=="" or lastName is None or lastName=="" or gender is None or gender=="" or birthDate is None or birthDate==""  or nationality=="" or nationality is None or nationalId is None or nationalId =="" :
			print('employeementId',employeementId,'firstName',firstName,'lastName',lastName,'gender',gender,'birthDate',birthDate,'nationality',nationality,'nationalId',nationalId)
			return JsonResponse({'msg':'Required fields empty !','status':400})
		if not validation_function.check_employeeId(employeementId):
			return JsonResponse({'msg':'Invalid Id , Id should be numeric ','status':400})
		if not validation_function.check_is_valid_name(firstName) :
			return JsonResponse({'msg':'Invalid First name !','status':400})
		if not validation_function.check_is_valid_name(middelName):
			return JsonResponse({'msg':'Invalid Middle Name !','status':400})
		if not validation_function.check_is_valid_name(lastName):
			return JsonResponse({'msg':'Invalid Last Name !','status':400})
		if not validation_function.is_date(birthDate):
			return JsonResponse({'msg':'Invalid Date Format !','status':400})
		if validation_function.calculateAge(datetime.strptime(birthDate, '%Y-%m-%d')) < 18 :
			return JsonResponse({'msg':'Your age is less then 18 years !','status':400})
		if not validation_function.is_valid_passport(passport):
			return JsonResponse({'msg':' passport no is not valid !','status':400})
		if not validation_function.is_valid_national(nationalId):
			return JsonResponse({'msg':' National no is not valid !','status':400})
		employee_obj =employee.objects.filter(employeementId = employeementId,status='Success').first()#check request is comming for edit user details
		print('employee_obj',employee_obj)
		if employee_obj:
			employee_obj.employeeFirstName=firstName
			employee_obj.employeeMiddelName=middelName
			employee_obj.employeeLastName=lastName
			employee_obj.employeeGender=gender
			employee_obj.employeeBirthDate=birthDate
			employee_obj.employeeNationality=nationality
			employee_obj.employeeNationalId=nationalId
			employee_obj.employeePassport=passport
			employee_obj.employeeEthnicity=ethnicity
			employee_obj.employeeReligion=religion
			# employee_obj.employeePhoto=photo
			employee_obj.status="Pending"
			employee_obj.save()
			old_image_Name = employee_obj.employeePhoto
			if 'image' in request.FILES:
				employee_obj.employeePhoto=photo
			else:
				employee_obj.employeePhoto=old_image_Name
			employee_obj.save()
			return JsonResponse({'msg':'success','status':200,'empID':employee_obj.employeeId})
		updateobj = employee.objects.filter(employeementId = employeementId,status='Pending').first()
		if updateobj:
			# old_image_Name = employee_obj.employeePhoto
			# if 'image' in request.FILES:
			# 	updateobj.employeePhoto=photo
			# else:
			# 	updateobj.employeePhoto=old_image_Name
			updateobj.employeeFirstName=firstName
			updateobj.employeeMiddelName=middelName
			updateobj.employeeLastName=lastName
			updateobj.employeeGender=gender
			updateobj.employeeBirthDate=birthDate
			updateobj.employeeNationalId=nationalId
			updateobj.employeeNationality=nationality
			updateobj.employeePassport=passport
			updateobj.employeeEthnicity=ethnicity
			updateobj.employeeReligion=religion
			updateobj.employeePhoto=photo
			updateobj.status="Pending"
			updateobj.save()
			# if 'image' in request.FILES:
			# 	employee_obj.employeePhoto=photo
			# else:
			# 	employee_obj.employeePhoto=old_image_Name
			# employee_obj.save()
			print('updateobj.employeeFirstName',updateobj.employeeId)
			print(type(updateobj))
			print("updateobj.employeeId",updateobj.employeeId)
			return JsonResponse({'msg':'success','status':200,'empID':updateobj.employeeId})
		obj_E = employee.objects.create(employeementId=employeementId,employeeFirstName=firstName,employeeMiddelName=middelName,employeeLastName=lastName,employeeGender=gender,employeeBirthDate=birthDate,employeeNationality=nationality,employeeNationalId=nationalId,employeePassport=passport,employeeEthnicity=ethnicity,employeeReligion=religion,employeePhoto=photo,status="Pending")		
		print('empID',obj_E.employeeId)
		return JsonResponse({'msg':'success','status':200,'empID':obj_E.employeeId})

#------------------------------------------------------
@csrf_exempt
def familyAjaxRequest(request):
	# if not request.user.is_authenticated:
	# 	return redirect('/newapp/login')
	print(request.POST.get('data[empid]'))
	if request.method == "POST":
		employee_empid=request.POST.get('data[empid]',None)
		print('employee_empid',employee_empid)
		print('request.POST',request.POST)
		obj =employee.objects.filter(employeeId = employee_empid).first()
		if not obj:
				return JsonResponse({'msg':'Id not exist!','status':400}) 
		maritalStatus=request.POST.get('data[maritalstatus]',None)
		print('maritalStatus',maritalStatus)
		numberOfChild=request.POST.get('data[numberofchild]',None)

		print('numberOfChild',numberOfChild,type(numberOfChild))
		spouseWorking=request.POST.get('data[spouseworking]',None)
		print('spouseWorking',spouseWorking)
		spousefirstName= request.POST.get('data[spousefirstname]',None)
		print('spousefirstName',spousefirstName)
		spousemiddelName= request.POST.get('data[spousemiddlename]',None)
		print('spousemiddelName',spousemiddelName)
		spouselastName= request.POST.get('data[spouselastname]',None)
		print('spouselastName',spouselastName)
		spousebirthDate= request.POST.get('data[spousebirthdate]',None)
		print('spousebirthDate',spousebirthDate)
		print('spousebirthDate',spousebirthDate,type(spousebirthDate))
		spousenationality= request.POST.get('data[spousenationality]',None)
		print('spousenationality',spousenationality)
		spousepassport= request.POST.get('data[spousepassport]')
		print('spousepassport',spousepassport)
		spousenationalId= request.POST.get('data[spousenationalid]')
		print('spousenationalId',spousenationalId)
		spouseethnicity= request.POST.get('data[spouseethnicity]',None)
		print('spouseethnicity',spouseethnicity)
		spousereligion= request.POST.get('data[spouserelegion]',None)
		print('spousereligion',spousereligion)
		if not employee_empid:
			return JsonResponse({'msg':' Employee Id field Empty!','status':400})
		# if spousenationality is None or spousenationality =="":
		# 	return JsonResponse({'msg':' spouse Nationality number is Required field !','status':400})
		if not validation_function.check_is_valid_name(spousefirstName) :
			print("error1")
			return JsonResponse({'msg':'First name only takes alphabets !','status':400})
		if not validation_function.check_is_valid_name(spousemiddelName):
			print("error2")
			return JsonResponse({'msg':'Middle Name name only takes alphabets !','status':400})
		if not validation_function.check_is_valid_name(spouselastName):
			print("error3")
			return JsonResponse({'msg':'Last name only takes alphabets !','status':400})
		if spousebirthDate is not None and spousebirthDate != '':
			spousebirthDate=spousebirthDate
		else:
			spousebirthDate=None
		if not validation_function.is_valid_passport(spousepassport):
			print("error5")
			return JsonResponse({'msg':' passport no is not valid !','status':400})
		if spousenationalId == None or spousenationalId =="":
			spousenationalId = spousenationalId
		else:
			if not validation_function.is_valid_national(spousenationalId):
				print("error6")
				return JsonResponse({'msg':' national ID is not valid !','status':400})
		print('maritalStatus',maritalStatus,'numberOfChild',numberOfChild,'spouseWorking',spouseWorking,'spousefirstName',spousefirstName,'spousemiddelName')
				#if numberOfChild > 0 and maritalStatus == "Merried":
		# query_dict_childkey = request.POST.getlist('childkey[]')

		query_dict_childfirstname=request.POST.getlist('childfirstname[]')
		query_dict_childmiddlename=request.POST.getlist('childmiddlename[]')
		query_dict_childlastname=request.POST.getlist('childlastname[]')
		query_dict_childbirthdate=request.POST.getlist('childbirthdate[]')
		query_dict_childgender=request.POST.getlist('childgender[]')
		query_dict_childmaritalstatus=request.POST.getlist('childmaritalstatus[]')
		print("check")
		print('query_dict_childfirstname',query_dict_childfirstname)
		print('query_dict_childmiddlename',query_dict_childmiddlename)
		print('query_dict_childmiddlename',query_dict_childmiddlename)
		print('query_dict_childbirthdate',query_dict_childbirthdate)
		print('query_dict_childgender',query_dict_childgender)
		print('query_dict_childmaritalstatus',query_dict_childmaritalstatus)
		insert_list=[]
		check_child = employeeChildren.objects.filter(employeeForeignId=obj)
		for i in range(len(query_dict_childfirstname)):
			if check_child :
				print(check_child)
				employeeChildren.objects.filter(employeeForeignId=obj).delete()
			print(query_dict_childfirstname[i])
			newchildbirthdate = validation_function.checkForNone(query_dict_childbirthdate[i])
			if not validation_function.check_is_valid_name(query_dict_childfirstname[i]) :
				return JsonResponse({'msg':' child First name only takes alphabets !','status':400})
			if not validation_function.check_is_valid_name(query_dict_childmiddlename[i]):
				return JsonResponse({'msg':' childMiddle Name name only takes alphabets !','status':400})
			if not validation_function.check_is_valid_name(query_dict_childlastname[i]):
				return JsonResponse({'msg':'childLast name only takes alphabets !','status':400}) 
			insert_list.append(employeeChildren(employeeForeignId=obj,employeeChildrenFirstName=query_dict_childfirstname[i],employeeChildrenMiddelName=query_dict_childmiddlename[i],employeeChildrenLastName=query_dict_childlastname[i],employeeChildrenBirthDate=newchildbirthdate,employeeChildrenGender=query_dict_childgender[i],employeeChildrenMaritalStatus=query_dict_childmaritalstatus[i]),)
		employeeChildren.objects.bulk_create(insert_list)
		print('insert_list',insert_list)

		checkEmployee =employeeFamily.objects.filter(employeeForeignId = obj).update(employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousebirthDate,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=spousenationalId ,employeeFamilySpousePassport=spousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
		if checkEmployee:
			return JsonResponse({'msg':'success','status':200,'empID':employee_empid})
		employeeFamily.objects.create(employeeForeignId=obj, employeeFamilyMaritalStatus=maritalStatus,employeeFamilyNumberOfChild=numberOfChild,employeeFamilySpouseWorking=spouseWorking,employeeFamilySpouseFirstName=spousefirstName,employeeFamilySpouseMiddelName=spousemiddelName,employeeFamilySpouseLastName=spouselastName,employeeFamilySpouseBirthDate=spousebirthDate,employeeFamilySpouseNationality=spousenationality,employeeFamilySpouseNationalId=spousenationalId ,employeeFamilySpousePassport=spousepassport,employeeFamilySpouseEthnicity=spouseethnicity,employeeFamilySpouseReligion=spousereligion)
		return JsonResponse({'msg':'success','status':200,'empID':employee_empid})
#----------------------------------------------------------------
@csrf_exempt
def jobAjaxRequest(request):
	print("in")
	# if not request.user.is_authenticated:
	# 	return redirect('/newapp/login')
	if request.method == "POST":
		employeementId_obj=request.POST.get('empid')
		print('employeementId_obj',employeementId_obj)
		if not employeementId_obj:
			return JsonResponse({'msg':' emplaoyee Id field Empty!','status':400})
		obj =employee.objects.filter(employeeId = employeementId_obj).first()
		if not obj:
				return JsonResponse({'msg':'Id not exist!','status':400}) 
		print('request.POST',request.POST)
		DateJoined = request.POST.get('datejoin',None)
		print('DateJoined',DateJoined)
		EndofProbation = request.POST.get('endofprobation',None)
		print('EndofProbation',EndofProbation)
		print('EndofProbation',EndofProbation,type(EndofProbation))
		Position = request.POST.get('positiondd',None)
		print('Position',Position)
		JobStatusEffectiveDate = request.POST.get('jobstatuseffectivedate',None)
		print('JobStatusEffectiveDate',JobStatusEffectiveDate)
		print('JobStatusEffectiveDate',JobStatusEffectiveDate,type(JobStatusEffectiveDate))
		LineManager = request.POST.get('linemanagedd',None)
		print('LineManager',LineManager)
		Department = request.POST.get('departmentdd',None)
		print('Department',Department)
		Branch = request.POST.get('branchdd',None)
		print('Branch',Branch)
		Level = request.POST.get('leveldd',None)
		print('Level',Level)
		JobType = request.POST.get('jobtypedd',None)
		print('JobType',religion)
		EmploymentStatusEffectiveDate = request.POST.get('employmentstatuseffectivedate',None)
		print('EmploymentStatusEffectiveDate',EmploymentStatusEffectiveDate, type(EmploymentStatusEffectiveDate))
		JobStatus = request.POST.get('jobstatusdd',None)
		print('JobStatus',JobStatus)
		LeaveWorkflow = request.POST.get('leaveworkflowdd',None)
		print('LeaveWorkflow',LeaveWorkflow)
		Workdays = request.POST.get('workdays',None)
		print('Workdays',Workdays)
		Holidays = request.POST.get('holidaysdd',None)
		print('Holidays',Holidays)
		TermStart = request.POST.get('termstartdd',None)
		print('TermStart',TermStart)
		TermEnd = request.POST.get('termend',None)
		print('TermEnd',TermEnd)
		print('EmploymentStatusEffectiveDate',EmploymentStatusEffectiveDate,'DateJoined',DateJoined,'Position',Position,'JobStatusEffectiveDate',JobStatusEffectiveDate)
		if employeementId_obj is None or employeementId_obj=="" and DateJoined is  None or DateJoined == "" and Position is None or Position == "" and JobStatusEffectiveDate is None or JobStatusEffectiveDate == "" and EmploymentStatusEffectiveDate is None or EmploymentStatusEffectiveDate == "":		    
			return JsonResponse({'msg':'Required fields empty !','status':400})
		if EndofProbation is not None and EndofProbation != '':
			if not validation_function.end_of_probation(EndofProbation,DateJoined):
				return JsonResponse({'msg':'Invalid probation date','status':400})
			else:
				newendofProbation =	EndofProbation
		else:
			newendofProbation=None
		if not validation_function.check_join_date(DateJoined,obj.employeeBirthDate):
			return JsonResponse({'msg':'Invalid joining date','status':400})
		if not validation_function.calculate_Effective_date(JobStatusEffectiveDate):
			print("job status effective date")
			return JsonResponse({'msg':'Invalid Job  Effective date','status':400})
		if not validation_function.calculate_Effective_date(EmploymentStatusEffectiveDate):
			print("employee effective date ")
			return JsonResponse({'msg':'Invalid emplaoyee Effective date','status':400})
		checkJob =Job.objects.filter(employeeForeignId = obj).update(dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=JobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)
		if checkJob:
			return JsonResponse({'msg':'success','status':200,'empID':employeementId_obj})
		Job.objects.create(employeeForeignId=obj,dateJoined=DateJoined,endofProbation=newendofProbation,position=Position,jobStatusEffectiveDate=JobStatusEffectiveDate,lineManager=LineManager,department=Department,branch=Branch,level=Level,jobType=JobType,employmentStatusEffectiveDate=EmploymentStatusEffectiveDate,jobStatus=JobStatus,leaveWorkflow=LeaveWorkflow,workdays=Workdays,holidays=Holidays,termStart=TermStart,termEnd=TermEnd)		
		return JsonResponse({'msg':'success','status':200,'empID':employeementId_obj})
#----------------------------------------------------------------------------
@csrf_exempt
def contactAjaxRequest(request):
	# if not request.user.is_authenticated:
	# 	return redirect('/newapp/login')
	if request.method == "POST":
		employeementId_obj=request.POST.get('empid',None)
		if not employeementId_obj:
			return JsonResponse({'msg':' emplaoyee Id field Empty!','status':400})
		print('employeementId_obj',employeementId_obj)
		obj =employee.objects.filter(employeeId = employeementId_obj).first()
		print('obj',obj)
		Email = request.POST.get('email')
		print('Email',Email)
		BlogHomepage = request.POST.get('bloghomepage')
		print('BlogHomepage',BlogHomepage,type(BlogHomepage))
		Office = request.POST.get('office')
		print('Office',Office,type(Office))
		OfficeExtention = request.POST.get('officeextention')
		print('OfficeExtention',OfficeExtention,type(OfficeExtention))
		Mobile = request.POST.get('mobile')
		print('Mobile',Mobile,type(Mobile))
		Home = request.POST.get('home')
		print('Home',Home)

		Address1 = request.POST.get('address1')
		print('Address1',Address1)
		Address2 = request.POST.get('address2')
		print('Address2',Address2)
		City = request.POST.get('city')
		print('City',City)
		PostCode = request.POST.get('postcode')
		print('PostCode',PostCode,type(PostCode))
		State = request.POST.get('state')
		print('State',State)
		Country = request.POST.get('countrydd')
		print('Country',Country)
		contactFirstName = request.POST.get('coefirstname')
		print('contactFirstName',contactFirstName)
		contactLastName = request.POST.get('coelastname')
		print('contactLastName',contactLastName)
		conatctMiddleName = request.POST.get('coemiddlename')
		print('conatctMiddleName',conatctMiddleName)
		Relationship = request.POST.get('coerelationship')
		print('Relationship',Relationship)
		MobilePhone = request.POST.get('coemobile')
		print('MobilePhone',MobilePhone)
		HousePhone = request.POST.get('coehousephone')
		print('HousePhone',HousePhone)
		OfficePhone = request.POST.get('coeofficephone')
		print('OfficePhone',OfficePhone)
		print('OfficePhone',OfficePhone)
		print(Email,"OfficePhone->", type(OfficePhone),OfficePhone,"HousePhone",HousePhone, type(HousePhone),MobilePhone,type(MobilePhone),PostCode,type(PostCode),Mobile,type(Mobile))
		if Country is None or Country == ""  :                 
			return JsonResponse({'msg':'Required fields empty !','status':400})
		if not validation_function.is_valid_phone(str(Office)):
			return JsonResponse({'msg':'Invalid office Number !','status':400})
		if not validation_function.is_valid_phone(str(Mobile)):
			return JsonResponse({'msg':'Invalid Mobile Number !','status':400})
		if not validation_function.is_valid_phone(str(Home)):
			return JsonResponse({'msg':'Invalid Home Number !','status':400})
		if not validation_function.is_valid_phone(str(MobilePhone)):
			return JsonResponse({'msg':'Invalid MobilePhone Number !','status':400})
		if not validation_function.is_valid_phone(str(HousePhone)):
			return JsonResponse({'msg':'Invalid HousePhone Number !','status':400})
		if not validation_function.is_valid_phone(str(OfficePhone)):
			return JsonResponse({'msg':'Invalid OfficePhone Number !','status':400})
		if not validation_function.is_valid_phone(str(OfficeExtention)):
			return JsonResponse({'msg':'Invalid OfficeExtention Number !','status':400})
		if not validation_function.is_valid_postcode(PostCode):
			return JsonResponse({'msg':'Invalid Postcode !','status':400})
		if Email == "" or Email == None :
			Email = Email
		else:
			if not validation_function.is_valid_email(Email):
				return JsonResponse({'msg':'Invalid Email !','status':400})
			currentuseremail = Contact.objects.filter(email=Email,employeeForeignId=employeementId_obj).first()
			if not currentuseremail:
				checkDuplicateEmail=Contact.objects.filter(email=Email).first()
				if checkDuplicateEmail:
					return JsonResponse({'msg':'Email already exist !','status':400})
		if not validation_function.check_is_valid_name(contactFirstName) :
			return JsonResponse({'msg':'First name only takes alphabets !','status':400})
		if not validation_function.check_is_valid_name(contactLastName):
			return JsonResponse({'msg':'LastName name only takes alphabets !','status':400})
		if not validation_function.check_is_valid_name(conatctMiddleName):
			return JsonResponse({'msg':'Middle  name only takes alphabets !','status':400})
		checkContact =Contact.objects.filter(employeeForeignId = obj).update(email=Email,blogHomepage=BlogHomepage,office=Office,officeExtention=OfficeExtention,mobile=Mobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=PostCode,state=State,country=Country,firstName=contactFirstName,lastName=contactLastName,middleName=conatctMiddleName,relationship=Relationship,mobilePhone=MobilePhone,housePhone=HousePhone,officePhone=OfficePhone)
		if checkContact:
			return JsonResponse({'msg':'success','status':200})
		Contact.objects.create(employeeForeignId=obj,email=Email,blogHomepage=BlogHomepage,office=Office,officeExtention=OfficeExtention,mobile=Mobile,home=Home,address1=Address1,address2=Address2,city=City,postCode=PostCode,state=State,country=Country,firstName=contactFirstName,lastName=contactLastName,middleName=conatctMiddleName,relationship=Relationship,mobilePhone=MobilePhone,housePhone=HousePhone,officePhone=OfficePhone)
		return JsonResponse({'msg':'success','status':200})
#------------------------------------------------------------------------
@csrf_exempt
def healthAjaxRequest(request):
	# if not request.user.is_authenticated:
	# 	return redirect('/newapp/login')
	if request.method == "POST":
		employee_empid=request.POST.get('empid',None)
		if not employee_empid:
			return JsonResponse({'msg':' emplaoyee Id field Empty!','status':400})
		obj =employee.objects.filter(employeeId = employee_empid).first()
		height=	request.POST.get('height',None)
		print('height',height)
		weight=request.POST.get('weight',None)
		print('weight',weight)
		bloodGroup=	request.POST.get('bloodgroup',None)
		print('bloodGroup',bloodGroup)
		if not validation_function.is_valid_height(height):
			return JsonResponse({'msg':'Minimum Height should be 120 in cm and maximum should be 325 !','status':400})
		if not validation_function.is_valid_weight(weight):
			return JsonResponse({'msg':' Minimum Weight should be 25 and maximum should be 120 kg  !','status':400})
		checkhealth = employeeHealth.objects.filter(employeeForeignId = obj).update(employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)
		if checkhealth :
			return JsonResponse({'msg':'success','status':200})
		employeeHealth.objects.create(employeeForeignId=obj,employeeHealthHeight=height,employeeHealthWeight=weight,employeeHealthBloodGroup=bloodGroup)	
		return JsonResponse({'msg':'success','status':200})
#---------------------------------------------------------------------------

##function for calling edit html form with data in text box 
def editHtmlForm(request,employeeId):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	objEmployeePersonal=employee.objects.filter(employeeId = employeeId).first()
	nationalityList = nationality.objects.filter(status="isactive")
	ethnicityList=ethnicity.objects.filter(status="isactive")
	religionList=religion.objects.filter(status="isactive")
	countryList = country.objects.filter(status="isactive")
	jobTypeList=jobType.objects.all()
	jobStatusList=jobStatus.objects.all()
	workDaysList= workDays.objects.all()
	leaveWorkFlowList=leaveWorkFlow.objects.all()
	holiDaysList=holiDays.objects.all()
	lineManagerList=lineManager.objects.all()
	levelList=level.objects.all()
	positionList=position.objects.all()
	branchList=branch.objects.all()
	departmentList=department.objects.all()
	bloodGroupList = bloodGroup.objects.all()
	MaritalStatusList = maritalStatus.objects.all()
	numberofchildList=numberOfChild.objects.all()
	print('numberofchildList', numberofchildList)
	print('nationality ',objEmployeePersonal.employeeNationality)
	if objEmployeePersonal:
		objEmployeeFamily = objEmployeePersonal.employeefamily_set.all()
		objEmployeeChildren = objEmployeePersonal.employeechildren_set.all()
		objEmployeeHealth = objEmployeePersonal.employeehealth_set.all()
		objEmployeeJob = objEmployeePersonal.job_set.all()
		objEmployeeContact = objEmployeePersonal.contact_set.all()
		print("objEmployeeJob",objEmployeeJob)
		return render(request,'formedit.html',{'MaritalStatusList':MaritalStatusList,'numberofchildList':numberofchildList,'bloodGroupList':bloodGroupList,"nationalityList":nationalityList,'countryList':countryList,'ethnicityList':ethnicityList,'religionList':religionList,'workDaysList':workDaysList,'jobStatusList':jobStatusList,'jobTypeList':jobTypeList,'lineManagerList':lineManagerList,'holiDaysList':holiDaysList,'leaveWorkFlowList':leaveWorkFlowList,'departmentList':departmentList,'branchList':branchList,'positionList':positionList,'levelList':levelList
,'action':"/newapp/submit",'objEmployeePersonal':objEmployeePersonal,'objEmployeeFamily':objEmployeeFamily,'objEmployeeChildren':objEmployeeChildren,'objEmployeeHealth':objEmployeeHealth,'objEmployeeJob':objEmployeeJob,'objEmployeeContact':objEmployeeContact})
	else:
		return render(request,'error.html',{'error':'User not exist'})


##add new employee
@csrf_exempt
def submit(request):
	# if not request.user.is_authenticated:
	# 	return redirect('/login')
	employeementId_obj=request.POST.get('empid',None)
	print(employeementId_obj,employeementId_obj)
	userCheck = employee.objects.filter(employeeId = employeementId_obj,status='Pending').first()
	if not userCheck:
		print('userCheck',userCheck)
		return JsonResponse({'msg':"User Not Exist", 'status':400 })	
	#objEmployeeFamily=employeeFamily.objects.filter(employeeForeignId=userCheck)
	objEmployeeFamily=userCheck.employeefamily_set.all()
	#objEmployeeChildren=employeeChildren.objects.filter(employeeForeignId=userCheck)
	objEmployeeChildren= userCheck.employeechildren_set.all()
	#objEmployeeHealth=employeeHealth.objects.filter(employeeForeignId=userCheck)
	objEmployeeHealth=userCheck.employeehealth_set.all()
	#objEmployeeJob=Job.objects.filter(employeeForeignId=userCheck)
	objEmployeeJob=userCheck.job_set.all()
	#objEmployeeContact=Contact.objects.filter(employeeForeignId=userCheck)
	objEmployeeContact=userCheck.contact_set.all()	
	if objEmployeeFamily is None and objEmployeeChildren is None and objEmployeeHealth is None and objEmployeeJob is None and objEmployeeContact is None :
		return JsonResponse({'msg':"Data not save in the Database", 'status':400 })
	userCheck.status='Success'
	userCheck.save()
	print('Success')
	return JsonResponse({'msg':"Employee Register Successfully", 'status':200 })

## show list of all employee
def employeeList(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	employeeObj= employee.objects.filter(status='Success')
	if employeeObj is None:## if no employee is addedd
		return render(request, 'Employee.html',{'form':form})
	paginator = Paginator(employeeObj, 10) # Show 25 contacts per page
	page = request.GET.get('page')
	employee_page = paginator.get_page(page)
	return render(request, 'Listcopy.html',{'employeeObj':employee_page})

@csrf_exempt
def emplyeeDelete(request,employeementId ):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	emp_object = employee.objects.filter(employeementId=employeementId).first()
	if emp_object is None :
		return render(request,'Employee.html')
	employee.objects.filter(employeementId=employeementId).delete()
	return redirect('/newapp/employeeList')

## call html form for add new user
def addEmployee(request):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	action = "addFun"
	nationalityList = nationality.objects.filter(status="isactive")
	#countryListList = country.objects.filter(status="isactive")
	ethnicityList=ethnicity.objects.filter(status="isactive")
	religionList=religion.objects.filter(status="isactive")
	jobTypeList=jobType.objects.all()
	jobStatusList=jobStatus.objects.all()
	workDaysList= workDays.objects.all()
	leaveWorkFlowList=leaveWorkFlow.objects.all()
	holiDaysList=holiDays.objects.all()
	lineManagerList=lineManager.objects.all()
	levelList=level.objects.all()
	positionList=position.objects.all()
	branchList=branch.objects.all()
	departmentList=department.objects.all()
	bloodGroupList = bloodGroup.objects.all()
	MaritalStatusList = maritalStatus.objects.all()
	numberofchildList=numberOfChild.objects.all()
	countryList = country.objects.filter(status='isactive')
	return render(request,'form.html' , {'MaritalStatusList':MaritalStatusList,'numberofchildList':numberofchildList,'bloodGroupList':bloodGroupList,"nationalityList":nationalityList,'countryList':countryList,'ethnicityList':ethnicityList,'religionList':religionList,'workDaysList':workDaysList,'jobStatusList':jobStatusList,'jobTypeList':jobTypeList,'lineManagerList':lineManagerList,'holiDaysList':holiDaysList,'leaveWorkFlowList':leaveWorkFlowList,'departmentList':departmentList,'branchList':branchList,'positionList':positionList,'levelList':levelList
,'action':"/newapp/addFun",})


@csrf_exempt
def preview(request):
	employeementId_obj=request.POST.get('empid',None)
	obj =employee.objects.filter(employeeId = employeementId_obj).first()
	return JsonResponse({'msg':'success','status':200})


@csrf_exempt
def directory(request):
	employeementId_obj=request.POST.get('empid',None)
	obj =employee.objects.filter(employeeId = employeementId_obj).first()
	return JsonResponse({'msg':'success','status':200})

def createPdf(request,employeeId):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	objEmployeePersonal=employee.objects.filter(employeeId = employeeId).first()
	if objEmployeePersonal:
		objEmployeeFamily=employeeFamily.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeFamily',objEmployeeFamily)
		objEmployeeChildren=employeeChildren.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeChildren',objEmployeeChildren)
		objEmployeeHealth=employeeHealth.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeHealth',objEmployeeHealth)
		objEmployeeJob=Job.objects.filter(employeeForeignId=objEmployeePersonal).first()
		objEmployeeContact=Contact.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print("objEmployeeJob",objEmployeeJob)
		print('objEmployeeContact',objEmployeeContact.email)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    # Create a file-like buffer to receive PDF data.
	buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
	p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
	# dic = {"employee Id":objEmployeePersonal.employeementId,"Name":objEmployeePersonal.employeeFirstName}

	# keyList=['Emplaoyee Id', 'Name']
	# #valuelist=['employeementId','employeeBirthDate']
	# row = 750
	# keycolumn = 50
	# valuecolumn=300
	# for key in range(len(keyList)):
	# 	# 	print(valuelist[key])
	# 	# for i in range(len(valuelist)):
	# 	#print(key)
	# 	p.drawString(keycolumn,row,keyList[key]+":" )
	# 	p.drawString(valuecolumn,row,"hhcxc")
	# 	row=row-30
	p.setFont('Times-Bold',16)
	p.drawString(245,770, "Employee Details ")
	p.drawString(70,710, "Employee Id ")
	p.drawString(350,710, employeeId)
	p.drawString(70,680, "Name ")
	p.drawString(350,680,str(objEmployeePersonal.employeeFirstName+' '+objEmployeePersonal.employeeLastName).upper())
	p.drawString(70,650, "DOB ")
	p.drawString(350,650,str(objEmployeePersonal.employeeBirthDate))
	p.drawString(70,620,  "Gender")
	p.drawString(350,620,str(objEmployeePersonal.employeeGender).upper())
	p.drawString(70,590, "Nationality ")
	p.drawString(350,590, str(objEmployeePersonal.employeeNationality).upper())
	p.drawString(70,560,  "National Id")
	p.drawString(350,560,str(objEmployeePersonal.employeeNationalId))
	p.drawString(70,530, "Joining Date")
	p.drawString(350,530, str(objEmployeeJob.dateJoined))
	p.drawString(70,500,  "Email")
	p.drawString(350,500,str(objEmployeeContact.email ))
	p.drawString(70,470, "Mobile")
	p.drawString(350,470,str( objEmployeeContact.mobile))
	p.drawString(70,430,  "Country")
	p.drawString(350,430,str(objEmployeeContact.country).upper())
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    #return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

@csrf_exempt
def data(request):
	query_dict_childfirstname1=request.POST.getlist('childfirstname')
	query_dict_childfirstname3=request.POST.getlist('childfirstname[]')
	query_dict_childfirstname=request.POST.get('childfirstname[]')
	print('query_dict_childfirstname',query_dict_childfirstname)
	#len(query_dict_childfirstname))
	print('query_dict_childfirstname1',query_dict_childfirstname1)
	print(query_dict_childfirstname3)
	query_dict_childmiddelname3=request.POST.getlist('childmiddlename[]')
	query_dict_childlastname3=request.POST.getlist('childlastname[]')
	print('query_dict_childmiddelname3',query_dict_childmiddelname3)
	print('query_dict_childlastname3',query_dict_childlastname3)
	return JsonResponse({'msg':'Success','status':200 })

@csrf_exempt
def employeeView(request,employeeId, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect('/newapp/login')
	template = get_template('view_new.html')
	objEmployeePersonal=employee.objects.filter(employeeId = employeeId).first()
	if objEmployeePersonal:
		objEmployeeFamily=employeeFamily.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeFamily',objEmployeeFamily)
		objEmployeeChildren=employeeChildren.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeChildren',objEmployeeChildren)
		objEmployeeHealth=employeeHealth.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print('objEmployeeHealth',objEmployeeHealth)
		objEmployeeJob=Job.objects.filter(employeeForeignId=objEmployeePersonal).first()
		objEmployeeContact=Contact.objects.filter(employeeForeignId=objEmployeePersonal).first()
		print("objEmployeeJob",objEmployeeJob)
		print('objEmployeeContact',objEmployeeContact.email)
	context ={'objEmployeePersonal':objEmployeePersonal,'objEmployeeFamily':objEmployeeFamily,'objEmployeeChildren':objEmployeeChildren,'objEmployeeHealth':objEmployeeHealth,'objEmployeeJob':objEmployeeJob,'objEmployeeContact':objEmployeeContact}
	html = template.render(context)
	pdf= render_to_pdf('view_new.html',context)
	return HttpResponse(pdf,content_type='application/pdf')
		# return render(request,'view_new.html',{'objEmployeePersonal':objEmployeePersonal,'objEmployeeFamily':objEmployeeFamily,'objEmployeeChildren':objEmployeeChildren,'objEmployeeHealth':objEmployeeHealth,'objEmployeeJob':objEmployeeJob,'objEmployeeContact':objEmployeeContact})


    
    