lst=[10,20,30]
tpl=(10,20,30)

lst[0]=100
print(lst)
tpl[0]=100   #Not update value as tuple is immutable
print(tpl)
print(lst)
