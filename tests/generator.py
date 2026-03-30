import random

n= int(input())
a= [random.randint(1,100000) for i in range(n)]

with open("length.txt","w") as f:
    f.write(str(n) + "\n")
    f.write(" ".join (str(i) for i in a))