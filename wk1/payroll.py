# class Employee () :
#   global first_name
#   global last_name
#   employeeId = input('Enter Employee Id: ')
#   first_name = str(input('Enter employee\'s first name: '))
#   last_name = str(input('Enter employee\'s last name: '))
#   hourly_wage = float(input('Enter Employee\'s hourly wage: '))
#   hours_worked = float(input('Enter employee\'s hours worked: '))
  
#   def pay(hrs_worked, hrly_wage):
#     if(hrs_worked <= 40.0):
#       pay = float(hrs_worked * hrly_wage)
#       return print(first_name + " " + last_name + "\'s" + " paycheck is $" + str(pay) + " with 40.0 Regular Hours.")
#     elif(hrs_worked > 40.0):
#       reg_pay = float(hrs_worked * hrly_wage)
#       overtime = float(hrs_worked - 40.0)
#       ot_pay = float(overtime * (hrly_wage * 1.5))
#       total_pay = float(reg_pay + ot_pay)
#       return print(first_name + " " + last_name + "\'s" + " paycheck is $" + str(total_pay) + ' with 40.0 Regular Hours, and ' + str(overtime) + ' hours of Overtime.')
  
#   pay(hours_worked, hourly_wage)

# Use setters/getters with class
  
class Employee () :
  def __init__(self, first=None, last=None, id=None, pay=0.00):
    self.firstName = first
    self.lastName = last
    self.employeeId = id
    self.hourlyPay = pay

  def get
  
    