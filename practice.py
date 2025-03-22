# for num in range(10,0,-1):
#     print(num,end=" ")

# string=input('enter the string : ')
# if string==string[::-1]:
#     print(f'{string} is palindrome')
# else: 
#     print(f'{string} is notpalindrome')


num1=10
num2=20

# temp=num1
# num1=num2
# num2=temp
# print(num1,num2)


# num1,num2=num2,num1
# print(num1,num2)


# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(num1,num2)

"'Write a Python program that modifies a list of numbers such that even numbers are decreased by 1 and odd numbers are increased by 1. Given a list [1, 2, 3, 4], return the modified list.'"
# list=[1,2,3,4,5,6,7,8,96]
# new_list=[]
# for num in list:
#     if num%2==0:
#         new_list.append(num-1)
#     else:
#         new_list.append(num+1)

# print(new_list)

"Write a Python program to reverse a given list and then create a new list containing the squares of the reversed list "
"elements. Given [1, 2, 3, 4, 5, 6], print the squared values."
"Using the original list and the squared values list, create a dictionary where the original list elements are keys"
" and their squared values are the corresponding values."

# list=[1,2,3,4,5,6]
# reverse=list[::-1]
# new_list=[]
# for num in reverse:
#     new_list.append(num**2)
# print(new_list)

# dic1={}
# for value in range(len(list)):
#     dic1[list[value]]=new_list[value]
# print(dic1)

# find ascii value of character whose ascii value exceeds 78 and also xalculate sum of such character

# list1=[1,2+3j,'hi','52:65','hi==bye']
# new_list=[]
# for value in list1:
#     if type(value) == str:
#         for char in value:
#             if ord(char)>=78:
#                 new_list.append(ord(char))
# print(new_list)
# sum=0
# for value in new_list:
#     sum+=value
# print(sum )

# find prime number upto n number

# num=int(input('enter the number :'))
# # prime_numbers = []
# for Prime in range(2, num + 1):
#     count=0
#     for n in range(2,Prime):
#         if num % Prime==0:
#             count+1
#         else:
#             print(Prime)
            # prime_numbers.append(Prime)    
        
          
# print(prime_numbers)

# list1=[1,2,3,4,5,6,7]
# reverse=list1[::-1]
# print(reverse)


# l=[52,65,82,96,74,78]
# l_char=[]
# for num in l:
#     l_char.append(chr(num))
# print(l_char)


# string method

# upper
# string=input('enter the string : ')
# print(string.upper())
# # lower
# print(string.lower())
# # swapcase
# print(string.swapcase())
# #casefold
# print(string.casefold())
# # count
# print(string.count('a'))
# # find
# print(string.find('a'))
# replace
# print(string.replace('a','b'))
# join
# list1=['a','b','c']
# print('@'.join(list1))
# startswith
# print(string.startswith('d'))
# print(string.endswith('d'))

# common factor for given number

# number=int(input('enter the number:'))
# common_factor=[]
# num=1
# sum=0
# while num<number:
#     if number%num==0:
#         common_factor.append(num)
#         sum+=num
#         num+=1
#     else:
#         num+=1
# if sum==number:
#     print(f'perfect number{number}')
# else:
#     print(f'not perfect')
# print(f'common factor number :{common_factor}')
# print(f'the sum of factor number {sum}')








# odd nunmber 100 to 1
# odd_number=[]
# for i in range(100,0,-1):
#     if i%2!=0:
#         odd_number.append(i)
# print(f'the odd number 100 to 1 {odd_number}')

# # print common factor for given two number
# num1= int(input('enter the first number:'))
# num2= int(input('enter the second number:'))
# common_factor=[]
# num=1
# while num<=num1 and num<=num2:
#     if num1%num==0 and num2%num==0:
#         common_factor.append(num)
#         num+=1
#     else:
#             num+=1
# print(common_factor)


# num=1
# while num<=5:
#     print('python')
#     num+=1

# num=int(input('enter the number : '))
# start=0
# while start<=num:
#     print(start)
#     start+=1

# start=int(input('enter the start number : '))
# end =0
# while start>=end:
#     print(start)
#     start-=1


num=int(input('enter the num :'))

if num%2==0:
    sum=0
    while num!=0:
        last_digit=num%10
        sum+=last_digit
        num//=10
print(sum)


    










            





