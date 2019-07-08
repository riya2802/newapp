import re
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from dateutil.parser import parse

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
	if phone == "" or phone == None:
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
	if name.isalnum():
		return False
	return False

def date_to_string(date1):
	date_obj = datetime.strptime(date1, '%Y-%m-%d').date()
	print('date_obj',date_obj,type(date_obj))
	print()
	return date_obj

def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def calculateAge(born): 
	if born == "":
		return True
	today = datetime.today() 
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
   	if passport == "" or passport is None :
   		return True
   	if len(str(passport)) != 12:
   		print("2")
   		return False
   	if str(passport).isalpha():
   		print("1")
   		return False
   	print("3")
   	return True

def is_valid_national(nationaid):
	if nationaid == "":
		return False
	if len(str(nationaid)) != 8:
		print("2")
		return False
	if str(nationaid).isalpha():
		print("1")
		return False
	if str(nationaid).isdigit():
		return True
	return True

def check_join_date(joindate, birthdate):
	if not is_date(joindate):
		return False
	current_date=datetime.today()
	mindate =data = add_years(birthdate,18)
	print('mindate',mindate,type(mindate))
	if date_to_string(joindate) < mindate or date_to_string(joindate) > current_date.date() :
		print('correct')
		return False
	return True 

def calculate_Effective_date(effectivedate):
	if not is_date(effectivedate):
		return False
	c_date = datetime.date(datetime.today())
	month = c_date-timedelta(days=30)
	print('c_date',c_date,type(c_date))
	print('month',month,type(month))
	#print('effectivedate',date_to_string(effectivedate),type(date_to_string(effectivedate)))
	edate = date_to_string(effectivedate)
	print(edate)
	if date_to_string(effectivedate) < month or date_to_string(effectivedate) > c_date :
		#print(date_to_string(effectivedate) > current_date - (datetime.timedelta(1*365/12)).isofornat())
		return False
	return True

def check_employeeId(employeeid):
	if employeeid.isalpha():
		return False
	if employeeid.isdigit():
		return True
	else:
		return False



# def is_valid_health(health):
# 	if str(height).isalpha():
# 		return False
# 	pass


def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
    
def end_of_probation(probationdate,joindate):
	if not is_date(probationdate):
		return False
	days1 = 30*3+2 ## probation date is b/w  joining date and from 3 months later
	print('date_to_string(probationdate)',date_to_string(probationdate))
	newprobationdate=date_to_string(probationdate)
	joinDate = date_to_string(joindate)
	print(type(joinDate),type(newprobationdate))
	afterdate = joinDate+timedelta(days=days1)
	print('afterdate',afterdate, type(afterdate))
	if newprobationdate < joinDate or newprobationdate > afterdate:
		return False
	return True

def is_valid_postcode(postcode):
	if postcode == "" or postcode is None :
		return True
	if postcode.isalpha():
		return False
	if len(postcode) != 6 :
		return False
	return True

def is_valid_height(height):
	if height =="" or height is None:
		return True
	if height.isalpha():
		return False
	if float(height) > 122  and float(height) <= 325:
		return True
	return False

def is_valid_weight(weight):
	if weight =="" or weight is None:
		return True
	if weight.isalpha():
		return False
	if float(weight) > 25 and float(weight) <=120 :
		return True
	return False