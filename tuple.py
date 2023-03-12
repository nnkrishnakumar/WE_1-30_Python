# tuple
#tuple constructor is tuple()
# tuple literal is ()
# tuple is faster then list
# tuple is immutable
#tuple support indexing 
#tuple support slicing 
# tuple have two methods index() and count()

a=tuple()
print(a)  #we will get literal of tuple ()
print(type(a))  # <class 'tuple'>
print(id(a))  #140710488298968

d=tuple()
print(type(d),id(d))  #140710488298968

e=()
print(e,type(e),id(e))

# those data which are immutable they are same in structure their id must be same .

f=(1,1,1,1,1,2,2,2,2,3,3,3,2,2,2,21,1,1,1,34,5,4,44,44)
print(f.count(1))   # occurence of 1 insite a tuple f

print(f.index(2))   # index value of first occurence of 2 is 5

print(sum(f))  # 183


# indexing(Positive indexing)

a=(1,2,3,4,5,6)
print(a[2])  # 3
# print(a[10])  #IndexError: tuple index out of range

# indexing(Negative Indexing)
print(a[-3])  #4


#slicing(Positive Slicing LTR)

a=(1,2,3,4,5,6,7)
print(a[1:6:1])
print(a[0:5:1])
print(a[:5:1])
print(a[::2])


#slicing(Negative Slicing RTL)
b=(1,2,3,4,5,6,7)
print(b[-1:-5:-1])
print(b[::-1])

# Interviews question
a=10,20,"krishna","kumar",10.0
print(a,type(a))

# Packing and Unpacking
# Packing
a=[10,20,"krishna","kumar",10.0]

# Unpacking

k,l,m,n,o=[10,20,"krishna","kumar",10.0]
print("k",k)
print("l",l)
print("m",m)
print("n",n)
print("o",o)

x,y,*z=[10,20,"krishna","kumar",10.0]
print(x)
print(y)
print(z)


x,*y,z,w=[10,20,"krishna","kumar",10.0]
print(x)
print(y)
print(z)
print(w)

