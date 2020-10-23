drug = int(input("Enter the drug number here-->"))
drug2 = str(input("Enter the drug name here-->"))
purchase = int(input("Enter the unit purchased here-->"))
print("packing unit(I=Injection, B=Bottle,T=Tablet)")``
packing = str(input("Enter the packing unit here-->"))
rate = int(input("Enter the rate per unit here-->"))

amt1 = (purchase * rate) 
total = amt1 + (amt1 * 7.5 / 100)

if packing == "I":
    amt3 = total - (total * 7.5 /100)
    print("----------------------------------")
    print("The drug no. is-->", drug)
    print("The drug name is-->", drug2)
    print("The unit purchase is-->", purchase)
    print("Packing unit is-->", packing)
    print("Sales tax is--> 7.5%")
    print("Final amount is-->", amt3)
    print("----------------------------------")

elif packing == "B":
    amt3 = total - (total * 5 /100)
    print("----------------------------------")
    print("The drug no. is-->", drug)
    print("The drug name is-->", drug2)
    print("The unit purchase is-->", purchase)
    print("Packing unit is-->", packing)
    print("Sales tax is--> 7.5%")
    print("Final amount is-->", amt3)
    print("----------------------------------")

elif packing == "T":
    amt3 = total - (total * 2.5 /100)
    print("----------------------------------")
    print("The drug no. is-->", drug)
    print("The drug name is-->", drug2)
    print("The unit purchase is-->", purchase)
    print("Packing unit is-->", packing)
    print("Sales tax is--> 7.5%")
    print("Final amount is-->", amt3)
    print("----------------------------------")