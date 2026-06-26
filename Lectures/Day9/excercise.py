class UnderAgeError(Exception):
    pass


def check_age(age):
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise UnderAgeError("You do not qualify to drive.")
    except UnderAgeError as e:
        print("Error:", str(e))
check_age(15)



# print error debugging
lists = [2,4,6,8,10]
print("List:", lists)
# logging system errors
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR)
logging.info("Application started.")
logging.warning("Low disk space.")
logging.error("An error occurred.")