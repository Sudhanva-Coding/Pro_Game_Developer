#Write a Python program to sq  uare and cube every number in a given list of integers using Lambda
num = [12, 18, 23, 6, 9, 201, 1]
print("the original list of integers are : ", num)
print("\n")
square_num = list(map(lambda x: x **2, num))
print("the integers squared are : ",square_num)
print("\n")
cube_num = list(map(lambda x: x **3, num))
print("the integers cubed are : ",cube_num)

#Write a Python program to extract year, month, date and time using Lambda

import datetime
now = datetime.datetime.now()
print(now)
print("\n")
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))

#Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
#Original arrays:
#[1, 2, 3, 5, 7, 8, 9, 10]
#Number of even numbers in the above array: 3
#Number of odd numbers in the above array: 5

num2 = [1, 2, 3, 5, 7, 8, 9, 10]
print("the original list of integers are : ", num2)
evennum = len(list(filter(lambda x: (x %2 == 0), num2)))
oddnum  = len(list(filter(lambda x: (x %2 != 0), num2)))
print("\nnumber of even numbers are : ",evennum)
print("\nnumber of odd numbers are : ",oddnum)


#Write a Python program to add two given lists using map and lambda.
#Original list:
#[1, 2, 3]
#[4, 5, 6]
#Result: after adding two list
#[5, 7, 9]


num1 = [1, 2, 3]
num2 = [4, 5, 6]
print("Original list:")
print(num1)
print(num2)
answer = list(map(lambda x, y: x + y, num1, num2))
print("\nResult: after adding two list")
print(list(answer))

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i += 1


#Write a Python program to remove all elements from a given list present in another list using lambda


def list_comparison(list1, list2):
  result = list(filter(lambda x: x not in list2, list1))
  return result

list1 = [1, 6, 5, 7, 0, 2, 8, 10]
list2 = [1, 4, 9]

print("original lists", list1, list2)
print(" the final list after removal is : ", list_comparison(list2, list1))

#Write a Python program to calculate the product of a given list of numbers using lambda
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
import functools
def remove_duplicates(nums):
  result = functools.reduce(lambda x, y: x*y, nums, 1)
  return result

print("the product of the list numbers are : ", remove_duplicates(list))


#Write a Python program to remove None values from a given list using the lambda function.
#Original list:
#[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
#Remove None value from the said list:
#[12, 0, 23, -55, 234, 89, 0, 6, -12]

#What will be the output of the following Python function?

min(max(False,-3,-4), 2,7)
