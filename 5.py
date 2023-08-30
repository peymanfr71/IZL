age = int(input("your age: "))
if age >= 18:
    print ("permited")
else:
    print ("With parental permission")
# ##
age = int(input("your age: "))
parental_permission = input("do you have parental permission? (yes/no): ").lower() == "yes"
if age >= 18 and parental_permission:
    print ("permitted")
else:
    print ("not permitted")
# ##
age = int(input("your age: "))
parental_permission = input("do you have parental permission? (yes/no): ").lower() == "yes"
if age >= 18 or parental_permission:
    print ("permitted")
else:
    print ("not permitted")
# ##
age = int(input("your age: "))
if not (age < 18):
    print ("permitted".upper())
else:
    print ("not permitted".upper())
