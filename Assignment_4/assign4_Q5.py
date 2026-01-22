s="Python"
print(id(s))
print(s)
s=s+"3"
print(s)
print(id(s))

#O/p : Python3 as it will concatenate python and memory address will get changed as python removes the previous memory address of that variable and assigns new address to the same var after concatenation