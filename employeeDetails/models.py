from django.db import models

# Create your models here.
gender = [
        ('M' ,'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]
Nationality= [
		('India' ,'India'),
        
]
class employee(models.Model):
	employeeId= models.IntegerField(primary_key=True, required = True)
	employeementId =models.IntegerField(primary_key=True, required = True)
	employeeFirstName= models.CharField(max_length=255, required = True)
	employeeMiddelName=models.CharField(max_length=255)
	employeeLastName=models.CharField( max_length=255,required = True)
	employeeGender= models.CharField(max_length=1, choices=gender, default='O')
	employeeBirthDate=models.DateField()
	employeeNationality=models.CharField(max_length=1, choices=Nationality, default='india')
	employeeNationalId=models.IntegerField(required = True,)
	employeePassport=models.IntegerField(primary_key=True, required = True)models.IntegerField(primary_key=True, required = True)
	employeeEthnicity=models.CharField(max_length=255)
	employeeReligion=models.CharField(max_length=255)


