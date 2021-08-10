import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_product(productname,distributor_name,manufacturer_number):
    val1=re.search("[A-Z]{1}[^A-Z]{0,25}$",productname)
    val2=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",distributor_name)
    val3=re.search("^[7-9][0-9]{9}",manufacturer_number)
    try:
        if val1 and val2 and val3:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")






