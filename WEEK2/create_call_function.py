#   # creating a function to add numbers
# def addition(a,b):
#     return(a + b)

# add_1 =addition (5,10)
# add_2 =addition (20,30)
# add_3 = addition (100,200)

# print(add_1)
# print(add_2)
# print(add_3)

# def force():
#   mass = float(input("Enter value of mass in kg: "))
#   acceleration = float(input("Enter value of acceleration in m/s:sqr"))
  
#   return mass * acceleration
# print(f"Force = {force()}N")

# # square root of a number
# def square_root():
#   number = float(input("Enter a numer: "))
  
  # without * args - regid: only works with exactly 3 scores
def average_3(a, b, c, d):
    return (a + b + c + d)  / 4
  
# with *args - flexible: works with any number of score

# def average(*args):
#     if not args:
#       return 0
#     return sum (args) / len(args)
  
# #print(F"Without *args: {average_3(2,4,6,8)}")
# print(f"With * args: {average(2,4,6,8)}")


# **kwards - flexible: accepts any number of keyword arguments
def build_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
my_profile = build_profile(
              name="Ikenna",
              age=30,
              profession="Developer",
              country="Nigeria"
             )
print(my_profile) 




