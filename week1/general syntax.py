



# # # this is the list used in for loop example

# # scores = [70, 30, 50, 45, 60]
# # for score in scores:
# #     print(f"This is yor score: {score}")
    
# # ages = []
# # user_age = input("How old are you?: ").strip()
# # if user_age .isdigit():
# #     ages.append(user_age)
# # else:
# #     print("Write your age in figure")
# # print(ages)

# # using for loop on dictionary
# db_config = {
#     "host": "db.techrise.ng",
#     "port": 5432,
#     "name": "analytics_db",
#     "max_connections": 50
# }
# for key in db_config:
#     print(key)
    
#     # iltrating over dictionary values
#     for value in db_config.values():
#         print(value)
        
# # looping over a key and values pair
# for key, value in db_config.items():
#     print(f"    {key}: {value}")

# sales_data = {
#     "North":    [120000, 148000, 148000],
#     "South":    [98000, 101000, 115000],
#     "East":    [210000, 19800, 22500] 
# }
# for key in sales_data:
#     print(key)
#     for values in sales_data.values():
#         print(values)

# for region, monthly_figures in sales_data.items():
#     print(f"\nRegion: {region}")
#     total = 0
# for month_index, revenue in enumerate(monthly_figures, start=1):
#     print(f"  month {month_index}: N{revenue:,}")
#     total += revenue
# print(f"  TOTAL: N{total:,}")

    
    
# a list of 5 items
# list = ["ada", "eze", "okon", "urenna", "ella"]
# print(list[1:4])

# # list comprehension
# raw_emails = [ "ada@techrise.ng","ezecompany.com","okon@goofle.ng" ]
# cleaned_email = []
#     cleaned_emails

# while loop condition
# count = 0
# while count <= 4:
#     print("we have eaten lunch")
#     count +=1
    
# count = 1
# ages = []
# while count <=5:
#     user_age = input("How old are you:")
#     if user_age.isdigit():
#         ages.append(user_age)
#     else:
#         print("write your age in figure")
#     count +=1
# print(ages)    

# for age in ages:
#     print(f"I am {ages} year old.")


# even_numbers = [2,4,6,8,10,12,14,16,18,20]
# for nums in even_numbers:
#     print(nums)


# even_numbers = [2,4,6,8,10,12,14,16,18,20]
# for nums in even_numbers:
#     print(nums, end="," )

# for i in range(5):
#     print(i)
    
    
# for i in range(5):
#         print(i, end=",")
    
    
# for i in range(1,5):
#     print(i)
    
# for i in range(0,20,4):
#     print(i) 
     
# for i in range (-10, 20,4):
#     print(f"    {i}", end=" ")
# print()

# print(" countdown:")
# for i in range(10,0,-2):
#     print(f"    {i}", end=" ")
# print()

# looping over a string
# print("\n[3] loop Over a string  (character by character)")
# cohort = "Techrise"
# for ch in "Techrise":
#     print(f"    {ch}", end=" ")
# print()

# -enumerate-
# students = ["Ada", "Kemi", "Tunde"]
# print("\n[4] enumurate() - index AND value together")
# for index, name in enumerate(students):
#     print(f"    position {index}: {name}")
    
    
    
# students = ["Okon", "Blessing", "Ada", "Kemi", "Tunde"]
# print("\n[4] enumurate() - index AND value together")
# for index, name in enumerate(students):
#     print(f"    position {index}: {name}")

# students = ["Ada", "Kemi", "Tunde"]
# for index, name in enumerate(students, start=1):
#     print(f" {index}. {name}")
    
    
# loop control: break, continue, pass, else -
# print("\n[5] loop control keyword")

# print(" continue - skip even numbers:")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(f"    {i}", end =" ")
# print()
 

# print(  "break _ stop at 5:")
# for i in range (10):
#     if i == 5:
#          break
#     print(f"    {i}", end=" ")


#print(" else_runs if beak was never hit:")
# for n in [1,3,5]:
#     if n ==4:
#         break
# else:
#     print("  4 not found in the list")


# print("    pass- placeholder (empty block):")
# for i in range(3):
#     pass
# print("    (loop finished - pass did nothing)")

# netsed loop
# print("\n[6] Nested loops - maltiplication table")
# for i in range(1, 4):
#     for j in range(1,4):
#         print(f"    {i} x {j} = {i*j}")
        
        
        # class work
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#      print("FizzBuzz")
#     elif i % 3 == 0:
#          print("Fizz")
#     elif i % 5 == 0:
#          print("Buzz")
#     else:
#         print(i)   

    # class work
    
students = {
    "First_name": "Ikenna",
    "Last_name": "Chibor",
    "Age": 50,
    "Course": "Enterprise_python"
}

for key, value in students.items():
    print(key, ":", value)
    


records = [
    {"student_number": 1, "name": "Chioma", "score": 85},
    {"student_number": 2, "name": "Bob", "score": 90},
    None,
    {"student_number": 4, "name": "David", "score": 78},
    {"student_number": 5, "name": "Eve", "score": 92},
    None,
    {"student_number": 7, "name": "Grace", "score": 88},
    {"student_number": 8, "name": "Henry", "score": 81}
]

processed = 0
skipped = 0

for record in records:
    if record is None:
        print("Skipping corrupt record")
        skipped += 1
        continue

    print(record["student_number"], record["name"], record["score"])
    processed += 1

print("\nProcessed:", processed)
print("Skipped:", skipped)

# Retry processing

attempt = 1

while attempt <= 3:
    print("Attempt", attempt)

    if attempt == 3:
        print("Processing successful!")
        break

    print("Processing failed.")
    attempt += 1


#            LISTS

fruits = ["apple", "banana", "cherry"]
# Access (index starts at 0)
print(fruits[0]) # apple
print(fruits[-1]) # cherry ← negative index counts from end


# Modify

fruits[1] = "blueberry" # replace
fruits.append("orange") # add to end
fruits.insert(0, "mango") # insert at position 0
fruits.remove("apple") # remove by value
popped = fruits.pop() # remove and return last item

# Slicing — [start:stop] — stop is excluded
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10] ← reversed

# Useful methods
numbers.sort() # sort ascending in-place
numbers.reverse() # reverse in-place
length = len(numbers) # count items

