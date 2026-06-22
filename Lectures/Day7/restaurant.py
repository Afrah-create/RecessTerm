class Restaurant:
    def __init__(self, restName, cuisineType):
        self.restName = restName
        self.cuisineType = cuisineType
    def decRestaurant(self):
        print(f"{self.restName} serves {self.cuisineType} cuisine.")
    def openRestaurant(self):
        print(f"{self.restName} is open for meals.")
restaurant = Restaurant("Five Star(*****)", "K'jong")
print(restaurant.restName)
print(restaurant.cuisineType)
restaurant.decRestaurant()
restaurant.openRestaurant()

restaurant2 = Restaurant("Bush Meals Rest", "Chinese")
print(restaurant2.restName)
print(restaurant2.cuisineType)
restaurant2.decRestaurant()
restaurant2.openRestaurant()

restaurant3 = Restaurant("Bondea Restaurant", "Aringa")
print(restaurant3.restName)
print(restaurant3.cuisineType)
restaurant3.decRestaurant()
restaurant3.openRestaurant()