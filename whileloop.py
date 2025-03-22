# string=input('enter the string :')
# rev=''
# start=0
# while start<len(string):
#     char=string[start]
#     rev= char + rev
#     start+=1
# if rev== string:
#     print('palindrome')
# else:
#     print('not palindrome')
############################################################################
# factoraila using for loop
############################################################################
# fact_num=int(input('enter the factorial number: '))
# fact=1
# for num in range(1,fact_num+1):
#     fact=fact*num
#     print(fact)
############################################################################
# factoraila using while loop
############################################################################

# fact_num=int(input('enter the factorial: '))
# fact=1
# start=1
# while start<=fact_num:
#     fact*=start
#     start+=1
# print(fact)
############################################################################
# febonacie using for loop
############################################################################

# fibonacie=int(input('enter the number: '))
# first=0
# second=1
# for _ in range(fibonacie+1):
#     print(first ,end=' ') 
#     temp=first+second
#     first=second
#     second=temp
############################################################################
# febonacie using while loop
############################################################################

# fibonacie=int(input('enter the number: '))
# first=0
# second=1
# start=0
# while start<=fibonacie:
#     print(first,end=' ')
#     temp=first+second
#     first=second
#     second=temp
#     start+=1
############################################################################Microsoft.QuickAction.WiFi
############################################################################
# 1. Write a Python program to find the sum of all the elements in a list.
# list1=eval(input('enter the list : '))


############################################################################
# 2. Write a Python program to find the maximum and minimum element in a list.
############################################################################

############################################################################
# 2. number palindrome without slicing
############################################################################
# number=int(input('enter the number: '))
# onum=number
# rev=0

# while number!=0:
#     ld=number%10
#     rev=rev*10+ld
#     number//=10
# if rev==onum:
#     print('palindrome')
# else:
#      print('not palindrome')


# word=["sabyari","vignesh","mahesh"]
# output={}
# for words in word:
#     val=len(words)//2
#     res=words[val]
#     output[res]=ord(res)
#     print(output)


############################################################################
# prime number
############################################################################

p_num=int(input('enter the prime number :'))
if p_num>1:
    for num in range(2,p_num):
    # for num in range(2, int(p_num ** 0.5) + 1):  # Check only up to sqrt(p_num)
    
        if p_num % num == 0:
            print('not prime number')
            break
    else:
        print('prime number')
else:
    print('number should greater then 1')

 # 2. Write a Python program to find the maximum and minimum element in a list.
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

# p_num = int(input('Enter a number: '))

# if p_num > 1:
#     for num in range(2, int(p_num ** 0.5) + 1):  # Check only up to sqrt(p_num)
#         if p_num % num == 0:
#             print('Not a prime number')
#             break
#     else:
#         print('Prime number')
# else:
#     print('Number should be greater than 1')













