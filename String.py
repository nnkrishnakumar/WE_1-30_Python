# String
    # > String constructor is str()
    # > String literal is '',"""""",'''''',""
    # > String is a set of sequence of character
    # > String is immutable.
    # > String support indexing
    # > String support slicing 
    # > String support concatination 
    
# a="krishna"
# print(a)

print("this is \newbook of python")

print("this is \\newbook of python")

print("this is krishna I have a laptop \"avita\"")
print("this is krishna I have a laptop 'avita'")
print('this is krishna I have a laptop "avita"')
print("this is krishna I have a laptop 'avita'")
print("krishna","Kumar")
print("krishna""kumar") 
print("krishna"+"kumar")# concatination 

print("krishna \tkumar")
print("krishna \bkumar")

a=str()  # constructor
print(a,type(a))

# literal '',"""""",'''''',""
b='Krishna'
print(b,type(b))

c=""
print(c,type(c))

d=""""""
print(d,type(d))

e=''''''
print(e,type(e))

#string is a set of sequence of character

f="krishna"
print(f[0])
print(f[4])
print(f[-7])  #k
print(f[0])  #k

h=f[0]  #k
print(h,type(h))

print(f[1],f[2],f[3],f[4],sep="")
print(f[1:4])
print(f[1:5])
print(f[1:5:1])
print(f[1:5:2])

print(f[8:9:1])
print(f[1:])
print(f[1::1])
print(f[1:20000000000000000000:1])
print(f[0::1])
print(f[::1])
print(f[:])
print(f[::])

# reverse printing 
print(f[5:1:-1]) #nhsi
print(f[6:-8:-1])
print(f[6::-1])
print(f[::-1])
print(f[0:-5])

#string methods

a="Kr2324234ishna is a boy"
print(a[::-1])

c="krishna"
print(c.upper())

print(c)

