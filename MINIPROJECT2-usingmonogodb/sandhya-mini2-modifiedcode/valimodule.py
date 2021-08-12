import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_cricketers(cricketer_name,location,batting_style,bowling_style):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",cricketer_name)
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",location)
    val3=re.match("([a-z]+)([a-z]+)([a-z]+)$",batting_style)
    val4=re.match("([a-z]+)([a-z]+)([a-z]+)$",bowling_style)
    try:
        if val1 and val2 and val3 and val4:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")