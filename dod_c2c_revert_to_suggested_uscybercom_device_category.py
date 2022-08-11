import jwt  # PyJWT version 1.6.1 as of the time of authoring
import uuid
import time
from time import gmtime, strftime, sleep
from datetime import datetime, timedelta

# CONFIGURATION
# All server configuration fields will be available in the 'params' dictionary.
url = params["connect_dod_c2c_url"] 
bot_name = params["connect_dod_c2c_bot_name"] 
default_channel = params["connect_dod_c2c_default_channel"] 


# Actions Parameters 
category = actions_params["dod_c2c_category"] 


# ***** START - AUTH API CONFIGURATION ***** #



# Making an API call to get the JWT token



# To use the server validation feature, use the keyword 'ssl_context' in the http reqeust


# ***** END - AUTH API CONFIGURATION ***** #



# ***** PART 2 - DELETE USER  ***** #
# Here, the cookie that was set in adding the user is being used. The user id is used to delete the user.
# DELETE_USER_URL = url + "/users/v2/" + params["cookie"]


r = urllib.request.urlopen(request, context=ssl_context)
request_response = r.getcode()
response = {}
if r.getcode() == 200:
	response["succeeded"] = True
else:
	response["succeeded"] = False
	response["troubleshooting"] = "Failed action. Response code: {}".format(r.getcode())