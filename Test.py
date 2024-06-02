""" my_list = []

fruit = input("Enter your fav fruit: ")
game = input("Enter your fav game: ")
drink = input("Enter your fav drink: ")

fav = {"Fruit": fruit, "Game": game, "Drink": drink}
my_list.append(fav)

for fav in my_list:
    print(f"Fav drink is: {drink}\nFav fruit is: {fruit}")
 """


item_prices = {"Games": 300,
               "Drinks": 200,
               "food": 500}

i = 1
for item, prices in item_prices.items():
    print(f"({i}){item}-Rs:{prices}")
    i += 1
