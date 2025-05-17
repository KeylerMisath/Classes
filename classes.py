class Dog:
    def __init__(self, size, color, race, price):
        self.size = size
        self.color = color
        self.race = race
        self.price = price

Rufo = Dog("big", "black", "German Shepherd", 500)
Marcelo = Dog("small", "white", "Poodle", 300)
Yovani_Vasquez = Dog ("medium", "brown", "Labrador", 400)
Hanzo = Dog("medium", "yellow", "Golden Retriever", 450)
Paco = Dog("small", "black", "Pug", 200)

print(f"Rufo is a  {Rufo.color} {Rufo.race} and his price is {Rufo.price} dollars and he is {Rufo.size}")
print(f"Marcelo is a {Marcelo.color} {Marcelo.race} and his price is {Marcelo.price} dollars and he is {Marcelo.size} size")
print(f"Yovani Vasquez is a  {Yovani_Vasquez.color} {Yovani_Vasquez.race} and his price is {Yovani_Vasquez.price} dollars and he is {Yovani_Vasquez.size}")
print(f"Hanzo is a {Hanzo.color} {Hanzo.race} and his price is {Hanzo.price} dollars and he is {Hanzo.size} size")
print(f"Paco is a {Paco.color} {Paco.race} and his price is {Paco.price} dollars and he is {Paco.size} size")

print("_____________________________________________________________________________________________")
class Movie:
    def __init__(self, title, director, year, genre, price):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.price = price

Scarface = Movie("Scarface", "Brian De Palma", 1983, "Thriller", 25)
Shutter_Island = Movie("Shutter Island", "Martin Scorsese", 2010, "Thriller", 80)
Interstellar = Movie("Interstellar", "Christopher Nolan", 2014, "Science Fiction", 165)
Dune_part_two = Movie("Dune part two", "Denis Villeneuve", 2023, "Science Fiction", 190)
The_Batman = Movie("The Batman", "Matt Reeves", 2022, "Action", 185)

print(f"Scarface is a {Scarface.genre} movie of the {Scarface.year} directed by {Scarface.director} released in {Scarface.year} and cost {Scarface.price} million dollars")
print(f"Shutter Island is a {Shutter_Island.genre} movie of the {Shutter_Island.year} directed by {Shutter_Island.director} released in {Shutter_Island.year} and cost {Shutter_Island.price} million dollars")
print(f"Interstellar is a {Interstellar.genre} movie of the {Interstellar.year} directed by {Interstellar.director} released in {Interstellar.year} and cost {Interstellar.price} million dollars")
print(f"Dune part two is a {Dune_part_two.genre} movie of the {Dune_part_two.year} directed by {Dune_part_two.director} released in {Dune_part_two.year} and cost {Dune_part_two.price} million dollars")
print(f"The Batman is a {The_Batman.genre} movie of the {The_Batman.year} directed by {The_Batman.director} released in {The_Batman.year} and cost {The_Batman.price} million dollars")

class jojoStands:
    def __init__(self, name, power, type, stand_master, part):
        self.name = name
        self.power = power
        self.type = type
        self.stand_master = stand_master
        self.part = part

Star_platinum = jojoStands("Star Platinum", "Superhuman Strength, Precision, Speed, Time Stop", "short range", "Jotaro Kujo", "3")
Crazy_Diamond = jojoStands("Crazy Diamond", "Restoration", "close range", "Josuke Higashikata", "4")
Golden_Experience = jojoStands("Golden Experience", "Life Giver", "close range", "Giorno Giovanna", "5")
Silver_Chariot = jojoStands("Silver Chariot", "Swordsmanship and Speed", "close range", "Jean Pierre Polnareff", "3")
The_World = jojoStands("The World", "Time Stop and Superhuman Strength", "close range", "Dio Brando", "3")

print("_____________________________________________________________________________________________")

print(f"{Star_platinum.name} is a {Star_platinum.type} stand of {Star_platinum.stand_master} from part {Star_platinum.part} with the power of {Star_platinum.power}")
print(f"{Crazy_Diamond.name} is a {Crazy_Diamond.type} stand of {Crazy_Diamond.stand_master} from part {Crazy_Diamond.part} with the power of {Crazy_Diamond.power}")
print(f"{Golden_Experience.name} is a {Golden_Experience.type} stand of {Golden_Experience.stand_master} from part {Golden_Experience.part} with the power of {Golden_Experience.power}")
print(f"{Silver_Chariot.name} is a {Silver_Chariot.type} stand of {Silver_Chariot.stand_master} from part {Silver_Chariot.part} with the power of {Silver_Chariot.power}")
print(f"{The_World.name} is a {The_World.type} stand of {The_World.stand_master} from part {The_World.part} with the power of {The_World.power}")