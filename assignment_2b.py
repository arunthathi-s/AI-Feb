# -*- coding: utf-8 -*-
"""Assignment_2b.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pLHAngw54Z_sSxBdGJ0DuCRD0DnIJNHV
"""

n=int(input("Enter number of elements: "))
a=[]
for i in range (0,n):
  b=int(input())
  a.append(b)
print("GIven list:")
print(a)
print("Positive elements in given list are :")
for j in range (0,n):
  if (a[j]>0):
    print(a[j],"\t")
  else:
    continue



