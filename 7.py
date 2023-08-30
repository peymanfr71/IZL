# 1) simple example
for i in range (5):
    print ("i:", i)
    break
    print ("after break inside of loop")
print ("after break outside of loop")
# # 2) if i equals to "2" => then break
for zizi in range (5):
    if zizi == 2:
        break
    print ("zizi:", zizi)
print ("after, outside, done")
# # 3) continue statement in python
for number in range (5):
    print ("number:", number)
    continue

for numbers in range (5):
    if numbers == 2:
        continue
    print ("numbers:", numbers)
# # 4) prompt the user with nnumbers until they entre "exit"
while True:
    enter = (input("please enter the number: "))
    if enter == "exit":
        print ("exited")
        break
# # 5) prompt the user two numbers then divide the first number by the second.
while True:
    first_number = input("first number: ")
    second_number = input("second number: ")
    if second_number == "0":
        print ("Try Again!")
        continue
    division = float (first_number) / float (second_number)
    print ("division:", division)
# ###
while True:
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))
    if second_number == 0:
        print("Try Again!")
        continue
    division = first_number / second_number
    print("Division: {:.2f}".format(division))
    user = input("do you want to continue? (yes/no) ")
    if user.lower() == "no":
        print ("exiting...")
        break
for i in range (3):
    for x in range (2):
        print ("(i, x):", (i, x))
    if i == 1:
        print ("i equal to 1")
for i in range(3):
    print ("i", i)
    for j in range(2):
        print ("j", j)
        if i == 2:
            print ("something!", (i, j))
