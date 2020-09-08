list=[25,14,98,63,75,98]
print(list)
print(list[5])
list[5]=741
print(list)

tuple=(25,14,98,63,75,98)
print(tuple)
print(tuple[5])
#tuple[5] = 741 #cant change values in tuple, as tuples are immutable.
print(tuple)
print(tuple.count(98))
print(tuple.index(14))


set={25,14,98,63,75,98}
print(set)
#print(set[5]) #set elements are not in any particular order.
#thus acessing them via index is not possible.
#in python set elements are ordered by using concept of hash.
#set[5]=741
print(set)