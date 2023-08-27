class Review:
    def __init__(self , customer , restaurant , rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant

    def rating (self):
        return self._rating
    
    def all(self):
        return {
            'customer' : self._customer ,
            'restaurant' : self._restaurant ,
            'rating' : self._rating 
        }