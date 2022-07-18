import logging
logging.basicConfig(filename="oops_taskit2.log",level=logging.DEBUG, format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

class list_questions:
    def __init__(self,l):
        self.l = l

    def list_entity(self):
        """Q1 try to extract all the list entity"""
        logging.info("extracting all the list entities")
        try:
            ans = []
            for i in self.l:
                if type(i) == list:
                    logging.info("List extracted {}".format(i))
                    ans.append(i)
            return ans
        except Exception as e:
            logging.exception(e)

    def dict_entity(self):
        """Q2 try to extract all the dictionary entity"""
        logging.info("Extracting all the dictionary entities")
        try:
            ans = []
            for i in self.l:
                if type(i) == dict:
                    logging.info("Dictionary entity extracted {}".format(i))
                    ans.append(i)
            return ans
        except Exception as e:
            logging.exception(e)

    def tuple_entity(self):
        """Q3 try to extract all the tuple entity"""
        logging.info("Extracting all the tuple entities")
        try:
            ans = []
            for i in self.l:
                if type(i) == tuple:
                    logging.info("Tuple entity extracted {}".format(i))
                    ans.append(i)
            return ans
        except Exception as e:
            logging.exception(e)

    def numerical_data(self):
        """Q4 try to extract all the numerical data it may be part of dict key and values"""
        logging.info("Extracting all the numerical data from list")
        try:
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            print(j)
                            logging.info(j)
                elif type(i) == dict:
                    for j in i:
                        if type(j) == int or type(i[j]) == int:
                            print(str(j) + ":" + str(i[j]))
                            logging.info(str(j) + ":" + str(i[j]))
        except Exception as e:
            logging.exception(e)

    def sum_numerical_data(self):
        """Q5 try to give summation of all the numerical data"""
        logging.info("Summation of all numbers in data")
        try:
            sum = 0
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j
                elif type(i) == dict:
                    for j in i:
                        if type(j) == int or type(i[j]) == int:
                            if type(j) == int:
                                sum = sum + j
                            else:
                                sum = sum + i[j]
            logging.info("Sum of all numbers in list is :{}".format(sum))
            return sum
        except Exception as e:
            logging.exception(e)
    def odd_data(self):
        """Q6 try to filter out all the odd values out of all the numerical data which is a part of list"""
        logging.info("Extracting odd values from list")
        try:
            odd_list = []
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int and j%2 != 0:
                            odd_list.append(j)
                        elif type(i) == dict:
                            for j in i:
                                if type(j) == int or type(i[j] == int):
                                    if type(j) == int and j%2 == 0:
                                        odd_list.append(j)
                                    elif type(i[j]) == int and i[j]%2 != 0:
                                        odd_list.append(i[j])
            logging.info("Odd data list :{}".format(odd_list))
            return odd_list

        except Exception as e:
            logging.exception(e)
    def ineuron_extract(self):
        """Q7 try to extract ineuron out of this data"""
        try:
            logging.info("Extract ineuron from the data set")
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == str and j == 'ineuron':
                            print(j)
                            logging.info("Found it in list/set/tuple :{}".format(j))
                if type(i) == dict:
                    for j in i:
                        if (type(j) == str and j == 'ineuron') or (type(i[j]) == str and i[j] == 'ineuron'):
                            print(str(j) +":" + str(i[j]))
                            logging.info("Found it in dictionary :{}".format(j+":"+i[j]))
        except Exception as e:
            logging.exception(e)

    def count_data(self):
        """Q8 try to find out number of occurances of all the data"""
        logging.info("Logging the frequency of data")
        try:
            data_set = []
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        data_set.append(j)
                if type(i) == dict:
                    for j in i:
                        data_set.append(j)
                        data_set.append(i[j])
            for i in set(data_set):
                print(data_set.count(i))
                logging.info("Frequency of {} ".format(str(i) + ":" + str(data_set.count(i))))
        except Exception as e:
            logging.exception(e)

    def key_count_dict(self):
        """Q9 try to find out number of keys in dict element"""
        logging.info("Logging number of keys in dict element")
        try:
            key_count = 0
            for i in self.l:
                if type(i) == dict:
                    for j in i:
                        key_count = key_count+1
            logging.info("Number of keys found {}".format(key_count))
            return key_count
        except Exception as e:
            logging.exception(e)

    def strings_in_list(self):
        """Q10 try to filter out all the strings data"""
        logging.info("Filter the string data from list")
        try:
            str_list = []
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == str:
                            str_list.append(j)
                elif type(i) == dict:
                    for j in i:
                        if type(j) == str:
                            str_list.append(j)
                        if type(i[j]) == str:
                            str_list.append(i[j])
            logging.info("The string data extracted from list are {}".format(str_list))
            return str_list
        except Exception as e:
            logging.exception(e)

    def alphanumeric_data(self):
        """Q11 try to find out alphanumeric data  ## k1 ,k2,k3"""
        logging.info("Filter the alphanumeric data from list")
        try:
            str_list = []
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == str and j.isalnum():
                            str_list.append(j)
                elif type(i) == dict:
                    for j in i:
                        if type(j) == str and j.isalnum():
                            str_list.append(j)
                        if type(i[j]) == str and i[j].isalnum():
                            str_list.append(i[j])
            logging.info("The alphanumeric data extracted from list are {}".format(str_list))
            return str_list
        except Exception as e:
            logging.exception(e)
logging.shutdown()

obj = list_questions([[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
)
obj.list_entity()
obj.dict_entity()
obj.tuple_entity()
obj.numerical_data()
obj.sum_numerical_data()
obj.odd_data()
obj.ineuron_extract()
obj.count_data()
obj.key_count_dict()
obj.strings_in_list()
obj.alphanumeric_data()
