import re

from django.contrib.auth.models import User


def checkForNone(fieldvalue):
	if fieldvalue is not None and fieldvalue !="":
		print(" fieldvalue",fieldvalue)
		data= fieldvalue
		return (data) 
	else:
		data = None
		return (data)


def is_valid_email(email):
	if email == "":
		return None
	else :
		if re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I):
			print('kkkk')
			return email
		else:
			return "errormsg"
		

			#return bool(re.se("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
def is_valid_phone(phone):
	if phone == "":
		print("blank")
		phone = None
		return phone
	else:
		Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
		if Pattern.match(phone):
			return phone
		return "errormsg"

def is_valid_username(username):
	if re.search(' +', username): ## return true when user name contain space 
		print('is_valid_username function call')
		return None
	else:
		return username



