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
class employee(models.Model):
	employeeId= models.AutoField(primary_key=True)
	employeementId =models.CharField(max_length=255,null=False,blank=False,unique=True)
	employeeFirstName= models.CharField(max_length=255,blank=False,null=False)
	employeeMiddelName=models.CharField(max_length=255,null=True,blank=True)
	employeeLastName=models.CharField( max_length=255,blank=False,null=False)
	employeeGender= models.CharField(max_length=15, choices=gender, default='U',blank=False,null=False)
	employeeBirthDate=models.DateField(blank=False,null=False)
	employeeNationality=models.CharField(max_length=15, choices=Nationality, default='India',blank=False,null=False)
	employeeNationalId=models.IntegerField(null=False,blank=False,unique=True)
	employeePassport=models.IntegerField(null=True,blank=True)
	employeeEthnicity=models.CharField(max_length=15,choices=Ethnicity, default='NA',null=True,blank=True)
	employeeReligion=models.CharField(max_length=15,choices=Religion, default='NA',null=True,blank=True)
	employeePhoto=models.ImageField(upload_to='photo', blank=True,)

class employeeFamily(models.Model):
	employeeForeignId =models.ForeignKey(employee,models.CASCADE,unique=True)
	employeeFamilyMaritalStatus=models.CharField(max_length=15, choices=MaritalStaus, default='Unmarried')
	employeeFamilyNumberOfChild= models.CharField(max_length=15,default="0")
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