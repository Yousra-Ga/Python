

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
    
    mounth_amount= input("entre your mounth amount:")
 
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

with open("expense.csv", "w") as f:
    f.write("date,category,note,amount\n")
    for enter in enters:
        x = f"{enter['date']},{enter['category']},{enter['note']},{enter['amount']}\n"
        f.write(x)

with open("expense.csv","r") as f:
    print("\nenters are:")
    print(f.read())
    f.close()
