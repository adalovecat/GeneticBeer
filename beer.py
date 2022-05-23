import random
names = ["Pagana", "Lucero", "Vauchi", "Santiago", "Vaquita", "Granada",
         "Bruja", "Calibán", "Manzano", "Shikibu"]


class Beer:

    def __init__(self):
        self.color = self.get_color()
        self.bitterness = random.randint(1, 10)
        self.thickness = random.randint(1, 10)
        self.alcohol = random.randint(1, 8)
        self.ingredients = self.get_ing()
        self.name = random.choice(names)

    def __str__(self):
        beer_text = "Color: " + self.color + "\nBitterness: " + str(self.bitterness) + "\nThickness: " + str(self.thickness) + \
            "\nAlcohol: " + str(self.alcohol) + "\nIngredients: " + \
            str(self.ingredients) + "\nName: " + self.name
        return beer_text

    def get_color(self):
        colors = ["Rubia", "Negra", "Roja"]
        selected_choice = random.choice(colors)
        return selected_choice

    def get_ing(self):
        ing = {"Frutales": ["Frutilla", "Manzana", "Uva", "Limón"],
               "Cítricos": ["Naranja", "limón", "Pomelo"],
               "Florales": ["Vainilla", "Coco", "Menta"],
               "Dulces": ["Miel", "Caramelo", "Almíbar"],
               "Amargos": ["Café", "chocolate", "ahumado"],
               "Frutos secos": ["Nuez", "Almendra", "Anís", "Maní"]}
        selected_number = random.randint(2, 4)

        recipy = []
        for number in range(1, selected_number):
            selected_list = ing.get(random.choice(list(ing)))
            selected_ing = random.choice(selected_list)
            recipy.append(selected_ing)
        return recipy


class Generation:
    def __init__(self):
        self.population = self.get_pop()

    def get_pop(self):
        beer_list = []
        for element in range(1, 11):
            b = Beer()
            beer_list.append(b)
        return beer_list


Test = Beer()
Generation = Generation()
for beer in Generation.population:
    print(beer)
