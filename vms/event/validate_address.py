from easy_maps import geocode

def validate_address(location):
    if not location.isspace():
    	#removing extra spaces
    	location = " ".join(location.split())
        try:
        	location = geocode.google_v3(location)
        except:
        	location = "not found"
    else:
        location = " "
    return location