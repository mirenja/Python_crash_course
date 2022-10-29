# def display_message():
#     """displays chapter learning targets"""
#     print("Chapter 8 is on functions")
# display_message()


# def fav_book(title):
#     """print out your fav book from the para"""
#     print(f"One of my favorite books is {title.title()}")

# fav_book("Americanah")


# # Chapter 6-Dictionaries

# rand_person = {}
# rand_person['first_name'] = 'jules'
# rand_person['last_name'] = 'She'
# rand_person['age'] = '28'
# rand_person['city'] = 'Nairobi'
# print(rand_person)

# print(f"{rand_person['first_name'] }")
# print(f"{rand_person.get('age') }")

# for key, value in rand_person.items():
#     print(f"\n key:{key}")
#     print(f"\n value: {value}")


# Task 2:start with an empty dictionary
# fav_num = {}
# fav_num['Jane'] = 7
# fav_num['jules'] = 13
# fav_num['Lindy'] = 9
# fav_num['Lynn'] = 12

# print(fav_num)

# for name, number in fav_num.items():
#     print(f"{name}'s favorite number is {number}")

# new_words = {
#     "list":"An mutable group of items",
#     "dictionary":"key value pairs",
#     "function" : "block of code doing a specific task"
# }

# for word, meaning in new_words.items():
#     print(f"\n{word}")
#     print(f"{meaning}")

#task 6-6 polling
# fav_num = {}
# fav_num['Jane'] = 7
# fav_num['Jules'] = 13
# fav_num['Lindy'] = 9
# fav_num['Lynn'] = 12
# fav_num['Sly'] = 30
# fav_num['Eve'] = 22

# print(fav_num)
# people = ['Jane','Henry','Jules','Peter','Lynn']

# for person in people:
#     if person.title() in fav_num.keys():
#         print(f"thanks {person} for responding")
#     else:
#         print(f"Hello {person} please take the poll")

# Nesting

# rand_person = {}
# rand_person['first_name'] = 'jules'
# rand_person['last_name'] = 'She'
# rand_person['age'] = '28'
# rand_person['city'] = 'Nairobi'

# rand_person2 = {}
# rand_person2['first_name'] = input("first name")
# rand_person2['last_name'] = input("second name")
# rand_person2['age'] = input("age")
# rand_person2['city'] = input("city")

# rand_person3 = {}
# rand_person3['first_name'] = input("first name")
# rand_person3['last_name'] = input("second name")
# rand_person3['age'] = input("age")
# rand_person3['city'] = input("city")


# people = []

# for person in range(1,4):
#     rand_person2 = {}
#     rand_person2['first_name'] = input("first name")
#     rand_person2['last_name'] = input("second name")
#     rand_person2['age'] = input("age")
#     rand_person2['city'] = input("city")
#     people.append(rand_person2)

# people = [{'first_name': 'jane', 'last_name': 'njoro', 'age': '28', 'city': 'nyahururu'}, {'first_name': 'lindy', 'last_name': 'obange', 'age': '30', 'city': 'kisumu'}, {'first_name': 'lynn', 'last_name': 'achieng', 'age': '30', 'city': 'dala'}]





# for person in people:

#     print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}")
# print("\n")


# for person in people:
#     for attribute, value in person.items():
        
#         print(f"{attribute} {value.title()}")
#     print("\n")
        
        
# task 6.8

pets = []

for pet in range(1,4):
    animal = {}
    animal['owner'] = input("Owner")
    animal['type'] = input("kind of animal")
    animal['name'] = input("fur baby's name")

    pets.append(animal)
print(pets)

for pet in pets:
    for key,value in pet.items():
        print(f"{key}: {value}")
    print(f"{pet['owner'].title() } has a little {pet['type']} fur baby named {pet['name'].title()}")
    print("\n")



