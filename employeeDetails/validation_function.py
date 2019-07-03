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
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year)  
    except ValueError:  						
    # raised when birth date is February 29 
    # and the current year is not a leap year
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
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