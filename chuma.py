# num=int(input("enter the number"))
# if (num>99 and num<1000) or (num<-99 and num>-1000):
#     print("it is 3 digit number")

# nums=[1,2,3,4,5,6]

# new_nums=[]
# for num in nums:
#     new_nums.append(num*2)
# print(new_nums)

# odd or even
# num=int(input("enter the any number : "))
# if num%2!=0:
#     print("it is odd number")
# else:
#     print('it is even number')

# prime number
# number=int(input('enter a number :'))
# if number>1:
#     for num in range(2,number):
#         if number%num==0:
#             print(f'{number} is not prime number')
#             break
#     else:
#             print(f'{number} is prime number')
# else:
#     print(f'number is not prime number')

# factiorial
# number=int(input('enter the factorial number: '))
# fact=1
# start=1
# if number<0:
#     print('factorial does not support for negative number')
# elif number==1 or number==0:
#     print(f'the factorial {number} is 1')
# else:
#     while start<=number:
#         fact*=start
#         start+=1
#     print(f'the factorial of {number} is {fact}')

# fiboanacci
# number=int(input('enter the number :'))
# num1,num2=0,1
# count=0
# if number<=0:
#     print('negative number not supported in fibonaci1')
# else: 
#     while count<=number:
#         print(num1,end=" ")
#         curr_num=num1+num2
#         num1=num2
#         num2=curr_num
#         count+=1


# for _ in range(2):
# number=int(input('enter the number: '))
    # if number%2==0:
    #     print('even')
    # else:
    #     print('odd')

# number=int(input('enter the numnber : '))
# if number>1:
#     for num in range(2,number):
#         if number%num==0:
#             print('is not prime')
#             break
#     else:
#         print('is prime')
# else:
#     print('is not prime')


# num=int(input('enter the number'))
# num1,num2=0,1
# sum=0
# if num<0:
#     print('negative number not suported')
# elif num==0 or num==1:
#     print(f'the sum of {num} is 1')
# else:
#     while sum<=num:
#         print(num1,end=" ")
#         cur_num=num1+num2
#         num1=num2
#         num2=cur_num
#         sum+=1


# string methods
# string=eval(input('enter the string : '))
# single_string=""
# for val in string:
#     words=str(val)+" "
#     single_string+=words
# print(f"{single_string}")


# joining=" ".join(map(str,string))
# print(joining)
# words = ["Hello", "World", "Python"]
# sentence = " ".join(str(words))
# print((sentence))
# print(string.count('h'))
# print(string.find('n'))
# print(string.index('n'))
# print(string.center(60))
# print(string.rjust(60))
# print(string.rstrip('-'))
# print(string.split('\n',2))
# if string.islower():
#     print("upper",string.upper())
# elif string.isupper():
#     print("lower",string.lower())
# elif string.istitle():
#     print("capital",string.capitalize())

# string.split()

# list
# ###############################################
# list1=eval(input('enter the list : '))
# list2=[11, 21, 3, 14, 25, 0]
# list2.reverse()
# print(list2)


# print(list2.sort())
# sorted=list2.sort()
# print(list2)
# print(f'before changes  : {list1}')
# list1.extend(list2)
# print(list1)
# list1.insert(2,22)
# print(list1)
# list1.append('last')
# print(list1)

# result="".join(map(str,list2))
# print(result)
# result=""
# for num in list2:
#     result+=str(num)+" "
# print(result)

# new_list=list2.copy()
# print(new_list)

# list2.clear()

# list2.remove(6)
# list2.pop(0)
# list2.pop()

# print(list2.index(2))
# print(list2.count(2,2,5))


# set1={1,2,3,4,5,6,7}
# set2={8,9,10,11,12,13,7}

# result=set1.union(set2)
# print('union')
# print(result)

# print('intersection')
# result=set1.intersection(set2)
# print(result)

# print('diference')
# result=set1.difference(set2)
# print(result)

# print('sym-diference')
# result=set1.symmetric_difference(set2)
# print(result)


# print('update')
# result=set1.update(set2)
# print(set1)

# result=set1.difference_update(set2)
# print(set1)

