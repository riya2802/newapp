from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
gender = [
        ('M' ,'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
Nationality= [
		('India' ,'India'),
        
]
Ethnicity= [
        ('Gernal' ,'Gernal'),
        ('NA','NA'),


]
Religion= [
        ('Gernal' ,'Gernal'),                                                                                                                        
        ('NA','NA'),]

# class employee(models.Model):
# 	employeeId= models.IntegerField(primary_key=True)
# 	employeementId =models.IntegerField(null=False,blank=False)
# 	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
# 	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
# 	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
# 	employeeGender= models.CharField(max_length=1, choices=gender, default='U',blank=False,null=False)
# 	employeeBirthDate=models.DateField(blank=False,null=False)
# 	employeeNationality=models.CharField(max_length=1, choices=Nationality, default='India',blank=False,null=False)
# 	employeeNationalId=models.IntegerField(null=False,blank=False)
# 	employeePassport=models.IntegerField(null=True,blank=True)
# 	employeeEthnicity=models.CharField(max_length=1,choices=Ethnicity, default='NA',null=True,blank=True)
# 	employeeReligion=models.CharField(max_length=1,choices=Religion, default='NA',null=True,blank=True)

class Job(models.Model):

	dateJoined = models.DateField(null=False,blank=False)
	endofProbation = models.DateField(null=True)
	position = models.CharField(max_length=30, null=False, blank=False)
	jobStatusEffectiveDate = models.DateField(null=False,blank=False)
	lineManager = models.CharField(max_length=30,null = True,blank=False)
	department = models.CharField(max_length=30,null = True,blank=False)
	branch = models.CharField(max_length=30,null = True,blank=False)
	level = models.CharField(max_length=30,null = True,blank=False)
	jobType = models.CharField(max_length=30,null = True,blank=False)
	employmentStatusEffectiveDate = models.DateField(null=False,blank=False)
	jobStatus = models.CharField(max_length=30,null = True,blank=False)
	leaveWorkflow = models.CharField(max_length=30,null = True,blank=False)
	workdays = models.CharField(max_length=30,null = True,blank=False)
	holidays= models.CharField(max_length=30,null = True,blank=False)
	termStart = models.CharField(max_length=30,null = True)
	termEnd = models.CharField(max_length=30,null = True)

class Contact(models.Model):
	email= models.EmailField(max_length=55, unique=True)
	blogHomepage=models.CharField(max_length=60)
	office=models.CharField(max_length=30)
	officeExtention=models.CharField(max_length=30)
	mobile=models.IntegerField(validators=[MaxValueValidator(11)])
	home=models.CharField(max_length=60)
	address1=models.CharField(max_length=160)
	address2=models.CharField(max_length=160)
	city =models.CharField(max_length=60)
	postCode=models.IntegerField(validators=[MaxValueValidator(20)])
	state=models.CharField(max_length=80)
	country=models.CharField(max_length=80, null=False)
	firstName=models.CharField(max_length=30)
	lastName=models.CharField(max_length=30)
	middleName=models.CharField(max_length=30)
	relationship=models.CharField(max_length=30)
	mobilePhone=models.IntegerField(validators=[MaxValueValidator(11)])
	housePhone=models.IntegerField(validators=[MaxValueValidator(11)])
	officePhone=models.IntegerField(validators=[MaxValueValidator(11)])


