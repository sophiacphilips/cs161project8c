#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/16/22
#This code fills a dictionary with employee data then can be used to return private data with ID number key.

class Employee:
    """Represents an employee for a company"""
    def __init__(self, name, ID_number, salary, email_add):
        """Creates an employee profile with private data of name, id number, salary, and email"""
        self._name=name
        self._ID_number=ID_number
        self._salary=salary
        self._email_add=email_add

    def get_name(self):
        """returns name"""
        return self._name
    def get_ID_number(self):
        """returns ID_number"""
        return self._ID_number
    def get_salary(self):
        """returns salary"""
        return self._salary
    def get_email_add(self):
        """returns email_add"""
        return self._email_add

def make_employee_dict(name, ID_number, salary, email_add):
    """creates dictionary for employee data, so when key id number is known, their name, email, and salary can be returned"""
    dict={} #creates empty dictionary for employee data
    for i in range(len(ID_number)): #sets length of employee info
        dict[ID_number[i]]=Employee(name[i], ID_number[i], salary[i], email_add[i]) #sets id number up as key for private data
    return dict #returns filled dictionary

#testing
#name= ["Jean", "Kat", "Pomona"]
#ID_number=["100", "101", "102"]
#salary=[30, 35, 28]
#email_add=["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
#result= make_employee_dict(name, ID_number, salary, email_add)
#print(result["100"].get_name())