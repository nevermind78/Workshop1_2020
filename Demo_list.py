#To create a list, use square brackets:
mylist = [ ]
mylist = [1,2,3]
mylist = ['a', 'b', 'c', [1,2,3] ]
# 4 elements
#Retrieving one element, given an index
x = mylist[3]
#Checking membership
mylist
3 in mylist
# True or False
#From another type: Given an iterable, the “list” function returns a list:
list('abc')
list((1,2,3))
list({1,2,3})
# ['a', 'b', 'c']
# [1,2,3]
# [1,2,3]
#Replacing an existing element
mylist = ['a', 'b', 'c']
mylist[1] = 'z'
mylist
# ['a', 'z', 'c']
#Replacing multiple existing elements
mylist = ['a', 'b', 'c', 'd', 'e', 'f']
mylist[1:3] = 'xyz'
# replace indexes 1 and 2 with x, y, z
mylist
# ['a', 'x', 'y', 'z', 'd', 'e', 'f']
#Adding an element to the end
mylist = ['a', 'b', 'c']
mylist.append('d')
mylist
# ['a', 'b', 'c', 'd']
mylist.append([1,2,3])
mylist
# ['a', 'b', 'c', 'd', [1,2,3]]
#Adding multiple elements to the end
mylist = ['a', 'b', 'c']
mylist.extend([1,2,3])
mylist
# ['a', 'b', 'c', 'd', 1, 2, 3]
#Removing an element from the end
mylist = ['a', 'b', 'c']
- 1 -mylist.pop()
mylist
# returns 'c'
# ['a', 'b']
#Removing an element from any index
mylist = ['a', 'b', 'c']
mylist.pop(0)
# returns 'a'
mylist
# ['b', 'c']
#Removing an element based on its value (rather than its position)
mylist = ['a', 'b', 'c', 'a', 'a', 'b']
mylist.remove('a')
# Remove the first 'a'
mylist
# ['b', 'c', 'a', 'a', 'b']
#Sorting
mylist = ['d', 'a', 'c', 'b']
mylist.sort()
# Returns None
mylist
# ['a', 'b', 'c', 'd']
#Reversing
mylist = ['a', 'b', 'c']
mylist.reverse()
# returns None
mylist
# ['c', 'b', 'a']
#Joining
mylist = ['a', 'b', 'c']
'*'.join(mylist)
'...'.join(mylist)
# 'a*b*c'
# 'a...b...c'
#Iterating over the elements
mylist = ['a', 'b', 'c']
for item in mylist:
    print(item)
#Iterating over the sorted elements
mylist = ['d', 'a', 'c', 'b']
for item in sorted(mylist):
    print(item)
