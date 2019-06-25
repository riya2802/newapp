from django import forms
from .models import employee,employeeFamily,employeeChildren,employeeHealth

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