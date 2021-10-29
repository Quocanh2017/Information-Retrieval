# import math

# a = int(input("a: "))
# b = int(input("b: "))

# tong = math.pow(a,b)
# if tong > math.pow(10,9):
#     print("tong: ",int(tong%math.pow(10,9)))
# else:
#     print("tong: ",int(tong))

# tong,x = 1,1
# for i in range(b):
#     tong = tong * a
# for i in range(b-1):
#     x = x*10
# if tong > x:
#     tong = tong % x
# print("results: ",int(tong))

# def fibo(n):
#     if n < 0:
#         return -1
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# def fibo_(n):
#     f0 = 0
#     f1 = 1
#     fn = 1

#     if n < 0:
#         return -1
#     elif (n==0 or n==1):
#         return n
#     else:
#         for i in range(2,n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn
# # print(fibo_(100000))
# print(fibo(10))

# n = int(input("n: "))
# a = [int(input("x: ")) for i in range(n)]
# while True:
#     k = int(input("k: "))
#     if k < 0 or k > n:
#         continue
#     else:
#         break

# a.sort()
# print(a)
# print("pos: ",a[k-1])
# l = []
# for i in range(k):
#     x = min(a)
#     a.remove(x)
# print(a)
# print("min: ",x)

# l = ["breakthrough drug for schizophrenia","new schizophrenia drug",
#     "new approach for treatment of schizophrenia","new hopes for schizophrenia patients"]

# x = set(l[i].split(" ") for i in range(len(l)))
# print(x)

