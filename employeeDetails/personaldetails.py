from django import forms
from .models import employee

class personalDetails(forms.ModelForm):
	class Meta:
		model = employee
		fields=['employeementId','employeeFirstName','employeeMiddelName','employeeLastName','employeeGender','employeeBirthDate','employeeNationality','employeeNationalId','employeePassport','employeeEthnicity','employeeReligion']
    