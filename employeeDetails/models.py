from django.db import models

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
class employee(models.Model):
	employeeId= models.AutoField(primary_key=True)
	employeementId =models.CharField(max_length=255,null=False,blank=False,unique=True)
	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
	employeeGender= models.CharField(max_length=1, choices=gender, default='U',blank=False,null=False)
	employeeBirthDate=models.DateField(blank=False,null=False)
	employeeNationality=models.CharField(max_length=1, choices=Nationality, default='India',blank=False,null=False)
	employeeNationalId=models.IntegerField(null=False,blank=False,unique=True)
	employeePassport=models.IntegerField(null=True,blank=True)
	employeeEthnicity=models.CharField(max_length=1,choices=Ethnicity, default='NA',null=True,blank=True)
	employeeReligion=models.CharField(max_length=1,choices=Religion, default='NA',null=True,blank=True)
	employeePhoto=models.ImageField(upload_to='photo', blank=True,)


