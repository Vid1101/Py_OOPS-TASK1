import logging
logging.basicConfig(filename='oops_taskit1.log', level=logging.DEBUG, format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

class string_questions:

    def __init__(self,s):
        logging.info("String initialized from constructor")
        self.s = s
    def jump(self):
        """Q1. try to extract data from index one to index 300 with a jump of 3"""
        try:
            logging.info("Extracting string from index 0 to 300")
            sub_string = self.s[0:300:3]
            logging.info("extracted string : {}".format(sub_string))
            return sub_string
        except Exception as e:
            logging.exception(e)

    def reverse_string(self):
        """Q2 reverse the string without using reverse function"""
        try:
            new_string = ''
            logging.info("String reverse without reverse function")
            for i in range(len(self.s)-1,-1,-1):
                new_string = new_string+self.s[i]
            logging.info("Reversed value :{}".format(new_string))
            return new_string
        except Exception as e:
            logging.exception(e)

    def split_string(self):
        """Q3 Try to split a string after conversion of entire string in uppercase"""
        try:
            logging.info("Splitting string after converting to upper case")
            v = self.s.upper()
            logging.info("List of string values post split {}".format(v.split()))
            return v.split()
        except Exception as e:
            logging.exception(e)
    def lower_string(self):
        """Q4 try to convert the whole string into lower case"""
        try:
            logging.info("Converting the string to lower case")
            logging.info("Lower case string {}".format(self.s.lower()))
            return self.s.lower()
        except Exception as e:
            logging.exception(e)

    def capitalize_string(self):
        """Q5 try to capitalize the whole string"""
        try:
            logging.info("Capitalized string :{}".format(self.s.upper()))
            return self.s.upper()
        except Exception as e:
            logging.exception(e)
    def isalpha_vs_isalnum(self):
        """Q6 difference between isalpha and isalnum"""
        try:
            logging.info("Show difference between isalpha and isalnum")
            alpha = self.s.isalpha()
            alnum = self.s.isalnum()
            if alpha:
                logging.info("The string contains aplhabets only")
                return "Aphabetical string"
            elif alnum:
                logging.info("The string contains alphabets and numbers both")
                return "Alphanumeric string"
            else:
                logging.info("The string is heterogeneous")
                return "Heterogeneous string"
        except Exception as e:
            logging.exception(e)

    def expand_tabs(self,test_string):
        """Q7 Try to give an example of expand tab"""
        self.test_string = test_string
        logging.info("Demo example of expand tab")
        try:
            logging.info("The actual string without tab expands :{}".format(self.test_string))
            logging.info("Added 5 spaces in the string spaces using expandtabs() function :{}".format(self.test_string.expandtabs(5)))
            return self.test_string.expandtabs(5)
        except Exception as e:
            logging.info(e)

    def strip_string(self,ex):
        """Q8 Give an example of strip , lstrip and rstrip"""
        self.ex = ex
        logging.info("Example of strip, lstrip & rstrip")
        try:
            logging.info("The actual string :{}".format(self.ex))
            logging.info("The string after strip function :{}".format(self.ex.strip()))
            logging.info("The string after lstrip function :{}".format(self.ex.lstrip()))
            logging.info("The string after rstrip function :{}".format(self.ex.rstrip()))
            return self.ex.strip()
        except Exception as e:
            logging.exception(e)
    def string_replace(self):
        """Q9 Replace a string charecter by another charector by taking your own example """
        logging.info("demo replace in string functions")
        try:
            logging.info("Replacing python with data science in original string")
            logging.info(self.s.replace("Python","Data science"))
            return self.s.replace("Python","Data science")
        except Exception as e:
            logging.info(e)

    def string_center(self,string):
        self.string = string
        """Q10 Try  to give a definition of string center function with and example"""
        try:
            logging.info("Center method with fillchar character as *")
            logging.info("The new string :{}".format(self.string.center(30,'*')))
            return self.string.center(30,'*')
        except Exception as e:
            logging.exception(e)

logging.shutdown()
obj = string_questions("this is My First Python programming class and i am learNING python string and its function")
obj.jump()
obj.reverse_string()
obj.split_string()
obj.lower_string()
obj.capitalize_string()
obj.isalpha_vs_isalnum()
obj.expand_tabs("Test\texpand\ttabs")
obj.strip_string("  testing strip function  ")
obj.string_replace()
obj.string_center("centralize")