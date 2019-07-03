# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator
# # Create your models here.
# gender = [
#         ('M' ,'Male'),
#         ('F', 'Female'),
#         ('U', 'Unknown')
#     ]
# Nationality= [
# 		('India' ,'India'),
#         ('Canada','Canada'),
# ]
# Ethnicity= [
# 		('Gernal' ,'Gernal'),
# 		('NA','NA'),

        
# ]
# Religion= [
# 		('Gernal' ,'Gernal'),																														
# 		('NA','NA'),
        
# ]
# MaritalStaus=[
# 		('Married','Married'),
# 		('UnMarried','Unmarried')
# ]
# BloodGroup=[
# 		('AN','AN'), 
# 		('AP','AP'),
# 		('B' ,'B'),		
# 		('BP','BP'),
# 		('ABN','ABN'),
# 		('ABP','ABP'),
# 		('OP','OP'),
# 		('ON',"ON"),
# 		("Don/'t know","Don/'t know")
# ]
# class employee(models.Model):
# 	employeeId= models.AutoField(primary_key=True)
# 	employeementId =models.CharField(max_length=255,null=False,blank=False,unique=True)
# 	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
# 	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
# 	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
# 	employeeGender= models.CharField(max_length=15, choices=gender, default='U',blank=False,null=False)
# 	employeeBirthDate=models.DateField(blank=False,null=False)
# 	employeeNationality=models.CharField(max_length=15, choices=Nationality, default='India',blank=False,null=False)
# 	employeeNationalId=models.IntegerField(null=False,blank=False,unique=True)
# 	employeePassport=models.IntegerField(null=True,blank=True)
# 	employeeEthnicity=models.CharField(max_length=15,choices=Ethnicity, default='NA',null=True,blank=True)
# 	employeeReligion=models.CharField(max_length=15,choices=Religion, default='NA',null=True,blank=True)
# 	employeePhoto=models.ImageField(upload_to='photo', blank=True,)

# class employeeFamily(models.Model):
# 	employeeForeignId =models.ForeignKey(employee,models.CASCADE,unique=True)
# 	employeeFamilyMaritalStatus=models.CharField(max_length=15, choices=MaritalStaus, default='Unmarried')
# 	employeeFamilyNumberOfChild= models.CharField(max_length=15,default="0")
# 	employeeFamilySpouseWorking =models.CharField(max_length=15,default='No',null=True)
# 	employeeFamilySpouseFirstName= models.CharField(max_length=255,blank=True,null=True)
# 	employeeFamilySpouseMiddelName=models.CharField(max_length=255,null=True,blank=True)
# 	employeeFamilySpouseLastName=models.CharField( max_length=255,blank=True,null=True)
# 	employeeFamilySpouseBirthDate=models.DateField(null=True)
# 	employeeFamilySpouseNationality=models.CharField(max_length=15, choices=Nationality, default='India',blank=False,null=False)
# 	employeeFamilySpouseNationalId=models.IntegerField(null=True,blank=True)
# 	employeeFamilySpousePassport=models.IntegerField(null=True,blank=True)
# 	employeeFamilySpouseEthnicity=models.CharField(max_length=15,choices=Ethnicity, default='NA',null=True,blank=True)
# 	employeeFamilySpouseReligion=models.CharField(max_length=15,choices=Religion, default='NA',null=True,blank=True)

# class employeeChildren(models.Model):
# 	employeeForeignId =models.ForeignKey(employee,models.CASCADE)
# 	employeeChildrenFirstName= models.CharField(max_length=255,blank=True,null=True)
# 	employeeChildrenMiddelName=models.CharField(max_length=255,null=True,blank=True)
# 	employeeChildrenLastName=models.CharField( max_length=255,blank=True,null=True)
# 	employeeChildrenBirthDate=models.DateField(blank=True,null=True)
# 	employeeChildrenGender= models.CharField(max_length=15, choices=gender, default='U',blank=True,null=True)
# 	employeeChildrenMaritalStatus=models.CharField(max_length=1, choices=MaritalStaus, default='Unmarried')

# class employeeHealth(models.Model):
# 	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
# 	employeeHealthHeight=models.CharField(max_length=255,blank=True,null=True)
# 	employeeHealthWeight=models.CharField(max_length=255,null=True,blank=True)
# 	employeeHealthBloodGroup=models.CharField(max_length=5, choices=BloodGroup, default="Don't No",blank=True,null=True)

