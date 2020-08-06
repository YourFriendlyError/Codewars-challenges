import re

# REGEX may be confusin but it's definitely worth it!

def is_valid_IP(strng):
    if (len(strng.split(".")) != 4) or strng == '':
        return False
        
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:\+\-\s]')
    
    for lead in strng.split('.'):
        if lead.isalpha() or regex.search(lead): # Ignore alpha characters or if any special character was used
            return False
            
        if int(lead) <= 255:
            if re.match('0[\d{0,9}].*', lead): # and not re.match('.0. | .0', lead): # if a section of IP address starts with 0 and ends with a trailing number (e.g .085.) return as false
                print('Trailing')
                return False
        else: # If num is greater than 255
            return False
    return True