from random import randint
abc = int(input("How many terms? "))

num1 = randint(1, 50)
num2 = randint(1, 50)


#num1, num2 = 0, 1
count = 0


if abc <= 0:
   print("Please enter a positive integer")

elif abc == 1:
   print("Fibonacci sequence upto",abc)
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < abc:
       print(num1)
       nth = num1 + num2
       # update values
       num1 = num2
       num2 = nth
       count += 1