# result=set1.intersection_update(set2)
# print(set1)

# result=set1.symmetric_difference_update(set2)
# print(set1)


# set1.add(-1)
# print(set1)


# dict1={1:'hai',2:'bye',3:'welcome',4:'to'}
# dict2={5:'our',6:'college'}

# print(dict1.setdefault(11,'hello'))
# print(dict1)



# print(dict1.items())
# dict1.popitem()
# print(dict1)

# dict1.update(dict2)
# print(dict1)
# print(dict1.values())

# dict1.pop(1)
# print(dict1)

# print(dict1.get(1))

# print(dict1.keys())
# print(dict1.values())
# new=dict1.copy()
# print(new)
# new=dict1.clear()
# print(dict1)

# number=int(input('enter the number to square : '))
# print(f'the square of{number} is {number**2}')

# list1=eval(input('enter the list : '))

# index=int(input('enter the index number: '))
# list1.pop(index)
# print(list1)

# print(list1[index])

# print(list1[-1])

# word=input('enter the word: ')
# print(word[::-1])


# number=int(input('enter the number : '))
# if number%2==0:
#     print(f'the given number {number} is even')
##############################################################################


# alphaphabets=input("enter the word : ")
# for alpha in alphaphabets:
#     if alpha in 'aeiou AEIOU':
#         print('it is vowel')
#         break
##############################################################################


# value=eval(input('enter the value: '))
# if type(value) in [int,float,complex,bool]:
#     print(f'the given value ({value}) is single value data type')

##############################################################################

# set1={1,2,3,4,5,6,7,8,9,10,11}
# set2={8,9,10,11,12,13,7}
# set1=eval(input('enter the value: '))
# set2=eval(input('enter the value: '))
# if set1.issubset(set2):
#     print('set1 is subset of set2')
##############################################################################


# value=input('enter the value: ')
# if value[0].isupper():
#     print('its start with upper')
##############################################################################

# value=eval(input('enter the value: '))
# if value>=0:
#     print('positive')
##############################################################################

# value=eval(input('enter the value: '))
# if value%5==0 and value%3==0:
#     print('its multiple by 5 and divisble by 3')
##############################################################################

# value=eval(input('enter the value: '))
# if value>=100 and value<=999:
#     print('it is 3 digit number')
##############################################################################

# value=eval(input('enter the value: '))
# if value==value[::-1]:
#     print('its palindrome')
##############################################################################

# value=eval(input('enter the value: '))
# if value>=0:
#     print('positive')
# else:
#     print('negative')
##############################################################################

# value=eval(input('enter the value: '))

# if 'A'<=value<='Z':
#     print('its upper case')
# else:
#     print('its lower case')

##############################################################################

# if value.isupper():
#     print('uppercase letter')
# else:
#     print('lowercase letter')
##############################################################################

# "Write a Python program to swap two numbers without using a temporary variable. Given num1 = 10 and num2 = 20, swap their values and print the result.

# num1=10
# num2=20

# # using temp
# temp=num1
# num1=num2
# num2=temp

# print(f'num1: {num1},num2: {num2}')

# using operator

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
    
# print(f'num1: {num1},num2: {num2}')
##############################################################################

# char=input('enter the character: ')
# if ('A'<=char<='Z' or 'a'<=char<='z' or '1'<=char<='9'):
#     print('it is not special character')
# else:
#     print('it is special character')
##############################################################################

# data=eval(input('enter the data : '))
# if type(data) in (str,tuple):
#     print('it is immutabale')
# else:
#     print('muttable')
##############################################################################

# num=eval(input('enter the number: '))
# if num%2==0:
#     print(f'the square of {num} is {num**2}')
# else:
#     print(f'the cube of {num} is {num**3}')
##############################################################################

# import keyword
# list=keyword.kwlist
# print(list)
# word=input('enter thbe word : ')
# if word in (list):
#     print('it is key word')
# else:
#     print('its not a key')
##############################################################################

# collection=eval(input('enter the collection : '))
# if len(collection)<5:
#     print('the collection is less than 5')
# else:
#     print('the collection is greater thean 5')
#     print('the collection is less the=an 5')
##############################################################################


