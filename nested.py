#ask user to enter their age
age = int(input("What is your age: "))
#ask user to enter if they are member or not
member = input("Are you a member (Y or N)?").upper()
#calculate entry price based on age and member status
if age< 17:
    if member=="Y":
        ticket_price=0
    else:
        ticket_price=6
else:
    if member=="Y":
        ticket_price=5
    else:
        ticket_price = 10
print("Your entry price is £",ticket_price)

