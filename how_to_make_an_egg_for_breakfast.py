print("How to make an egg for breakfast")

print("Get your eggs and smash them into a container")

print("mix them up hard with also the preffered ingredients")

print("Put in a frying pan that has ready oil")

print("turn it around til ready")

your_breakfast = "~ ~ ~ You can now have your yummy egg breakfast ~ ~ ~"

print(your_breakfast)



print("How to make an egg for pancake")

print("Get your ingredients and mix them up")

print("Put in a frying pan that has ready oil")

print("turn it around til ready")

your_breakfast = "~ ~ ~ You can now have your yummy Pancake breakfast ~ ~ ~"

print(your_breakfast)

def specifiy_breakfast(breakfast_name, ingredients):
	print(" ~~~ Yummy %s ~~~") %breakfast_name

def specify_breakfast(breakfast_name, ingredients):
	ingredients_list = "".join(str(ingredients))
	breakfast = "~~~ Yummy " + breakfast_name + " ~~~ made with" + ingredients_list
	return breakfast

def specify_breakfast(breakfast_name, *ingredients):
	breakfast = "~~~ Yummy " + breakfast_name + " ~~~ made with" + ingredients
	return breakfast

