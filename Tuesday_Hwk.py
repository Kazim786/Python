# 1 & 2
total_bill = float(input("What is your total? "))
service = input("What was the level of service? Good, fair, or bad ")
how_many_people = float(input("How many people are there? "))
if (service == "Good"):
    tip = total_bill * .20
    total_amount = tip + total_bill
    print(total_amount)
    the_split = total_amount/how_many_people
    print(the_split)
elif (service == "fair"):
    tip = total_bill * .15
    total_amount = tip + total_bill
    print(total_amount)
    the_split = total_amount/how_many_people
    print(the_split)
elif (service == "Bad"):
    tip = total_bill * .10
    total_amount = tip + total_bill
    print(total_amount)
    the_split = total_amount/how_many_people
    print(the_split)
else:
    print("INVALID ENTRY ")
