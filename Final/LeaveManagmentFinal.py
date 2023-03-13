# Gabriel Wersebe
# This is the class implementation of the final project with a sample driver program. This is for the leave managment system.

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    leaves = relationship('Leave', backref='employee')

class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    team = relationship('Employee', backref='manager')

class Leave(Base):
    __tablename__ = 'leave'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    reason = Column(String)
    status = Column(String, default='Pending')

class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manager_id = Column(Integer, ForeignKey('manager.id'))
    employees = relationship('Employee', backref='department')

class Holiday(Base):
    __tablename__ = 'holiday'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    
engine = create_engine('sqlite:///leaves.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_admin():
    name = input('Enter name: ')
    email = input('Enter email: ')
    password = input('Enter password: ')
    admin = Admin(name=name, email=email, password=password)
    session.add(admin)
    session.commit()

def create_manager():
    name = input('Enter name: ')
    email = input('Enter email: ')
    password = input('Enter password: ')
    manager = Manager(name=name, email=email, password=password)
    session.add(manager)
    session.commit()

def create_employee():
    name = input('Enter name: ')
    email = input('Enter email: ')
    password = input('Enter password: ')
    manager_id = int(input('Enter manager ID: '))
    employee = Employee(name=name, email=email, password=password, manager_id=manager_id)
    session.add(employee)
    session.commit()

def create_department():
    name = input('Enter name: ')
    manager_id = int(input('Enter manager ID: '))
    department = Department(name=name, manager_id=manager_id)
    session.add(department)
    session.commit()

def create_leave():
    start_date = input('Enter start date (YYYY-MM-DD): ')
    end_date = input('Enter end date (YYYY-MM-DD): ')
    reason = input('Enter reason: ')
    employee_id = int(input('Enter employee ID: '))
    leave = Leave(start_date=start_date, end_date=end_date, reason=reason, employee_id=employee_id)
    session.add(leave)
    session.commit()

def query_leaves():
    leaves = session.query(Leave).all()
    for leave in leaves:
        print(f'{leave.employee.name} ({leave.employee.manager.name}) has a leave request from {leave.start_date} to {leave.end_date} for {leave.reason}')

def query_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f'{employee.name} ({employee.email}) works under {employee.manager.name}')

def query_departments():
    departments = session.query(Department).all()
    for department in departments:
        print(f'{department.name} is managed by {department.manager.name}')

def query_holidays():
    holidays = session.query(Holiday).all()
    for holiday in holidays:
        print(f'{holiday.name} is on {holiday.date}')

menu = {
    '1': {'text': 'Create admin', 'action': create_admin},
    '2': {'text': 'Create manager', 'action': create_manager},
    '3': {'text': 'Create employee', 'action': create_employee},
    '4': {'text': 'Create department', 'action': create_department},
    '5': {'text': 'Create leave', 'action': create_leave},
    '6': {'text': 'Query leaves', 'action': query_leaves},
    '7': {'text': 'Query employees', 'action': query_employees},
    '8': {'text': 'Query departments', 'action': query_departments},
    '9': {'text': 'Query holidays', 'action': query_holidays},
    '0': {'text': 'Exit', 'action': exit},
}

while True:
    print('MENU')
    for key, value in menu.items():
        print(f'{key}. {value["text"]}')
    choice = input('Enter choice: ')
    menu[choice]['action']()

