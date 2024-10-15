# num=int(input("enter the number to square"))
# square=num**2
# print(f"the {num} square is {square}")
 
# user_list=eval(input("enter the list"))
# last_element=user_list[-1]
# print(f"the last element is {last_element}")

# list1=[1,2,3,4,5,6,7,8,9]
# index_position=int(input("entr the index position"))
# value=list1[index_position]
# print(f"the orginal list{list1}")
# print(f"the value at index {index_position} is {value}")  

# user_list=eval(input("entr the list :"))
# index=int(input("enter the index number: "))
# user_list.remove(index)
# print(f"{user_list}")

# word=input("enter the word : ")
# print(word[::-1])

# num1=int(input("enter num1 :"))
# num2=int(input("enter num2 :"))
# sum=num1+num2
# print(f"sum of {num1} and {num2} is {sum}")  
# sub=num1-num2
# print(f"sub of {num1} and {num2} is {sub}")
# div=num1/num2
# print(f"div of {num1} and {num2} is {div}")
# mod=num1%num2
# print(f"mod of {num1} and {num2} is {mod}")
# mul=num1*num2
# print(f"mul of {num1} and {num2} is {mul}")
#letter m
# for row in range(3):
#     for col in range(3):
#         if col==0 or col==2 or row==1: 
#             print("*", end=" ")
#         else:
#             print("_", end=" ")
#     print()
#letter w
# n=20
# for row in range(n):
#     for col in range(n):
#         if col==0 or col==n-1 or (col+row==n-1 and row>n//2) or (col==row and row>n//2):
#             print("*",end="")
#         else:
#             print(" ",end="" )
#     print()
#letter x
# n=15
# for row in range(n):
#     for col in range(n):
#         if  (row+col==n-1 ) or (row==col ):
#             print("*",end="")
#         else:
#             print(" ",end="" )
#     print()
# 
#     print()

# n=15
# for row in range(n):
#     for col in range(n):
#         if (row+col==n-1 and row>=n//2 )or(row>=n//2 and row==col)  :
#              print("*",end="")
#         else:
#             print("_",end="" )
#     print()
# n = 15
# for row in range(n):
#     for col in range(n):
#         if col == row or col == n - row - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n=5
# for row in range(n):
#     for col in range(n):
#         if col==4 or row ==4 or row+col>=n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n=5
# for row in range(n):
#     for col in range(n):
#         if row==0 or (row+col==n-1 and row <=n//2)or (row==col and row<=n//2) :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# n=int(input("Enter Number: "))
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n-1 or row == 0 or row == n//2:
#             print('A',end = ' ')
#         else:
#             print(' ',end=' ')
#     print()
# n = int(input("Enter a Number: "))
# for row in range(n):
#     for col in range(n):
#         if (col==row and row<=n//2) or (col+row == n-1 and row<=n//2):
#             print('V',end = ' ')
#         else:
#             print('_',end=' ')
#     print()
#letter b
# n=5
# for row in range(n):
#     for col in range(n):
#         if col==0 or (row==0 and col!=n-1) or(row==n//2 and col!=n-1) or(row==n-1 and col!=n-1) or (col==n-1 and row!=0 and row!=n-1 and row!=n//2):
#             print("*",end=" ")
#         else:
#             print("_",end=" ")
#     print()
#letter d
# n=5
# for row in range(n):
#     for col in range(n):
#         if col==0 or (row==0 and col!=n-1)or (row==n-1 and col!=n-1) or(col==n-1 and row!=n-1 and row!=0 ):
#             print("*",end=" ")
#         else:
#             print("_",end=" ")
#     print()
# n=5
# for row in range(n):
#     for col in range(n):
#         if col==0 or (row+col==n-1 and row<=n//2 ) or (col==row and row>=n//2):       
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# n=5
# for row in range(n):
#     for col in range(n):
#         if col==0 or (row+col==n-2 and row<=n//2) or (col==row-1 and row>=n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    
# n=5
# for row in range(n):
#     for col in range(n):
#         if col==0 or (row==0 and col!=n-1) or (row==n//2 and col!=n-1) or(col==n-1 and  row==1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for row in range(n):
#     for col in range(n):
#         if (col==0 and row!=0 and row!=n-1) or (col==n-1 and row!=0 and row!=n-1) or (row==0 and col!=0 and col!=n-1) or(row==n-1  and col!=0 and col!=n-1) or(col==row and row>=n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=int(input("Enter Number: "))
# for row in range(n):
#     for col in range(n):
#         if col == 0 or row == 0 or row == n//2 or (col==n-1 and row <= n//2) or (row==col and row >= n//2):
#             print('R',end = ' ')
#         else:
#             print(' ',end=' ')
#  
# letter u   print()
# n=5
# for row in range(n):
#     for col in range(n):
#         if (col==0 or col==n-1) and row!=n-1 or (row==n-1 and col!=0 and col!=n-1):
#             print('*',end = ' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=10
# for row in range(n):
#     for col in range(n):
#         if row==col :
#             print('*',end = ' ')
#         else:
#             print(' ',end=' ')
#     print()
n = int(input("Enter the size : "))
for row in range(n):
    for col in range(n * 2 - 1):
        if row == col or row + col == n * 2 - 2:
            print("*", end="")
        else:
            print("_", end="")
    print()