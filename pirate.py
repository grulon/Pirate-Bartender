import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def drink_choice ():
	CDrink = {}
	print 'Please answer Yes or No to the following: '

	str1 = raw_input(questions['strong'])
	if str1[0] == 'y' or str1[0] == 'Y':
		CDrink['strong'] = True
	else:
		CDrink['strong'] = False
	salt1 = raw_input(questions['salty'])
	if salt1[0] =='y' or salt1[0] == 'Y':
		CDrink['salty'] = True
	else:
		CDrink['salty'] = False
	bit1 = raw_input(questions['bitter'])
	if bit1[0] == 'y' or bit1[0] == 'Y':
		CDrink['bitter'] = True
	else:
		CDrink['bitter'] = False
	swe1 = raw_input(questions['sweet']) 
	if swe1[0] == 'y' or swe1[0] == 'Y':
		CDrink['sweet'] = True
	else:
		CDrink['sweet'] = False
	fru1 = raw_input(questions['fruity'])
	if fru1[0] == 'y' or fru1[0] == 'Y':
		CDrink['fruity'] = True
	else:
		CDrink['fruity'] = False
	return CDrink

def make_drink(prefs):
	drink = {}
	if prefs['strong'] == True:
		drink['strong']= random.choice(ingredients['strong'])
		
	if prefs['salty'] == True:
		drink['salty'] = random.choice(ingredients['salty'])
		
	if prefs['bitter'] == True:
		drink['bitter'] = random.choice(ingredients['bitter'])
		
	if prefs['sweet'] == True:
		drink['sweet'] = random.choice(ingredients['sweet'])
		
	if prefs['fruity'] == True:
		drink['fruity'] = random.choice(ingredients['fruity'])
		
	return drink
	
if __name__ == '__main__':
	answers = drink_choice()
	#print answers    # for testing only  ... remove
	drink = make_drink(answers)
	print 'Enjoy your drink, It has lots of good stuff. '
	for things in drink:
		print 'A ' + drink['{}'.format(things)]
