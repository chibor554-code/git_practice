
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# def sum_all(*args):
#     return sum(args)

# def build_config(**kwargs):
#     return kwargs

# greet tests
# print(greet("Ikenna"))
# print(greet("John", "Good morning"))
# print(greet("Ada", "Welcome"))

# sum_all tests
# print(sum_all(10, 20))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all())   

# build_config tests
# print(build_config(name="Ikenna", age=25))
# print(build_config(host="localhost", port=8080))
# print(build_config(theme="dark", language="English", mode="online"))


# def num_stat(numbers):
#     lowest = min(numbers)
#     highest = max(numbers)
    
#     return lowest, highest

# my_numbers = [5,2,5,1,10]
# lowest,highest = num_stat(my_numbers)
# print("minimum & maximum value")
# print(f" maximum value:{highest}")
# print(f" minimum value: {lowest}")

# name = "Global Ada"    # global 
 
# def introduce(): 
#     name = "Local Bob"    # local — DIFFERENT variable, same name 
#     print(name)           # Local Bob  (local shadows global) 
 
# introduce()    # Local Bob 
# print(name)    # Global Ada  (global is unchanged) 
 
# The local 'name' and global 'name' are TWO separate variables 

# rename_app = "techrise"
# user_count = 0
# def rename_app(new_name):
#     app_name = new_name
#     print(app_name)
# rename_app("Ikenna")


# score = int(input("Enter score: "))

# try:
#     score = int(input("Enter score: "))   # try the risky operation 
#     print(f"Your score is {score}") 
# except ValueError: 
#     print("That is not a valid number. Please try again.")
    
# try: 
#     number = int(input("Enter a number: ")) 
#     result = 100 / number 
#     print(f"Result: {result}") 
# except ValueError: 
#     print("Please enter a number, not text.") 
# except ZeroDivisionError: 
#     print("You cannot divide by zero.") 
# except Exception as e: 
#     print(f"Something unexpected happened: {e}")
    
file = None
try: 
    file = open("data.csv", "r") 
    content = file.read() 
except FileNotFoundError: 
    print("data.csv does not exist.") 
    content = None 
else: 
# Only runs if the file opened successfully 
    print(f"File loaded: {len(content)} characters") 
finally: 
# ALWAYS runs — close the file if it was opened 

    try: 
        file.close() 
    except: 
        pass   # file might not have opened — that is fine 
print("File operation complete.")
return content
read_file_safety("data.csv")