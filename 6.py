# loops in python programming. (while)
x_time = 0
x_time += 1
while x_time < 15:
    print (x_time, "Hello World!")
    x_time = x_time + 3
# ##
# 1
iterable = "python"
for iterator in iterable:
    print ("iterator:", iterator)
# 2
for i in "letters":
    print ("i:", i)
# 3
for char in "python":
    print ("char:", char)
# 4
my_string = "LaNa"
for char in my_string:
    print (my_string, "loves you!")
# 5
sum = 0
for i in range(1, 19):
    sum += i
    print (f"{sum} + {i} = {sum + i}", end="\n")
print ("")
#
sum = 0
for i in range(1, 19):
    print (f"{sum} + {i} = {sum + i}")
    sum += i
# 6
print (range (0, 10))
print (list(range (0, 10)))
for i in range (10):
    print ("Hola!")
#
range(start = 0, stop = 50, step = 5)
for i in range (50, 0, -3):
    print ("what?:", i)
# 7
start = 50
stop = 0
step = -7.5
i = start
while i > stop:
    print("what?:", i)
    i += step
#
for char in "python":
    print (char)
    if char == "t":
        break
    print ("lililoop")
print ("loop ended")
print ("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
for char in "python":
    print (char)
    if char == "t":
        continue
    print ("lililoop")
print ("loop ended")
print ("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
for char in "python":
    print (char)
    if char == "t":
        pass
    print ("lililoop")
print ("loop ended")
