 
x = str(input("Enter string value::"))
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")