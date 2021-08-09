import re,logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_books(book_title,author,description,price,distributor_name,publisher):
    val1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",book_title)
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",author)
    val3=re.match("([a-z]+)([a-z]+)([a-z]+)$",description)
    val4=re.match("([0-9]{0,7}$)",price)
    val5=re.match("([a-z]+)([a-z]+)([a-z]+)$",distributor_name)
    val6=re.match("([a-z]+)([a-z]+)([a-z]+)$",publisher)
    try:
        if val1 and val2 and val3 and val4 and val5 and val6:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")