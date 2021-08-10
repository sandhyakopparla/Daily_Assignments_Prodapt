import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_allrounder(all_roundername,all_location):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",all_roundername)
    val2=re.natch("([a-z]+)([a-z]+)([a-z]+)$",all_location)
    try:
        if val1 and val2:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")