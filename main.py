import random

print("What do you want your animal to be called?")
animalname = input("")

colors = ["red", "green", "blue", "white", "black"]
biomes = {"ocean":"blue", "volcano":"red", "grasslands":"green", "arctic tundra":"white", "wasteland":"black"}

numb = 0
run = "true"

biome = random.choice(biomes)

animals = []

nonmatchingchance = 90
matchingchance = 10

class animal():
	def __init__(self, name, color):
		self.name = name
		self.color = color

for ani in colors:
	exec("thing" + str(numb) + " = animal('thing" + str(numb) + "', ani")
	animals.append("thing" + str(numb))
	numb = numb + 1
	exec("thing" + str(numb) + " = animal('thing" + str(numb) + "', ani")
	animals.append("thing" + str(numb))

numb = 0

while run == "true":
	for th in colors:
		for tb in animals:
			if tb.color == th:
				numb = numb + 1
		print("You have " + numb + " " + th + " " + animalname + "s.")
		numb = 0
	for tb in animals:
		death = random.randint(1, 100)
		if tb.color == biomes[biome]:
			if randint <= matchingchance:
				del(tb)
		else:
			if randint <= nonmatchingchance:
				del(tb)
		
