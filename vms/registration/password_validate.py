def validate_password(password):
	upper_case=False #counter for uppercase characters
	lower_case=False #counter for lowercase characters
	number=False #counter for numbers
	special_character=False #counter for special characters
	special_list=['!','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','\\','^','_','`','{','}','|','~','"']
	for x in password:
		if x.isupper(): #checking for uppercase characters
			upper_case=True
		if x.islower(): #checking  for lowercase characters
			lower_case=True
		if x.isdigit(): #checking for nummbers
			number=True
		if x in special_list: #checking for special characters
			special_character=True
		if ((upper_case==True and lower_case==True and special_character==True)
		or (upper_case==True and lower_case==True and number==True)
		or (number==True and lower_case==True and special_character==True)
		or (upper_case==True and number==True and special_character==True)):
			return(True)
	return(False)
