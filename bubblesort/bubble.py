import time

t1a=open("length1a.txt", 'r')
t1b=open("length1b.txt", 'r')
t1c=open("length1c.txt", 'r')
t2a=open("length2a.txt", 'r')
t2b=open("length2b.txt", 'r')
t2c=open("length2c.txt", 'r')
t3a=open("length3a.txt", 'r')
t3b=open("length3b.txt", 'r')
t3c=open("length3c.txt", 'r')
t4a=open("length4a1.txt", 'r')
t4b=open("length4b1.txt", 'r')
t4c=open("length4c1.txt", 'r')
t5a=open("length5a1.txt", 'r')
t5b=open("length5b1.txt", 'r')
t5c=open("length5c1.txt", 'r')

def bubble(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break

#small list

n=int(t1a.readline())
a=list(t1a.readline().split())
time1as=time.time()
bubble(a)
time1ae=time.time()
n=int(t1b.readline())
a=list(t1b.readline().split())
time1bs=time.time()
bubble(a)
time1be=time.time()
n=int(t1c.readline())
a=list(t1c.readline().split())
time1cs=time.time()
bubble(a)
time1ce=time.time()
time1e=(time1ae+time1be+time1ce)/3
time1s=(time1as+time1bs+time1cs)/3
print("test 1 time: ", time1e-time1s," 50 elements")

#medium list

n=int(t2a.readline())
a=list(t2a.readline().split())
time2as=time.time()
bubble(a)
time2ae=time.time()
n=int(t2b.readline())
a=list(t2b.readline().split())
time2bs=time.time()
bubble(a)
time2be=time.time()
n=int(t2c.readline())
a=list(t2c.readline().split())
time2cs=time.time()
bubble(a)
time2ce=time.time()
time2e=(time2ae+time2be+time2ce)/3
time2s=(time2as+time2bs+time2cs)/3
print("test 2 time: ", time2e-time2s," 10000 elements")

#large list

# n=int(t3a.readline())
# a=list(t3a.readline().split())
# time3as=time.time()
# bubble(a)
# time3ae=time.time()
# n=int(t3b.readline())
# a=list(t3b.readline().split())
# time3bs=time.time()
# bubble(a)
# time3be=time.time()
# n=int(t3c.readline())
# a=list(t3c.readline().split())
# time3cs=time.time()
# bubble(a)
# time3ce=time.time()
# time3e=(time3ae+time3be+time3ce)/3
# time3s=(time3as+time3bs+time3cs)/3
# print("test 3 time: ", time3e-time3s," 1000000 elements")

#mostly sorted list

n=int(t4a.readline())
a=list(t4a.readline().split())
time4as=time.time()
bubble(a)
time4ae=time.time()
n=int(t4b.readline())
a=list(t4b.readline().split())
time4bs=time.time()
bubble(a)
time4be=time.time()
n=int(t4c.readline())
a=list(t4c.readline().split())
time4cs=time.time()
bubble(a)
time4ce=time.time()
time4e=(time4ae+time4be+time4ce)/3
time4s=(time4as+time4bs+time4cs)/3
print("test 4 time: ", time4e-time4s," mostly sorted")

#reverse sorted list

n=int(t5a.readline())
a=list(t5a.readline().split())
time5as=time.time()
bubble(a)
time5ae=time.time()
n=int(t5b.readline())
a=list(t5b.readline().split())
time5bs=time.time()
bubble(a)
time5be=time.time()
n=int(t5c.readline())
a=list(t5c.readline().split())
time5cs=time.time()
bubble(a)
time5ce=time.time()
time5e=(time5ae+time5be+time5ce)/3
time5s=(time5as+time5bs+time5cs)/3
print("test 5 time: ", time5e-time5s," reverse sorted")