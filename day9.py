#tuples

a=(1,2,3,4,5,9,5,3,1,"Smriti","Test")
print(type(a))

#TypeCasting
print(a)
b=list(a)
b[0]=100
print(b)
a=tuple(b)
print(a)

#TypeCasting with String
print(a)
c=list(a)
c[4]="Try"
print(c)
a=tuple(c)
print(c)


#Set
a={1,3,3,2,2,5,6,1,2,1,21,"Smriti","Hi","hey"}
print(type(a))
print(a)



c=list(a)
print(type(c))

a=set(c)
a.remove(5)
print(a)
print(type(a))

