# list_one = [7, 4, 3]
# list_two = [9, 4, 7]
# new_list = []
# for index in range (len(list_one)):
#     new_number = list_one[index] * list_two[index]
#     new_list.append(new_number)
#     print(new_number)
# print(new_list)
#For each item in list
#make a new number equal to the first items in each list multiplied together
#add the new number to our new list
#print the new list.

#Matrix Addition
# ad the 2 maticies together, i.e 2+4. 4+7, etc
# a = [[2,4], [1,6]]
# b = [[4,7], [2,3]]
# new_big_list = []
# outer
# for indexOne in range(len(a)):
#     # a[index] b[index]
#     # [2,4]       [4,7]
#     new_small_list = []
#     # inner
#     for indexTwo in range(len(a[indexOne])):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)
# 4 De-Dup
# myList = [1, 2, 3, 4, 9, 8, 9]
# copiedList = []
# copiedList = myList.copy()
# #print(copiedList)
# copiedList = list(dict.fromkeys(copiedList))
# print(copiedList)
#5
# sentence = input("insert A, E, G, I, O, S, T ")
# for char in sentence:
#     if (char == 'A'):
#         print('4')
#     elif (char == 'E'):
#         print('3')
#     elif (char == "G"):
#         print('6')
#     elif (char == 'I'):
#         print('1')
#     elif (char == "S"):
#         print("5")
#     elif (char == "T"):
#         print("7")
#     elif (char == "O"):
#         print('0')
#     print(sentence)
# SHOULD OUT PUT LIKE THIS "1 L0V3 D16174L " < GET HELP
#6
#word = input("Type any word with vowels ")


#7
#Caeser Cipher
#cipherString = input("")


#SMALL
#1
# sumList = []
# amountOfDigits = int(input("How many numbers do you have? "))
# for i in range (amountOfDigits):
#     numbers = int(input("Enter a number"))
#     sumList.append(numbers)
# print("The sum of the numbers in the list is ", sum(sumList))

#2
largestNumb = []
amount_of_numbers = int(input("Enter how many numbers their will be in the list "))
for i in range (amount_of_numbers):
    number_entry = int(input("Enter a number "))
    largestNumb.append(number_entry) 
print("The largest number in the list is ", max(largestNumb))


