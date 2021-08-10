import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_employee(name,phone,address):
    val1=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
    val2=re.search("^[7-9][0-9]{9}",phone)
    val3=re.search("[A-Z]{1}[^A-Z]{0,25}$",address)
    try:
        if val1 and val2 and val3:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")
