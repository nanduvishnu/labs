import functools
def multiples_of_list(lst1):
 list2=[]
 for num in lst1:
  if num%4==0:
    list2.append(num)
 return list2
lst=range(0,100)
print(multiples_of_list(lst))

