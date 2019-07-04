import re
from datetime import date 
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
		return True
	else :
		if re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I):
			print('kkkk')
			return True
		else:
			return False
		

			#return bool(re.se("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
def is_valid_phone(phone):
	if phone == "":
		print("blank")
		return True
	else:
		Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
		if Pattern.match(phone):
			return True
		return False

def is_valid_username(username):
	if re.search(' +', username): ## return true when user name contain space 
		print('is_valid_username function call')
		return False
	else:
		return True

def check_is_valid_name(name): 
	if name is None or name =="":
		return True
	if name.isalpha():
 		return True
	return False


def calculateAge(born): 
	if born == "":
		return True
	today = date.today() 
	try:  
		birthday = born.replace(year = today.year)  
	except ValueError:  						
    # raised when birth date is February 29 
    # and the current year is not a leap year
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1) 
	if birthday > today: 
		return today.year - born.year - 1
	else: 
		return today.year - born.year 

def is_valid_passport(passport):
    if str(passport).isalpha():
        print("1")
        return False
    if passport == "":
        return True
    if len(str(passport)) != 12:
        print("2")
        return False
    print("3")
    return True

def is_valid_national(nationaid):
	if str(nationaid).isalpha():
		print("1")
		return False
	if nationaid == "":
		return False
	if len(str(nationaid)) != 8:
		print("2")
		return False
		print("3")
	return True

def calculate_join_date(joindate, birthdate):
	current_date=date.today()
	if joindate < birthdate and joindate > current_date :
		return False
	return True 

def calculate_Effective_date(effectivedate):
	current_date=date.today()
	last_month = now.month-1 if now.month > 1 else 12
	if  effectivedate > current_date:
	pass


