# assessment-5
#Task-1
a={"Aman":98,"piyush":76,"dev":89}
n=input("Enter sudent name")
if n in a:
    print(a[n])
else:
    print("sudent name not found")

#Task-2
a= list(range(1, 11))
b = a[:5]
c= b[::-1]
print("Orignal list:", a)

print("First five elements:", b)
print("Reversed first five elements:", c)

