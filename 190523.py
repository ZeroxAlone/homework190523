"""
Is your secret number 83?
Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly. 
Game over. Your secret number was: 83
"""
"""
import random
r=random.randint(0,100)
print("Is your secret number",r,"?")
s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
a=r-1
b=r+1
a!=b
while 0==0:
    if s=="h":
        c=random.randint(0,a)
        c<a
        print("Is your secret number",c,"?")
        s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
    elif s=="l":
        c=random.randint(b,101)
        c>b
        print("Is your secret number",c,"?")

        s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
    elif s=="c":
        break
print("Game over. Your secret number was:",c)
"""
#question set
#1

b=eval(input("balance = "))
a=eval(input("annualInterestRate = "))
m=eval(input("monthlyPaymentRate = "))
for i in range(12):
    b=(b-b*m)*(1+a/12)
print("Month 12 Remaining balance:",round(b,2))

#2
b=eval(input("balance = "))
a=eval(input("annualInterestRate = "))
for i in range(12):
    
    z=b/12-b*(1+a)/(1+a/12)
    d=(b-z*12)*(1+a/12)/12/(b*(1+a))
print("""Result Your Code Should Generate:
-------------------
Lowest Payment: """,z)

#2不对 3不会









