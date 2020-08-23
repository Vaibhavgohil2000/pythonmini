import re

class validation1:
    @staticmethod
    def validateemail(eemail):
        emailRegex = re.compile(r'[\w\.-]+@[\w\.-]+')

        if emailRegex.search(eemail):
            return True
        else:
            return False
    @staticmethod
    def validatetemobile(emob):
        mobRegex = re.compile(r'\d{10}')

        if mobRegex.search(emob):
            return True
        else:
            return False
