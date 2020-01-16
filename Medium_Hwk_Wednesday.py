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
a = [[2,4], [1,6]]
b = [[4,7], [2,3]]
new_big_list = []
# outer
for indexOne in range(len(a)):
    # a[index] b[index]
    # [2,4]       [4,7]
    new_small_list = []
    # inner
    for indexTwo in range(len(a[indexOne])):
        sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
        new_small_list.append(sum_of_values)
    new_big_list.append(new_small_list)
print(new_big_list)
        