# class Job(models.Model):
# 	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
# 	dateJoined = models.DateField(null=False,blank=False)
# 	endofProbation = models.DateField(null=True)
# 	position = models.CharField(max_length=30, null=False, blank=False)
# 	jobStatusEffectiveDate = models.DateField(null=False,blank=False)
# 	lineManager = models.CharField(max_length=30,null = True,blank=False)
# 	department = models.CharField(max_length=30,null = True,blank=False)
# 	branch = models.CharField(max_length=30,null = True,blank=False)
# 	level = models.CharField(max_length=30,null = True,blank=False)
# 	jobType = models.CharField(max_length=30,null = True,blank=False)
# 	employmentStatusEffectiveDate = models.DateField(null=False,blank=False)
# 	jobStatus = models.CharField(max_length=30,null = True,blank=False)
# 	leaveWorkflow = models.CharField(max_length=30,null = True,blank=False)
# 	workdays = models.CharField(max_length=30,null = True,blank=False)
# 	holidays= models.CharField(max_length=30,null = True,blank=False)
# 	termStart = models.CharField(max_length=30,null = True)
# 	termEnd = models.CharField(max_length=30,null = True)
	

# class Contact(models.Model):
# 	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
# 	email= models.EmailField(max_length=55, unique=True)
# 	blogHomepage=models.CharField(max_length=60)
# 	office=models.CharField(max_length=30,null=True)
# 	officeExtention=models.CharField(max_length=30)
# 	mobile=models.IntegerField(validators=[MaxValueValidator(11)],null=True)
# 	home=models.CharField(max_length=60,null=True)
# 	address1=models.CharField(max_length=160)
# 	address2=models.CharField(max_length=160)
# 	city =models.CharField(max_length=60)
# 	postCode=models.IntegerField(validators=[MaxValueValidator(20)],null=True)
# 	state=models.CharField(max_length=80)
# 	country=models.CharField(max_length=80, null=False)
# 	firstName=models.CharField(max_length=30)
# 	lastName=models.CharField(max_length=30)
# 	middleName=models.CharField(max_length=30)
# 	relationship=models.CharField(max_length=30)
# 	mobilePhone=models.IntegerField(validators=[MaxValueValidator(11)],null=True)
# 	housePhone=models.IntegerField(validators=[MaxValueValidator(11)],null=True)
# 	officePhone=models.IntegerField(validators=[MaxValueValidator(11)],null=True)

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
gender = [
        ('M' ,'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
Nationality= [
		('India' ,'India'),
        ('Canada','Canada'),
]
Ethnicity= [
		('Gernal' ,'Gernal'),
		('NA','NA'),

        
]
Religion= [
		('Gernal' ,'Gernal'),																														
		('NA','NA'),
        
]
MaritalStaus=[
		('Married','Married'),
		('UnMarried','Unmarried')
]
BloodGroup=[
		('AN','AN'), 
		('AP','AP'),
		('B' ,'B'),		
		('BP','BP'),
		('ABN','ABN'),
		('ABP','ABP'),
		('OP','OP'),
		('ON',"ON"),
		("Don/'t know","Don/'t know")
]
Status = [
	('isactive','isactive'),
	('notactive','notactive')
]
employeeStatus=(('Success','Success'),('Pending','Pending'))


Position=[
	('position1','position1'),
	('position2','position2'),
	('poition3','position3'),
]
class nationality(models.Model):
	nationalityName = models.CharField(max_length=30)
	status=models.CharField(max_length=30, choices=Status, default="notactive" )

class country(models.Model):
	countryName = models.CharField(max_length=30)
	countryCode= models.CharField(max_length = 30)
	status =models.CharField(max_length = 30,choices=Status,default= "notactive")
 
class ethnicity(models.Model):
	ethnicityName = models.CharField(max_length = 30,unique=True)
	status = models.CharField(choices= Status, max_length=30, null = True, blank = True)

class religion(models.Model):
	religionName = models.CharField(max_length = 30,unique=True)
	status = models.CharField(choices= Status, max_length=30, default="notactive" )

class jobType(models.Model):
	jobType=models.CharField(max_length=30,default='temporary',unique=True)
	
class jobStatus(models.Model):
	jobStatus=models.CharField(max_length=30,default='intern',unique=True)

class workDays(models.Model):
	workdays= models.CharField(max_length=30)

class leaveWorkFlow(models.Model):
	leaveworkflow= models.CharField(max_length=20)

class holiDays (models.Model):
	holidays= models.CharField(max_length=20)

class lineManager(models.Model):
	lineManagerList= models.CharField(max_length=20)

class level (models.Model):
	joblevel= models.CharField(max_length=20)

class position(models.Model):
	position= models.CharField(max_length=20)

class branch(models.Model):
	branchName = models.CharField(max_length=20)

class department(models.Model):
	branchObj = models.ForeignKey(branch,models.CASCADE)
	department =  models.CharField(max_length=20)	

class employee(models.Model):
	employeeId= models.AutoField(primary_key=True)
	employeementId =models.IntegerField(max_length=255,null=False,blank=False,unique=True)
	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
	employeeGender= models.CharField(max_length=15, choices=gender, default='U',blank=False,null=False)
	employeeBirthDate=models.DateField(blank=False,null=False)
	employeeNationality=models.CharField(max_length=15, default='India',blank=False,null=False)
	employeeNationalId=models.IntegerField(null=False,blank=False)
	employeePassport=models.IntegerField(null=True,blank=True)
	employeeEthnicity=models.CharField(max_length=15,choices=Ethnicity, default='NA',null=True,blank=True)
	employeeReligion=models.CharField(max_length=15,choices=Religion, default='NA',null=True,blank=True)
	employeePhoto=models.ImageField(upload_to='photo', blank=True,)
	status=models.CharField(max_length=30, choices=employeeStatus, default="notactive" )

class employeeFamily(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE,unique=True)
	employeeFamilyMaritalStatus=models.CharField(max_length=15, choices=MaritalStaus, default='Unmarried')
	employeeFamilyNumberOfChild= models.CharField(max_length=15,default="0",null=True)
	employeeFamilySpouseWorking =models.CharField(max_length=15,default='No',null=True)
	employeeFamilySpouseFirstName= models.CharField(max_length=255,blank=True,null=True)
	employeeFamilySpouseMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeFamilySpouseLastName=models.CharField( max_length=255,blank=True,null=True)
	employeeFamilySpouseBirthDate=models.DateField(null=True)
	employeeFamilySpouseNationality=models.CharField(max_length=15, choices=Nationality, default='India',blank=False,null=False)
	employeeFamilySpouseNationalId=models.IntegerField(null=True,blank=True)
	employeeFamilySpousePassport=models.IntegerField(null=True,blank=True)
	employeeFamilySpouseEthnicity=models.CharField(max_length=15,choices=Ethnicity, default='NA',null=True,blank=True)
	employeeFamilySpouseReligion=models.CharField(max_length=15,choices=Religion, default='NA',null=True,blank=True)

class employeeChildren(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE)
	employeeChildrenFirstName= models.CharField(max_length=255,blank=True,null=True)
	employeeChildrenMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeChildrenLastName=models.CharField( max_length=255,blank=True,null=True)
	employeeChildrenBirthDate=models.DateField(blank=True,null=True)
	employeeChildrenGender= models.CharField(max_length=15, choices=gender, default='U',blank=True,null=True)
	employeeChildrenMaritalStatus=models.CharField(max_length=1, choices=MaritalStaus, default='Unmarried')

class employeeHealth(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
	employeeHealthHeight=models.CharField(max_length=255,blank=True,null=True)
	employeeHealthWeight=models.CharField(max_length=255,null=True,blank=True)
	employeeHealthBloodGroup=models.CharField(max_length=5, choices=BloodGroup, default="Don't No",blank=True,null=True)

class Job(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
	dateJoined = models.DateField(null=False,blank=False)
	endofProbation = models.DateField(null=True)
	position = models.CharField(max_length=30, null=False, blank=False)
	jobStatusEffectiveDate = models.DateField(null=False,blank=False)
	lineManager = models.CharField(max_length=30,null = True,blank=True)
	department = models.CharField(max_length=30,null = True,blank=True)
	branch = models.CharField(max_length=30,null = True,blank=True)
	level = models.CharField(max_length=30,null = True,blank=True)
	jobType = models.CharField(max_length=30,null = True,blank=True)
	employmentStatusEffectiveDate = models.DateField(null=False,blank=True)
	jobStatus = models.CharField(max_length=30,null = True,blank=True)
	leaveWorkflow = models.CharField(max_length=30,null = True,blank=True)
	workdays = models.CharField(max_length=30,null = True,blank=True)
	holidays= models.CharField(max_length=30,null = True,blank=True)
	termStart = models.CharField(max_length=30,null = True)
	termEnd = models.CharField(max_length=30,null = True)
	

class Contact(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
	email= models.EmailField(max_length=55, unique=True, null=True	)
	blogHomepage=models.CharField(max_length=60,null=True)
	office=models.CharField(max_length=30,null=True)
	officeExtention=models.CharField(max_length=30,null=True)
	mobile=models.CharField(max_length=12,null=True,blank=True)
	home=models.CharField(max_length=60,null=True)
	address1=models.CharField(max_length=160,null=True)
	address2=models.CharField(max_length=160,null=True)
	city =models.CharField(max_length=60,null=True)
	postCode=models.CharField(max_length=12,null=True,blank=True)
	state=models.CharField(max_length=80,null=True)
	country=models.CharField(max_length=80, null=False)
	firstName=models.CharField(max_length=30,null=True)
	lastName=models.CharField(max_length=30,null=True)
	middleName=models.CharField(max_length=30,null=True)
	relationship=models.CharField(max_length=30,null=True)
	mobilePhone=models.CharField(max_length=12,null=True,blank=True)
	housePhone=models.CharField(max_length=12,null=True,blank=True)
	officePhone=models.CharField(max_length=12,null=True,blank=True)

