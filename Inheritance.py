# Gabriel Wersebe

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
