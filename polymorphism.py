class student:
    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname
    def putdata(self):
        print("first name:",self.f)
        print("last name:",self.l)
s1=student()
s1.getdata("jigar","thakkar")
s1.putdata()

