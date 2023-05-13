class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Название Ресторана -  {self.restaurant_name} \nКухня: {self.cuisine_type}.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} был обновлен до -  {self.rating}!")