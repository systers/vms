import re

def validate_password(password):
	upp_low_spec = False
	upp_low_num = False
	upp_num_spec = False
	low_num_spec = False
	if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[@#$%^&+=]',password):
		upp_low_spec = True
	if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[0-9]',password):
		upp_low_num = True
	if re.search(r'[A-Z]',password) and re.search(r'[0-9]',password) and re.search(r'[@#$%^&+=]',password):
		upp_num_spec = True
	if re.search(r'[a-z]',password) and re.search(r'[0-9]',password) and re.search(r'[@#$%^&+=]',password):
		low_num_spec = True


	if upp_num_spec or upp_low_num or upp_low_spec or low_num_spec :
		return True
	else:
		return False
