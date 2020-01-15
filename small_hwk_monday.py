#1 
# name = input("What is your name? ")
# print(name)
# #1b
# if (len(name) > 0):
#     print("HELLO " + name.upper() + "YOUR NAME HAS " + str(len(name)))
# #len(name) is an integer, had to parse it so it can be a string.

#Madlib
# user_input = input("What is your name?")
# fave_subject = input("Whats your favorite subject?")
# answer = "{}'s favorite subject is {}"
# print(answer.format(user_input, fave_subject))
#DayOfTheWeek
# day = int(input('What Day between (0-6) is it? '))
# if (day==0):
#     print("Sunday")
# if (day == 1):
#     print("Monday")
# if (day==2):
#     print("Tuesday")
# if (day == 3):
#     print("Wednesday")
# if (day == 4):
#     print("Thursday")
# if (day == 5):
#     print("Friday")
# if (day == 6):
#     print("Saturday")
# #
# if (day==0):
#     print("Sleep-in")
# if (day == 1):
#     print("work")
# if (day==2):
#     print("work")
# if (day == 3):
#     print("work")
# if (day == 4):
#     print("work")
# if (day == 5):
#     print("work")
# if (day == 6):
#     print("Sleep-in")
# temperature = int(input("Enter the temperature in Celsius"))
# fahren = (temperature * 9/5) + 32
# print(fahren)
# count = 0
# while(count < 10):
#     count += 1
#     print("The count is " + str(count)) #dont forget to convert count into a string to concactenate.
#Middle Part
TotalBill = float(input("What is the total bill?"))
service = input("What is the level of service? good, bad, or fair?")
tip = float()
if(service == "good"):
     tip = (TotalBill * .20)
     print("Tip is " ,tip)
elif(service == "fair"):
    tip = (TotalBill * .15)
    print("Tip is " ,tip)
elif(service == "bad"):
    tip == (TotalBill * .10)
    print("Tip is " ,tip)
else:
    print("Invalid entry")
TotalAmount = float(TotalBill + tip) 
print("The total amount is ",TotalAmount)


