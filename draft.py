import time
import datetime

# Print initial info
print("KMPCL LIMITED")
time.sleep(1.5)
print("Branch: Balwanthapoor")
time.sleep(1.5)

# Get current date, day, and time
current_date = datetime.date.today()
current_day = datetime.datetime.now().strftime("%A")
current_time = datetime.datetime.now().time()

print(f"Date: {current_date}")
print(f"Day: {current_day}")
print(f"Time: {current_time}")
time.sleep(1.5)

# Session input
session = input("Session = M for Morning, E for Evening:").strip().upper()
if session == "M":
    print("Morning")
elif session == "E":
    print("Evening")
else:
    print("Invalid choice! Please select a valid option.")
    exit()  # Exit the program if invalid input
total_quantity=0.0
total_fat=0.0
total_entries=0
# Membership number and milk details input
while True:  # Keep asking for membership and milk details until the user decides to stop
    num = int(input("Enter membership number: "))
    
    # Determine type of milk based on membership number
    if num < 300:
        print("Buffalo milk")
    else:
        print("Cow milk")
    
    # Quantity and fat input
    milk = float(input("Quantity in L: "))
    fat = float(input("Fat: "))
    total_quantity +=milk
    total_fat +=fat
    total_entries +=1
    # Ask if the user wants to enter another membership number
    count = input("Enter another membership? (Y/N): ").strip().upper()
    if count != 'Y':
        break

if total_entries > 0:
    average_fat=total_fat / 2
else:
    average_fat=0.0
print("Total Quantity: ",total_quantity)
print(f"Average fat percentage: {average_fat:.2f}%")
print("Total Entries: ",total_entries)
print("---------------Thank You Have A Nice Day-----------------")
