sname=input("Enter Student Name:")
rno=int(input("Enter Roll No:"))
s1=int(input("Enter Mark Of Subject 1:"))
s2=int(input("Enter Mark Of Subject 2:"))
s3=int(input("Enter Mark Of Subject 3:"))

total=s1+s2+s3
per=total/3

print("Student Name :",sname)
print("Roll No :",rno)
print("Total:",total)
print("Perchantage :",per)

if per>=70:
    print("Distincation")
elif per>=60:
    print("Second class")
elif per>=50:
    print("First class")
elif per>=40:
    print("pass class")
else:
    print("Fail")
