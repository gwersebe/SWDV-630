# Gabriel Wersebe
# This is an adaptation of the code from the original design patterns assignment where i made the leave classes. Instead of storing the objects in memory they will be stored in the SQLite database. 
# This database will be extended upon in the final project to potentially include a sign in feature as well as other tables to store employee information and other data.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///leaves.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Leave(Base):
    __tablename__ = 'leaves'

    id = Column(Integer, primary_key=True)
    employee_id = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    leave_type = Column(String)

    def __repr__(self):
        return f"<Leave(employee_id='{self.employee_id}', start_date='{self.start_date}', end_date='{self.end_date}', leave_type='{self.leave_type}')>"

Base.metadata.create_all(engine)


def add_leave():
    print("\nAdd Leave\n")

    employee_id = input("Employee ID: ")
    start_date_input = input("Start Date (MM/DD/YYYY): ")
    start_date = datetime.strptime(start_date_input, '%m/%d/%Y').date().strftime('%Y-%m-%d')
    end_date_input = input("End Date (MM/DD/YYYY): ")
    end_date = datetime.strptime(end_date_input, '%m/%d/%Y').date().strftime('%Y-%m-%d')
    leave_type = input("Leave Type: ")

    leave = Leave(employee_id=employee_id, start_date=start_date, end_date=end_date, leave_type=leave_type)
    session.add(leave)
    session.commit()

    print("\nLeave added successfully.")


def view_leaves():
    print("\nAll Leaves\n")

    leaves = session.query(Leave).all()

    if not leaves:
        print("No leaves found.")
    else:
        print("{:<5} {:<12} {:<12} {:<12} {}".format("ID", "Employee ID", "Start Date", "End Date", "Leave Type"))
        for leave in leaves:
            print("{:<5} {:<12} {:<12} {:<12} {}".format(leave.id, leave.employee_id, leave.start_date, leave.end_date, leave.leave_type))

    input("\nPress Enter to continue...")


def main():
    while True:
        print("\nLeave Management System\n")
        print("1. Add Leave")
        print("2. View Leaves")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ")

        if choice == '1':
            add_leave()
        elif choice == '2':
            view_leaves()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == '__main__':
    main()
