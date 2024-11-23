chargesperhour=0.51
daycharge=chargesperhour*24
monthcharge=daycharge*30


print("One server per day: $ {:.2f}".format(daycharge))
print("One server per month: $ {:.2f}".format(monthcharge))
print("20 servers per day: $ {:.2f}".format(20*daycharge))
print("20 servers per month: $ {:.2f}".format(20*monthcharge))
budget=input("Enter your budget in $ : ")
days=float(budget)/daycharge
print("You can operate for {0} days with this budget of {1:.2f}".format(int(days),float(budget)))
