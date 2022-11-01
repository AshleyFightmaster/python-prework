# Question 1: Write a function to print "hello_USERNAME!" 
# USERNAME is the imput of the function. 
# The first line of the code has been defined as below.
# def hello_name(user_name):

from ast import List


def hello_name(user_name):
        """Display a simple greeting."""
        print(f"hello_{user_name}!")

hello_name('username'.upper())

#Question 2: Write a python function,
#  first_odds that prints the odd numbers from 1-100 
# and returns nothing def first_odds():

def first_odds():
        """Display odd numbers from 1-100"""
        odd_numbers= list(range(1,100,2))
        print(odd_numbers)

first_odds()

#Question 3: Please write a Python function, 
# max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. 
# def max_num_in_list(a_list):


def max_num_in_list(list):
        """Return the max number of a given list"""
        list = (max(list))
        return list 
       
num = max_num_in_list([1,2,3,4])
print(num)

#Question 4:Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false). 
# def is_leap_year(a_year):

def is_leap_year(a_year):
       
        if a_year %4 == 0 and a_year %100 !=0 :
                return True
        elif a_year %400 != 0:
                return False
        
print(is_leap_year(1700))
  

#Question 5: Write a function to check to see if all numbers in the list are consecutive numbers.
#  For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. 
# def is_consecutive(a_list):

list_1 = [1,2,3,4]
list_2 = [5,6,7,9,10]
def is_consecutive(a_list):
        """Check if numbers in a list are consecutive or not."""
        for i in range(len(a_list)-1):
                if a_list[i] +1 != a_list[i+1]:
                        return False

        return True 

print(is_consecutive(list_1))
print(is_consecutive(list_2))
