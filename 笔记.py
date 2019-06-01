#1
a=eval(input("Please input your grade:"))
if 90<=a<=100:
    print("A")
elif 80<=a<90:
    print("B")
else:
    print("C")
    
#2
n=int(input(""))
i=1
while n>0:
    i*=n
    n=n-1
print(i)

#3
n=int(input(""))
i=1
while True:
    i*=n
    n=n-1
    if n==0:
        break
print(i)

#4
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
n=int(input(""))
print(f(n))

