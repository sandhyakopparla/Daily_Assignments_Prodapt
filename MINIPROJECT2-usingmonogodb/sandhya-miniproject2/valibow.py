import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_bowler(bowler_name,bo_location):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",bowler_name)
    val2=re.natch("([a-z]+)([a-z]+)([a-z]+)$",bo_location)
    try:
        if val1 and val2:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")