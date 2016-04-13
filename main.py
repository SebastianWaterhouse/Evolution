import random

print("What do you want your animal to be called?")
animalname = input("")

colors = {"red":0, "green":0, "blue":0, "white":0, "black":0}
biomes = {"ocean":"blue", "volcano":"red", "grasslands":"green", "arctic tundra":"white", "wasteland":"black"}

numb = 0
run = "true"

biome = random.choice(list(biomes.keys()))

animals = []

nonmatchingchance = 90
matchingchance = 10

class animal():
	def __init__(self, name, color):
		self.name = name
		self.color = color

for ani in colors:
	exec("thing" + str(numb) + " = animal('thing" + str(numb) + "', ani)")
	animals.append("thing" + str(numb))
	numb = numb + 1
	exec("thing" + str(numb) + " = animal('thing" + str(numb) + "', ani)")
	animals.append("thing" + str(numb))

numb = 0
amount = 0

for stuff in colors:
	for animaly in animals:
		if animaly[1] == stuff:
			amount = amount + 1
	colors[stuff] = amount
	amount = 0

while run == "true":
	for th in colors:
		for tb in animals:
			if tb[1] == th:
				numb = numb + 1
		print("You have " + str(colors[stuff]) + " " + th + " " + animalname + "s.")
		numb = 0
	for tb in animals:
		death = random.randint(1, 100)
		if tb[1] == biomes[biome]:
			if death <= matchingchance:
				del(tb)
		else:
			if death <= nonmatchingchance:
				del(tb)
	numb = numb + 1
	if numb >= 5:
		run = "false"
