print("200 is a great number")
print(3.5)
print("20 days are "  + str(50) + " minutes")
print(20 * 24 * 60)
print(f"20 days are {20 * 24 * 60} minutes")
print(f"35 days are {35 * 24 * 60} minutes")
print(f"110 days are {110 * 24 * 60} minutes")

#string with concantenation
#Naming convention: convention for naming things
calculation_to_seconds=24 * 60 * 60
name_of_units = "seconds"
print(f"20 days are {20 * calculation_to_seconds} seconds")
name_of_unit = "hours"
def days_to_units():
  print(f"20 days are {20 * calculation_to_seconds} {name_of_units}")