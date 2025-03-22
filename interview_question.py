# "Write a Python program to swap two numbers without using a temporary variable. Given num1 = 10 and num2 = 20, swap their values and print the result.

# num1=10
# num2=20

# using temp

# temp=num1
# num1=num2
# num2=temp
# print(f'num1: {num1},num2: {num2}')

# using operator

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(f'num1: {num1},num2: {num2}')

# num1,num2=num2,num1
# print(f'num1: {num1},num2: {num2}')

####################################################################################

"'Write a Python program that modifies a list of numbers such that even numbers are decreased by 1 and odd numbers are increased by 1. Given a list [1, 2, 3, 4], return the modified list.'"
# list1=[21,32,34,2]
# new_list=[]
# for num in list1:
#     if num % 2 == 0:
#         new_list.append(num-1)
#     else:
#         new_list.append(num+1)

# print(new_list)

###############################
"Write a Python program to reverse a given list and then create a new list containing the squares of the reversed list elements. Given [1, 2, 3, 4, 5, 6], print the squared values."
"Using the original list and the squared values list, create a dictionary where the original list elements are keys and their squared values are the corresponding values."
# list1=[13,54,23,19]
# revere_list=list1[::-1]
# new_list=[num**2 for num in revere_list ]
# print(new_list)

# dict1={}
# for value in range(len(list1)):
#     dict1[list1[value]]=new_list[value]

# print(dict1)

##############################################################################

# Write a Python program that takes a sentence as input, splits it into words, and creates a dictionary where:
# Keys are the reversed second halves of each word.
# Values are the lengths of the words.
# For example, given "Python is easy", return a dictionary with the transformed keys and their respective word lengths.


# sentance=input("enter any sentsnce")
# word=sentance.split()
# mid=

########################################################################