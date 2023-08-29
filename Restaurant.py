from review import Review

class Restaurant:
    def __init__(self ,name):
        self._name = name
        self._reviews =[]

    def name (self):
        return self._name
    
    def addreviews(self , reviews):
        self._reviews.append(reviews)

    def reviews(self):
        return self._reviews
    
    def customers(self):
        unique_customers = set()
        for review in self._reviews:
         unique_customers.add(review.customer().full_name())
        return list(unique_customers)
    
    def starrating(self):
        if not self.reviews:
            return 0

        sumofrating = sum([review.rating for review in self.reviews])  
        return sumofrating/ len(self.reviews)