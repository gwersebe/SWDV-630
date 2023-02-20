# Gabriel Wersebe

# I dont know which one of these patterns will be best for the final product yet but I have implemented these different design patterns based on the code from the Inheritance 2 Assignemnt. I think having these examples 
# will help me decide when it comes time to finalize the design for the final project.

# Original Code

class Leave:
    def __init__(self, employee_id, start_date, end_date):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def check_eligibility(self):
        pass
    
    def apply_leave(self):
        pass

class SickLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, illness_type):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.illness_type = illness_type
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Sick Leave Application Submitted")

class VacationLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, destination):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.destination = destination
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Vacation Leave Application Submitted")

class MaternityLeave(Leave):
    def __init__(self, employee_id, start_date, end_date):
        Leave.__init__(self, employee_id, start_date, end_date)
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Maternity Leave Application Submitted")



def Test():
    sick_leave = SickLeave("Emp001", "2023-02-01", "2023-02-05", "Covid-19")
    if sick_leave.check_eligibility():
        sick_leave.apply_leave()
        
    vacation_leave = VacationLeave("Emp002", "2023-03-01", "2023-03-10", "Italy")
    if vacation_leave.check_eligibility():
        vacation_leave.apply_leave()
        
    maternity_leave = MaternityLeave("Emp003", "2023-04-01", "2023-04-03")
    if maternity_leave.check_eligibility():
        maternity_leave.apply_leave()

Test()



# 1. Factory Pattern
# For this we can take the original code and add the factory class to create the differnet leave types.
class Leave:
    def __init__(self, employee_id, start_date, end_date):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def check_eligibility(self):
        pass
    
    def apply_leave(self):
        pass

class SickLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, illness_type):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.illness_type = illness_type
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Sick Leave Application Submitted")

class VacationLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, destination):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.destination = destination
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Vacation Leave Application Submitted")

class MaternityLeave(Leave):
    def __init__(self, employee_id, start_date, end_date):
        Leave.__init__(self, employee_id, start_date, end_date)
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Maternity Leave Application Submitted")

class LeaveFactoryClass:
    @staticmethod
    def create_leave(leave_type, employee_id, start_date, end_date, **kwargs):
        if leave_type == "sick":
            return SickLeave(employee_id, start_date, end_date, kwargs.get("illness_type"))
        elif leave_type == "vacation":
            return VacationLeave(employee_id, start_date, end_date, kwargs.get("destination"))
        elif leave_type == "maternity":
            return MaternityLeave(employee_id, start_date, end_date)
        else:
            return None


def Test():
    leave_factory = LeaveFactoryClass()
    
    sick_leave = leave_factory.create_leave("sick", "Emp001", "2023-02-01", "2023-02-05", illness_type="Covid-19")
    if sick_leave and sick_leave.check_eligibility():
        sick_leave.apply_leave()
        
    vacation_leave = leave_factory.create_leave("vacation", "Emp002", "2023-03-01", "2023-03-10", destination="Italy")
    if vacation_leave and vacation_leave.check_eligibility():
        vacation_leave.apply_leave()
        
    maternity_leave = leave_factory.create_leave("maternity", "Emp003", "2023-04-01", "2023-04-03")
    if maternity_leave and maternity_leave.check_eligibility():
        maternity_leave.apply_leave()

Test()

# 2. Facade Pattern
# For this method its a little more "functional" where as the factory method is more "object oriented", this pretty much does the same thing but will use a function to create the different leave types instead of another class.

class Leave:
    def __init__(self, employee_id, start_date, end_date):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def check_eligibility(self):
        pass
    
    def apply_leave(self):
        pass

class SickLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, illness_type):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.illness_type = illness_type
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Sick Leave Application Submitted")

class VacationLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, destination):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.destination = destination
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Vacation Leave Application Submitted")

class MaternityLeave(Leave):
    def __init__(self, employee_id, start_date, end_date):
        Leave.__init__(self, employee_id, start_date, end_date)
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Maternity Leave Application Submitted")


class LeaveFacade:
    def __init__(self):
        pass
    
    def apply_sick_leave(self, employee_id, start_date, end_date, illness_type):
        sick_leave = SickLeave(employee_id, start_date, end_date, illness_type)
        if sick_leave.check_eligibility():
            sick_leave.apply_leave()
    
    def apply_vacation_leave(self, employee_id, start_date, end_date, destination):
        vacation_leave = VacationLeave(employee_id, start_date, end_date, destination)
        if vacation_leave.check_eligibility():
            vacation_leave.apply_leave()
    
    def apply_maternity_leave(self, employee_id, start_date, end_date):
        maternity_leave = MaternityLeave(employee_id, start_date, end_date)
        if maternity_leave.check_eligibility():
            maternity_leave.apply_leave()

def Test():
    leave_facade = LeaveFacade()
    
    leave_facade.apply_sick_leave("Emp001", "2023-02-01", "2023-02-05", "Covid-19")
    
    leave_facade.apply_vacation_leave("Emp002", "2023-03-01", "2023-03-10", "Italy")
    
    leave_facade.apply_maternity_leave("Emp003", "2023-04-01", "2023-04-03")

Test()

# 3. Singleton Pattern
# This method is the most complex out of the 3 but is the most truly object oriented design since the factory method itself is technically using an object it is still a very "functional" way of doing it. Out of the 3 this would adhere the best
# to the true object oriented design principles.

class LeaveApplication:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply_leave(self, leave_type, employee_id, start_date, end_date, *args):
        if leave_type == "sick":
            leave = SickLeave(employee_id, start_date, end_date, *args)
        elif leave_type == "vacation":
            leave = VacationLeave(employee_id, start_date, end_date, *args)
        elif leave_type == "maternity":
            leave = MaternityLeave(employee_id, start_date, end_date)
        else:
            raise ValueError("Invalid leave type")

        if leave.check_eligibility():
            leave.apply_leave()

class Leave:
    def __init__(self, employee_id, start_date, end_date):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def check_eligibility(self):
        pass
    
    def apply_leave(self):
        pass

class SickLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, illness_type):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.illness_type = illness_type
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Sick Leave Application Submitted")

class VacationLeave(Leave):
    def __init__(self, employee_id, start_date, end_date, destination):
        Leave.__init__(self, employee_id, start_date, end_date)
        self.destination = destination
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Vacation Leave Application Submitted")

class MaternityLeave(Leave):
    def __init__(self, employee_id, start_date, end_date):
        Leave.__init__(self, employee_id, start_date, end_date)
    
    def check_eligibility(self):
        return True

    def apply_leave(self):
        print("Maternity Leave Application Submitted")
