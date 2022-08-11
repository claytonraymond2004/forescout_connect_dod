import jwt  # PyJWT version 1.6.1 as of the time of authoring
import uuid
import time
from time import gmtime, strftime, sleep
from datetime import datetime, timedelta


# Mapping between dod_c2c response fields to CounterACT properties
dod_c2c_to_ct_props_map = {
     "suggested_uscybercom_device_category" : "connect_dod_c2c_suggested_uscybercom_device_category", 
     "manual_uscybercom_device_category" : "connect_dod_c2c_manual_uscybercom_device_category", 
     "uscybercom_device_category" : "connect_dod_c2c_uscybercom_device_category", 
    
}

# CONFIGURATION
# All server configuration fields will be available in the 'params' dictionary.
url = params["connect_dod_c2c_url"] 
bot_name = params["connect_dod_c2c_bot_name"] 
default_channel = params["connect_dod_c2c_default_channel"] 


# ***** START - AUTH API CONFIGURATION ***** #


# Making an API call to get the JWT token

# To use the server validation feature, use the keyword 'ssl_context' in the http reqeust


# For properties and actions defined in the 'property.conf' file, CounterACT properties can be added as dependencies. 
# These values will be found in the params dictionary if CounterACT was able to resolve the properties. 
# If not, they will not be found in the params dictionary.