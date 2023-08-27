class Customer:
    def __init__(self , givenname , familyname):
       self.givenname =givenname
       self.familyname = familyname

    def givenname(self):
        return self.givenname
    
    def setgivenname(self , givenname):
        self.givenname = givenname
    
    def familyname(self):
        return self.familyname
    
    def setfamilyname(self ,familyname):
        self.familyname = familyname

    def fullnames(self):
        return f"{self.givenname}{self.familyname}"
    
    def all(self):
        return{
            'givenname' : self.givenname ,
            'familyname' : self.familyname ,
            'fullname': self.fullnames()
        }