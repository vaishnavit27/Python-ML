ba=bytearray([65,66,67])
ba[0]=97
print(ba)   #bytearray are mutable and bytes are immutable

b=bytes([65,66,67])
b[0]=97
print(b)