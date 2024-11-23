charges=0.51
daycharge=charges*24
monthcharge=daycharge*30

print("Hourly charges: $ "+str(charges))

print("Charges per day: $ "+str(daycharge))

print("Charges per month: $ "+str(monthcharge))

print("Charges per day: $ {:.2f}".format(daycharge))

print("Charges per month: $ {:.2f}".format(monthcharge))
