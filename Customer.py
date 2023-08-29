from review import Review

class Customer:
    customers = []

    def __init__(self , givenname , familyname):
       self.givenname =givenname
       self.familyname = familyname
       self._reviews = []

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


    def restaurants(self):
        unique_restaurants = set()
        for review in self._reviews:
            unique_restaurants.add(review.restaurant().name())
        return list(unique_restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)
    
    def reviews(self):
        return len(self._reviews)

    @classmethod 
    def findbyname(cls , name):
        for customer in cls.customers:
            if customer.fullnames() == name:
                return customer
    @classmethod
    def findallnames(cls , name):
       matchingcustomers = []
       for customer in cls.customers:
           if customer.givenname == name :
               matchingcustomers.append(customer)
       return  matchingcustomers



    def all(self):
        return{
            'givenname' : self.givenname ,
            'familyname' : self.familyname ,
            'fullname': self.fullnames()
        }
