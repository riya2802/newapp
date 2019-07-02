from django import forms
from .models import employee,employeeFamily,employeeChildren,employeeHealth




class login_class(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class personalDetails(forms.ModelForm):
	class Meta:
		model = employee
		fields=['employeementId','employeeFirstName','employeeMiddelName','employeeLastName','employeeGender','employeeBirthDate','employeeNationality','employeeNationalId','employeePassport','employeeEthnicity','employeeReligion']
    
class familyDetails(forms.ModelForm):
	class Meta:
		model = employeeFamily
		fields=['employeeFamilyMaritalStatus','employeeFamilyNumberOfChild','employeeFamilySpouseWorking','employeeFamilySpouseFirstName','employeeFamilySpouseMiddelName','employeeFamilySpouseLastName','employeeFamilySpouseBirthDate','employeeFamilySpouseNationality','employeeFamilySpouseNationalId','employeeFamilySpousePassport','employeeFamilySpouseEthnicity','employeeFamilySpouseReligion']

class childrenDetails(forms.ModelForm):
	class Meta:
		model = employeeChildren
		fields=['employeeChildrenFirstName','employeeChildrenMiddelName','employeeChildrenLastName','employeeChildrenBirthDate','employeeChildrenGender','employeeChildrenMaritalStatus']


class healthDetails(forms.ModelForm):
	class Meta:
		model = employeeHealth
		fields=['employeeHealthHeight','employeeHealthWeight','employeeHealthBloodGroup']


# class updateDetails(forms.Form):
# 	employeeFname=forms.CharField(max_length=255, required=True)
# 	employeeMname=form.CharField(max_length=255)
# 	employeeLname=forms.CharField(max_length=255, required=True)
# 	employeeGender=forms.CharField(max_length=255, required=True)
# 	employeeBithday=forms.DateField(max_length=255, required=True)
# 	employeeNationality=forms.CharField(max_length=255,required=True)
# 	employeeNationalId=forms.IntegerField(null=False,blank=False)
# 	employeePassport=forms.IntegerField(null=True,blank=True)
# 	employeeEthnicity=forms.CharField(max_length=255 ,null=True,blank=True)
# 	employeeReligion=forms.CharField(max_length=15,null=True,blank=True)
# 	employeePhoto=forms.ImageField( blank=True,)
# 	employeeMaritalstatu=forms.CharField(max_length=15,)
# 	employeeNumberOfChild=forms.CharField(max_length=15)
# 	employeeSpouseWorking=forms.CharField(max_length=15,null=True)
# 	employeeSpouseFirstName=forms.CharField(max_length=255,blank=True,null=True)
# 	employeeSpouseLastName=forms.CharField(max_length=255,null=True,blank=True)
# 	employeeSpouseMiddelName=forms.CharField( max_length=255,blank=True,null=True)
# 	employeeSpouseBirthDate=forms.DateField(null=True)
# 	employeeSpouseNationality=forms.CharField(max_length=15,blank=False,null=False)
# 	employeeSpouseNationalId=forms.IntegerField(null=True,blank=True)
# 	employeeSpousePassport=forms.IntegerField(null=True,blank=True)
# 	employeeSpouseEthnicity=forms.CharField(max_length=15,null=True,blank=True)
# 	employeeSpouseReligion=forms.CharField(max_length=15,null=True,blank=True)
# 	employeeChildrenFirstName=forms.CharField(max_length=255,blank=True,null=True)
# 	employeeChildrenMiddelName=forms.CharField(max_length=255,null=True,blank=True)
# 	employeeChildrenLastName=forms.CharField( max_length=255,blank=True,null=True)
# 	employeeChildrenBirthDate=forms.DateField(blank=True,null=True)
# 	employeeChildrenGender=forms.CharField(max_length=15,blank=True,null=True)
# 	employeeChildrenMaritalStatus=forms.CharField(max_length=1,)
# 	employeeHealthHeight=forms.CharField(max_length=255,blank=True,null=True)
# 	employeeHealthWeight=forms.CharField(max_length=255,blank=True,null=True)
# 	employeeHealthBloodGroup=forms.CharField(max_length=5,blank=True,null=True)
