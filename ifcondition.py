'''
1. Simple If
2. If-else
3. Nested if-else
4. Ladder if-else
'''

a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if a>b:
    if a>c:
        print("A Is max number")
    else:
        print("C Is max number")
elif b>c:
    print("B Is max number")
else:
    print("C Is max number")
