# # mathematics and pysics Modules

# #kinetic energy
# def kinetic_energy(mass, velocity):
#     """_summary_
#     Ages:
#     mass (flat):mass of a body, unit is kg_
#     velocity (float): _velocity of the body in m/s_
#     """
#     ke = 0.5 * mass * velocity
#     return ke

# # pressure
# def pressure(force, area):
#     """_summary_
#     Ages:
#     force (float): _discription_
#     area (type): discription_
#     """
#     pressure = force/area
#     return pressure

# # Power
# def power(current, voltag):
#    """_summary_
#    Args:
#    voltage (float): _voltage in volts_
#    current (float): _current in amperes_
#    """
#    resistance = voltag / current
#    return resistance

# # Mathematics functions
# def factorial(n):
#     """_summary_
#     Args:
    
#hellofunction
# def make_greetings():
#     message = "Hellow, Techrise"
#     print(message)
# make_greetings()
# print(message)
     
     # Global function
name = "Ikenna Chibor"
def make_greeting():
    global message
    message = f"Hellow {name} Welcome to Techrise"
    print(message)
make_greeting()
print(message)
