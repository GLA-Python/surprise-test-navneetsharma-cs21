def expanding(lst):

   for i in range(len(lst)-2):

       if(lst[i]>=lst[i+1]):

           return False

   return True

lst = [1,5,8,7,7]
d = expanding(lst)
print(d)