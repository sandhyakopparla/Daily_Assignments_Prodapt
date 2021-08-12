import re,logging
try:
    def validate(dogName): 
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dogName) 
        if valname:
            return True
        else:
            return False

    def validatemail(email):
        valemail=re.match("^\w+[\._]?\w+[@]\w+[.]\w{2,3}$",email)
        if valemail:
            return True
        else:
            return False
except:
    logging.error("unable to process")