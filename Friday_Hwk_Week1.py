
# # SMALL SECTION
# # 1

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# print(phonebook_dict["Elizabeth"])
# del phonebook_dict["Alice"]
# print(phonebook_dict)
# phonebook_dict["Kareem"] = "938-489-1234"
# print(phonebook_dict)
# phonebook_dict["Bob"] = "968-345-2345"
# print(phonebook_dict)

# Medium

#1 
letter_histogram = input("Please enter a word : ")
counts = {}
for word in letter_histogram:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts) 