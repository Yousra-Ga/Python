

from datetime import datetime

enters= []
exit_choise = "no"

def check_date(the_date):
    try:
        datetime.strptime(the_date,"%d.%m.%Y")
        return True
    except:
        return False
    
while exit_choise != "yes":
    date= input("give the date:")

    if not check_date(date):
        print("The date must be in format tt.mm.jjjj")
        continue

    category = input("give the category:")
    note= input("give the note:")
    amount = float(input("give the anount:"))
    expense={
        "date" : date,
        "category" : category,
        "note" : note,
        "amount" : amount
    }
    enters.append(expense)
    exit_choise = input("you want to exit(yes/no):")

for enter in enters:
    print(f"enters are:{enter}")
