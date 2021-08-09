import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_batsman(batsman_name,b_location):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",batsman_name)
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",b_location)
    try:
        if val1 and val2:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")