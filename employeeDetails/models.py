from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
gender = [
        ('M' ,'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]


Status = [
	('isactive','isactive'),
	('notactive','inactive')
]
employeeStatus=(('Success','Success'),('Pending','Pending'))

class nationality(models.Model):
	nationalityName = models.CharField(max_length=30)
	status=models.CharField(max_length=30, choices=Status, default="notactive" )

class country(models.Model):
	countryName = models.CharField(max_length=30)
	countryCode= models.CharField(max_length = 30)
	status =models.CharField(max_length = 30,choices=Status,default= "inactive")
 
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
	lineManager= models.CharField(max_length=20)

class level (models.Model):
	joblevel= models.CharField(max_length=20)

class position(models.Model):
	position= models.CharField(max_length=20)

class branch(models.Model):
	branchName = models.CharField(max_length=20)

class department(models.Model):
	branchObj = models.ForeignKey(branch,models.CASCADE)
	department =  models.CharField(max_length=20)		

class bloodGroup(models.Model):
	bloodgroup=  models.CharField(max_length=30)

class maritalStatus(models.Model):
	Maritalstatus=  models.CharField(max_length=30)

class numberOfChild(models.Model):
	numberOfchild=  models.CharField(max_length=30)

class employee(models.Model):
	employeeId= models.AutoField(primary_key=True)#primary key
	employeementId =models.IntegerField(max_length=255,null=False,blank=False,unique=True)
	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
	employeeGender= models.CharField(max_length=15, choices=gender, default='U',blank=False,null=False)
	employeeBirthDate=models.DateField(blank=False,null=False)
	employeeNationality=models.CharField(max_length=15, default='India',blank=False,null=False)
	employeeNationalId=models.IntegerField(null=False,blank=False)
	employeePassport=models.CharField(max_length=12,null=True,blank=True)
	employeeEthnicity=models.CharField(max_length=15,default='NA',null=True,blank=True)
	employeeReligion=models.CharField(max_length=15,default='NA',null=True,blank=True)
	employeePhoto=models.ImageField(upload_to='photo', blank=True,)
	status=models.CharField(max_length=30, choices=employeeStatus, default="Pending" )

class employeeFamily(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE,unique=True)
	employeeFamilyMaritalStatus=models.CharField(max_length=15, default='Unmarried')
	employeeFamilyNumberOfChild= models.CharField(max_length=15,default="0",null=True)
	employeeFamilySpouseWorking =models.CharField(max_length=15,default='No',null=True)
	employeeFamilySpouseFirstName= models.CharField(max_length=255,blank=True,null=True)
	employeeFamilySpouseMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeFamilySpouseLastName=models.CharField( max_length=255,blank=True,null=True)
	employeeFamilySpouseBirthDate=models.DateField(null=True,blank = True)
	employeeFamilySpouseNationality=models.CharField(max_length=15, default='India',blank=False,null=False)
	employeeFamilySpouseNationalId=models.CharField(max_length=8, null=True,blank=True)
	employeeFamilySpousePassport=models.CharField(max_length=12,null=True,blank=True)
	employeeFamilySpouseEthnicity=models.CharField(max_length=15, default='NA',null=True,blank=True)
	employeeFamilySpouseReligion=models.CharField(max_length=15,default='NA',null=True,blank=True)

class employeeChildren(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE)
	employeeChildrenFirstName= models.CharField(max_length=255,blank=True,null=True)
	employeeChildrenMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeChildrenLastName=models.CharField( max_length=255,blank=True,null=True)
	employeeChildrenBirthDate=models.DateField(blank=True,null=True)
	employeeChildrenGender= models.CharField(max_length=15, choices=gender, default='U',blank=True,null=True)
	employeeChildrenMaritalStatus=models.CharField(max_length=1,default='Unmarried')
	# employeeChildKey=models.CharField(max_length=15,default=0)

class employeeHealth(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE, unique = True)
	employeeHealthHeight=models.CharField(max_length=255,blank=True,null=True)
	employeeHealthWeight=models.CharField(max_length=255,null=True,blank=True)
	employeeHealthBloodGroup=models.CharField(max_length=5, default="Don't No",blank=True,null=True)

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
	email= models.EmailField(max_length=55,null=True,blank=True	)
	blogHomepage=models.CharField(max_length=60,null=True)
	office=models.CharField(max_length=30,null=True)
	officeExtention=models.CharField(max_length=30,null=True,blank=True )
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

