#list datatype:
# list constructor is list()
# list literal is []
# list is a set of sequence of elements
# list is mutable 
# list support indexing
# list support slicing 
# list support concatination 
# list have many inbuilt methods.

a=list()  # it help us to create a empty list ; list()
print(a)

b=[]      # creating empty list using list literal; []
print(b)

c=[1,1.0,"1.0",bool(),0j,[1,2,3]]


d=['k', 'r', 'i', 's', 'h', 'n', 'a']
print(d)


print(d[2])
print(d[-5])

print(d[1:5:1])
print(d[0:100000:1])
print(d[0::1])

a=[1,2,3,4,5]
b=[4,5,3,4,5]
print(a+b)     #list support concatination


a=[1,2,3,4,5]
b=[4,5,3,4,5]
c=["krishna","kumar",1,1.0,bool(10)]
print(a+b+c)     #list support concatination

print(type(a))

print(dir([]))
print(dir(list()))
print(dir([]))

# List Methods
# 'append', 
# 'clear', 
# 'copy', 
# 'count', 
# 'extend', 
# 'index', 
# 'insert', 
# 'pop', 
# 'remove', 
# 'reverse', 
# 'sort'

#1.append 

d=[]
print(type(d))
print(len(b))
print(d)  #[]
print(d.append(10))
print(d)  #[10]

# d.append(10,20)  #Error: TypeError: list.append() takes exactly one argument (2 given)
d.append([1,2,3,4,5])
print(d)

d.append("krishna")
print(d)

d.append(10.11)
print(d)       #[10, [1, 2, 3, 4, 5], 'krishna', 10.11]

#clear() method --> it remove all the element(s) from a list.
print(d.clear()) #None
print(d) #[] 

# id() function--> return the address of any datatype 
# if values and datatype of two or more elements are same then they will contain single memory.
a=10       
print(id(a))   #140731073426504

b=10
print(id(b))   #140731073426504


# copy() --> copy() method use to create two similar datatype with same elements and different address.

x=[1,2,3,4,5]
y=x
print(y,id(y))  #[1, 2, 3, 4, 5] 1565607216704
print(x,id(x))

y.append(100000)
print(y)        #[1, 2, 3, 4, 5, 100000]
print(x)


#copy() method use:

krishna=[1,2,3,4,5]
vishu=krishna.copy()

print(krishna,id(krishna))
print(vishu,id(vishu))

vishu.append("freez")
print("vishu",vishu)
print("krishna",krishna)
# --------------------------

krish=[4,5,6,7,8]
vishnu=[4,5,6,7,8]

print("krish",krish,id(krish))
print("vishnu",vishnu,id(vishnu))

#count()
a=[1,1,1,12,2,4,5,6,7,7,7,8,899,9,9,99,97,7,6,3,3]
print(a.count(9))

print(a.count(1))  #occurence of 1 is thrice

name=["Rahul","Rahul","Rahul","Rahul","Rahul","Raj","Raj","Raj","simran","simran","simran","prem","prem","prem"]
print(name.count("rahul"))  # return 0 beacuse counting of "rahul" is not equal to counting "Rahul"
print(name.count("Rahul"))  #5 Rahul repeted 5 times.

list1=[[1],[1],[1],[1],[1],[2],[3]]
print(list1.count([1]))   #5 means [1] repeated 5 times


list2=[1,2]
list2.append([1,2,3,4,5,6,7])
print(list2)   #[1, 2, [1, 2, 3, 4, 5, 6, 7]]

list3=[1,2]
list3.extend([1,2,3,4,5,6,7])
print(list3)     #[1, 2, 1, 2, 3, 4, 5, 6, 7]


list4=["rahul"]
list4.extend("krishna")
print(list4)       #['rahul', 'k', 'r', 'i', 's', 'h', 'n', 'a']

list4=["rahul"]
list4.extend(["krishna"])
print(list4)       #['rahul', 'krishna']

# list5=["rahul"]
# list5.extend(1)
# print(list5)       #TypeError: 'int' object is not iterable

# list6=["rahul"]
# list6.extend(10.0)
# print(list6)       #TypeError: 'float' object is not iterable



# index()  --> it will return index of values of a list

a=[4,3,2,3,3]
print(a.index(3))


a=[4,3,2,3,3]
print(a.index(4))  #0 index

# insert()

c=["krishna","Kumar","prajapati"]
c.insert(2,"kashyap")
print(c)


#pop()

a=[1,2,3,4,5]
print(a.pop(3))
print(a)

# remove()

a=[1,2,3,4,5]
a.remove(2)
print(a)

# reverse()

a=[1,2,3,4,5]
print(a.reverse())  # None
print(a)      #[5, 4, 3, 2, 1]

#sort()
d=[2,3,2,1,4,5]
print(d.sort())
print(d)    #[1, 2, 2, 3, 4, 5]

d.sort(reverse=False)
print(d)   #[1, 2, 2, 3, 4, 5]

d.sort(reverse=True)
print(d)   #[5, 4, 3, 2, 2, 1]
