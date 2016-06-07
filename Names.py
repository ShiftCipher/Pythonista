import names
import sys
import os

count = 1
file = open("data.csv", "w+")
for x in range(1,100):
    name = names.get_full_name()
    first_name = name.split(" ")
    first_name = first_name[0]
    file.write(name + "," + first_name + "@aol.com" + "," + str(count) + "\n");
    count = count + 1
    if count > 3:
        count = 1
file.close()
