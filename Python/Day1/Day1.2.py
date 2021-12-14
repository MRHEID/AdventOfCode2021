import math

input = "D:\\GIT\\AdventOfCode2021\\Python\\Day1\\test.txt"
increases = 0
A = None
B = None
C = None
sum = None
lastSum = None

with open(input,"r") as f:
    max_i = math.trunc(len(f.readlines()) / 3)
    for line in f.readlines():
        if A is None:
            print ("A is Empty")
        elif B is None:
            print ("B is Empty")
        elif C is None:
            print ("C is Empty")
        else:
            sum = A + B + C
            if sum > lastSum:
                increases = increases + 1
        C = B
        B = A
        A = line
print (increases)