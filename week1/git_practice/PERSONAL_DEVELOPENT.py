# Add new item to set

# students = {"John", "Favour", "Ada"}
# students.add("Chioma")
# print(students)

# # use clear method to clear # Add new item to set

# studets = {"John", "Favour", "Ada"}
# students.clear() # this will erase every item from the set, but the set still exist
# print(students)

# # copy method, this will save the list before making changes

# students = {"John", "Favour", "Ada"}
# backup_students = students.copy()
# print("original:", students)
# print("backup:", backup_students)

# # lets modify the list
# students= {"John", "Mary", "David"}

# students.add("sarah")
# print("original:", students)
# print("backup:", backup_students)

# # Pop method, removes and returns an item from the set

# students = {"John", "Favour", "Ada"}

# # Add a new student

# students.add("sarah")
# print("after add:", students)

# # Creat a backup

# backup_students= students.copy()
# print("Backup:", backup_students)

# # Select a random winner

# winner = students.pop()
# print("winner:", winner)
# print("remaining student:", students)

# # clear the class
# students.clear()
# print("after clear:", students)

# #exercise 6:3b
# #Tuple

# cities = ("lagos", "abuja", "abia")
# # print the second city
# print(cities[1])
# # upack the tuple into separate variable
# city1, city2, city3 = cities
# # print the unpacked variables
# print(city1)
# print(city2)
# print(city3)


# # SET
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# # Convert to a set (removes duplicates)
# unique_numbers = set(numbers)

# # Convert back to a sorted list
# sorted_numbers = sorted(unique_numbers)

# print(sorted_numbers)

# # Create two sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Find the intersection
# common_numbers = set1.intersection(set2)

# print(common_numbers)

# # - Escape sequences 
# print("Name: ikenna \nAge: 50")


# x = 10
# if x >5:
#      print("x is greater 5")
# else:
#     print("x is not greaer than 5")

# 5 == 5
# 5 == 6
# print(5 == 5)
# print(5 == 6)

# 8 >= 8
# 7 >= 6
# print(8 >= 8) 
# print(7 >= 8)
   
# 9 > 8
# 8 > 8
# print(9 > 8)
# print(8 > 8)

# grade checker
# score = int(input("Enter your score"))
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C:"
# elif score >= 50:
#     grade = "C"
# else:
#     grade = "F"
    
# print(f"Your gade: {grade}")


# shopping cart discount
# total = float(input("cart total (₦):" ))
# if total >= 50000:
#     discount = 0.20
# elif total >= 20000:
#     discount = 0.10
# elif total >= 10000:
#     discount = 0.05
# else:   discount = 0.0

# savings = total * discount

# final_total = total * (1 - discount)
# print(f"final total after discount: ₦{final_total:,.2f}")
# print(f"you saved: ₦{savings:,.2f}")

# shoe = input("buy shoe color:")
# if shoe == "black":
#     print("buy the shoe")
# else:
#     print(f"buy_mango")
    
portions = int(input("how many portion of jollof rice"))
if portions >= 10:
    total_price = portions * 800
    label = "Bulk order - big discount"
elif portions >= 5:
    total_price = portions * 1000
    label = "Group order - small discount"
elif portions >= 2:
    total_price = portions * 1200
    label = "standard price."
elif portions == 1:
        total_price = 1500
        label = "single portion - premium price."
else:
    print("Please enter a valid number.")
if portions > 0:
    print(f"Total: ₦{total_price} - {label}")
    
 
    