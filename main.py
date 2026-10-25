from calculator import calculator


print(" " * 15 + "Hello, Welcome" + " " * 15)
print()
print()
print()
try:
    money = int(input("Enter the investment amount: "))
except:
    print("An error occurred; please try again.")

while money <= 0:
    print("""
               Error!!!! 
    Your monetary value cannot be less than zero.

    """)
    money = int(input("Enter the investment amount: "))

while money > 0:
    
    print('''please select in time
    Week[1]:
    Mounth[2]:
    Years[3]:''')

    time = int(input("Select : "))


    if time == 1:
        percentage = float(input("Enter the target percentage return for the time period:"))
        data_time = int(input("How many weeks of data do you want to see?"))
        calculator(money, percentage, data_time)
        

    elif time == 2:
        percentage = float(input("Enter the target percentage return for the time period:"))
        data_time = int(input("How many mounths of data do you want to see?"))
        calculator(money, percentage, data_time)
        
    elif time == 3:
        percentage = float(input("Enter the target percentage return for the time period:"))
        data_time = int(input("How many years of data do you want to see?"))
        calculator(money, percentage, data_time)
        
    else:
        print("Time not found")

