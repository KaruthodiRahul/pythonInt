

#custom list 
alist = []
print(type(alist))

#another way to define a list

alist = list()
print(type(alist))

#functions of the list 
print(dir(alist))
alist = [_ for _ in range(20) if _%2 ==0]
print (alist)

#appending to the list
alist.append('Rahul')

#list inside a list 
blist = [[1,2], [3,4]]
clist = blist[:]
clist[0].append(3)

print(clist, blist)
#multiple similar elements
dlist = clist * 4

print (dlist)

#remove from the list
dlist.remove([1,2,3])
print (dlist)
dlist.sort()
print (dlist)

print (dlist.index([1,2,3]))



