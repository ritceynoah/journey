t=(1,2,4,7,9,21,45)
print(t);
num = int(input("enter num to be deleted"))
b=list(t)
b[num]=100
print()
t=tuple(b)
print(t, end=' is the updated t')
