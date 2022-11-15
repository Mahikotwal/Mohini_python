# Syntax - tuple()
# tuple uses round paranthesis
# tuple is fix data structure
# tuple is a mutable formation
# we does not change value in tuple
# tuple is an orderd and unchanged data structure
# tuple accept duplicate elements
# the difference between tuple and list  is that tuple uses paranthesis whereas, list uses square brackets 
# elements of tuple can't be change but list can be change

# tup=(2,3.4,'str',True)
# print(tup)
# print(type(tup))

# tup=(2,)
# print(tup)
# print(type(tup))

# tup=(1,2,3,4,5)
# index(tup(2))=6
# print(tup)

tup=(1,2,3,4,5)
lst=list(tup)
type(lst)
lst[1]=5
print(lst)
tup=tuple(lst)
print(tup)

# Duplicate-
tup=(1,2,3,4,4,5)
print(tup)

# Accsess-
tup=(1,2,3,4,5)
print(tup[1])

# tup=(1,2,3,4,5)
# print(tup[1:3])//in tuple

# tuple add-
tup1=(1,2,3,4)
tup2=(5,6,7,8)
tup1=tup1+tup2
print(tup1)

print(len(tup))

# Add element last in tuple using list 
tup=(1,2,3,4)
lst=list(tup)
type(lst)
lst.append(6)
print(lst)
tup=tuple(lst)
print(tup)

tup=(1,2,3,4)
lst=list(tup)
type(lst)
lst.insert(4,10)
print(lst)
tup=tuple(lst)
print(tup)