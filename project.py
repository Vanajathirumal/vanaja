# def gen():
#     print('start')
#     yield 1
#     yield 2
#     print('bye')
# var=gen()
# next(var)
# next(var)
# next(var)


# def get_no():
#     start=1
#     while True:
#         yield start
# var1=get_no()
# next(var1)


# var=iter(range(5))
# while True:
#     try:
#         num=next(var)
#     except:
#         break
#     else:
#         next(var)

# num=int(input('enter the num :'))
# fact=1
# for n in range(1,num+1):
#     fact*=n
# print(fact)

# f_num=int(input('enter the num :'))
# first_num=0
# secon_num=1
# for num in range(f_num):
#     print(first_num,end=' ')
#     temp=first_num+secon_num
#     first_num=secon_num
#     secon_num=temp


# p_num=int(input('enter the num prime number : '))
# for num in range(2,p_num):
#     if p_num%num==0:
#         print('not prime number')
#         break
#     else:
#         print('prime number')
#         break


# a_num=int(input('enter the num:'))
# sum=0
# temp=a_num
# length=len(str(a_num))
# while temp!=0:
#     last_digit=temp%10
#     sum+=last_digit**length
#     temp//=10
# if sum==a_num:
#     print('amonstrong')
# else:
#     print('not amonstrong')

# from math import factorial
# s_num=int(input('enter the num :'))
# sum=0
# temp=s_num
# while temp!=0:
#     last_digit=temp%10
#     # fact=1
#     # for num in range(1,last_digit+1):
#     #     fact*=num
#     sum+=factorial(last_digit)
#     temp//=10
# if sum==s_num:
#     print('strong number')
# else:
#     print('not strong number')

# num=int(input('enter the number: '))
# for n in range(1,num+1):
#     if n*n==num:
#         print('perfect square')
#         break
# else:
#     print('not perfect square ')
number=int(input('enter the number : '))
num=0
while num!=0:
    last_digit=num%10


