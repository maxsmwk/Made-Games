#Maximo Salinas-Miner
#Dungeon crawl
from random import randint, random
import sys
import time

class Enemy:
	def __init__(self, strength=0, speed=0, health=0, name=""):
		self.strength = strength
		self.speed = speed
		self.health = health
		self.name = name

	def enemyType(self, x):
		# random enemy typing
		types = {
			1: ("Lv. 1 enemy", 1, 1, 1),
			2: ("Lv. 2 enemy", 2, 1, 2),
			3: ("Lv. 3 enemy", 2, 1, 3),
			4: ("Lv. 4 enemy", 2, 2, 4),
			5: ("Lv. 5 enemy", 3, 3, 5),
			6: ("Lv. 6 enemy", 3, 2, 6),
			7: ("Lv. 7 enemy", 4, 3, 6),
			8: ("Lv. 8 enemy", 4, 3, 8),
			9: ("Lv. 9 enemy", 4, 3, 9),
			10: ("Lv. 10 enemy", 5, 3, 10),
			11: ("Lv. 11 enemy", 5, 3, 11),
			12: ("Lv. 12 enemy", 6, 4, 11),
			13: ("Lv. 13 enemy", 7, 4, 12),
			14: ("Lv. 14 enemy", 8, 5, 13),
			15: ("Lv. 15 enemy", 9, 6, 15),
		}
		self.name, self.strength, self.speed, self.health = types[x]
		return self.name, self.strength, self.speed, self.health


class Player:
	def __init__(self, name="", strength=5, speed=2, health=5):
		self.name = name
		self.strength = strength
		self.speed = speed
		self.health = health

	def potionUpg(self, u):
		playerUpgrades = {
			"strength potion": (self.strength + 1, self.speed, self.health),
			"speed potion": (self.strength, self.speed + 1, self.health),
			"health potion": (self.strength, self.speed, self.health + 1),
		}
		self.strength, self.speed, self.health = playerUpgrades[u]

	def floor1gear(self, q):
		equipment1 = {
			"Lv.1 Sword": (self.strength + 2, self.speed, self.health),
			"Lv.1 Shield": (self.strength, self.speed, self.health + 2),
			"Lv.1 Armor": (self.strength, self.speed, self.health + 2),
			"None": (self.strength, self.speed, self.health),
		}
		self.strength, self.speed, self.health = equipment1[q]

	def floor2gear(self, w):
		equipment2 = {
			"Lv.2 Sword": (self.strength + 4, self.speed, self.health),
			"Lv.2 Shield": (self.strength, self.speed, self.health + 4),
			"Lv.2 Armor": (self.strength + 2, self.speed, self.health + 4),
			"None": (self.strength, self.speed, self.health),
		}
		self.strength, self.speed, self.health = equipment2[w]

	def floor3gear(self, e):
		equipment3 = {
			"Lv.3 Sword": (self.strength + 8, self.speed, self.health),
			"Lv.3 Shield": (self.strength, self.speed, self.health + 8),
			"Lv.3 Armor": (self.strength + 2, self.speed, self.health + 8),
			"None": (self.strength, self.speed, self.health),
		}
		self.strength, self.speed, self.health = equipment3[e]


class Room:
	def __init__(self, floorLvl=0):
		self.floorLvl = floorLvl
		pass
	def floor(self, enemyLvl, ifGear, potionType):
		e = Enemy()

		potionTypes = {
			1: "strength potion",
			2: "speed potion",
			3: "health potion",
		}
		self.potionType = potionTypes[potionType]

		if self.floorLvl <= 4:
			enemyEncounter = {
				1: e.enemyType(1),
				2: e.enemyType(2),
				3: e.enemyType(3),
				4: e.enemyType(4),
				5: e.enemyType(5),
			}
			self.enemyLvl = enemyEncounter[enemyLvl]

		gearTypes = {
			1: "Lv.1 Sword",
			2: "Lv.1 Shield",
			3: "Lv.1 Armor",
			4: "None",	
			5: "None",
			6: "None",
			7: "None",
			8: "None",
			9: "None",
			10: "None",
		}
		self.ifGear = gearTypes[ifGear]

		if 6 <= self.floorLvl <= 9:
			enemyEncounter = {
				1: e.enemyType(6),
				2: e.enemyType(7),
				3: e.enemyType(8),
				4: e.enemyType(9),
				5: e.enemyType(10),
			}
			self.enemyLvl = enemyEncounter[enemyLvl]

			gearTypes = {
				1: "Lv.2 Sword",
				2: "Lv.2 Shield",
				3: "Lv.2 Armor",
				4: "None",
				5: "None",
				6: "None",
				7: "None",		
				8: "None",
				9: "None",
				10: "None",
			}
			self.ifGear = gearTypes[ifGear]

		if 11 <= self.floorLvl <= 14:
			enemyEncounter = {
				1: e.enemyType(11),
				2: e.enemyType(12),
				3: e.enemyType(13),
				4: e.enemyType(14),
				5: e.enemyType(15),
			}
			self.enemyLvl = enemyEncounter[enemyLvl]

			gearTypes = {
				1: "Lv.3 Sword",
				2: "Lv.3 Shield",
				3: "Lv.3 Armor",
				4: "None",
				5: "None",
				6: "None",
				7: "None",
				8: "None",
				9: "None",
				10: "None",
			}
			self.ifGear = gearTypes[ifGear]

def sPrint(text, delay=0.05):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)
	sys.stdout.write("\n")

def sInput(prompt, delay=0.05):
	sPrint(prompt, delay)
	return input()

def game_loop(user1, roomLvl):
	roomCounter = 0
	while roomLvl < 5:
		level = Room(roomLvl)
		level.floor(randint(1,5), randint(1,10), randint(1,3))
		enter = sInput("You are on room " + str(roomLvl) + ". You see a room with a " + level.enemyLvl[0] + ". Will you enter? (y/n) ")
		if enter == "y" or enter == "yes":
			#if enemy outspeeds sequence
			if user1.speed < level.enemyLvl[2]:
				enemyAttack = user1.health - level.enemyLvl[1]
				newHealth = enemyAttack
				if newHealth <= 0:
					sPrint("The enemy swings at you, the blow lethal. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
					sPrint("GAME")
					sPrint("OVER")
				fleeOrNo = sInput("The enemy blindly swings at you, dealing damage. You originally had " + str(user1.health) + " health, but now you have " + str(newHealth) + " health. Do you want to flee? (y/n) ")
				if fleeOrNo == "y" or fleeOrNo == "yes":
					sPrint("You barely escape the clutches of the enemy.")
					roomCounter = roomCounter + 1
					roomLvl += roomCounter
					continue
				else:
					userAttack = level.enemyLvl[3] - user1.strength
					newEnemyHealth = userAttack
					while newEnemyHealth > 0:
						sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
						enemyAttack = newHealth - level.enemyLvl[1]
						if enemyAttack <= 0:
							sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
							sPrint("GAME")
							sPrint("OVER")
							exit()
						sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
						newHealth = enemyAttack
						newEnemyHealth = newEnemyHealth - user1.strength
					if newEnemyHealth <= 0:
						sPrint("You decide to fight the enemy. You swing with great force at the enemy, vanquishing it. You move to the back of the room to take a look at your spoils.")
			#if user outspeeds sequence
			elif user1.speed >= level.enemyLvl[2]:
				userAttack = level.enemyLvl[3] - user1.strength
				newEnemyHealth = userAttack
				while newEnemyHealth > 0:
					sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
					enemyAttack = newHealth - level.enemyLvl[1]
					if enemyAttack <= 0:
						sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
						sPrint("GAME")
						sPrint("OVER")
						exit()
					sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
					newHealth = enemyAttack
					newEnemyHealth = newEnemyHealth - user1.strength
				if newEnemyHealth <= 0:
					sPrint("You decide to fight the enemy. You swing with great force at the enemy, instantly vanquishing it. You move to the back of the room to take a look at your spoils.")
			user1.potionUpg(level.potionType)
			sPrint("You find a " + level.potionType + ". You consume the potion, increasing your stats. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			if level.ifGear == "Lv.1 Sword" :
					user1.floor1gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel stronger. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.1 Shield" :
					user1.floor1gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.1 Armor" :
					user1.floor1gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "None":
				sPrint("You find no gear in the room.") 
			roomCounter = roomCounter + 1
			roomLvl += roomCounter
		else:
			sPrint("You decide to skip the room, moving on to the next one.")
			roomCounter = roomCounter + 1
			roomLvl += roomCounter

def riddle():
	riddle1 = "I become shorter the older I get. What am I?"
	riddle2 = "What has hands but cannot clap?"
	riddle3 = "The more of this there is, the less you see. What is it?"
	riddleChooser = randint(1,3)
	sPrint("You enter a dark, cavernous room. 2 doors stand in front of you like leviathans. You can hear a voice from beyond bellow a riddle.")
	loop = True
	while loop:
		if riddleChooser == 1:
			riddle = sInput(riddle1)
			if riddle == "candle" or riddle == "Candle":
				sPrint("The doors shutter open, with a sound that echoes across the room. You move past the doors.")
				loop = False
			else:
				sPrint("The doors stay stagnant. The answer must have been wrong. Try again.")
		elif riddleChooser == 2:
			riddle = sInput(riddle2)
			if riddle == "clock" or riddle == "Clock":
				sPrint("The doors shutter open, with a sound that echoes across the room. You move past the doors.")
				loop = False
			else:
				sPrint("The doors stay stagnant. The answer must have been wrong. Try again.")
		elif riddleChooser == 3:
			riddle = sInput(riddle3)
			if riddle == "darkness" or riddle == "Darkness":
				sPrint("The doors shutter open, with a sound that echoes across the room. You move past the doors.")
				loop = False
			else:
				sPrint("The doors stay stagnant. The answer must have been wrong. Try again.")
		else:
			sPrint("you shouldn't be seeing this lol. You get to skip this ig")	
			loop = False
def main():
	user1 = Player(sInput("Welcome to python dungeon crawl! What's your player's name? "))
	gameStart = sInput("Have you ever played before? (y/n) ")
	while gameStart == "n" or gameStart == "no":
		gameStart = sInput("Python dungeon crawl is a turn based, simple dungeon crawl developed by Maximo Salinas-Miner. You will crawl through a total of 15 rooms, with a special challenge room every fifth room. In each room, you will encounter an enemy and a potion that will increase your stats. In some rooms, you may even find gear that will boost your stats further. You may decide to skip a room, but you must enter the special challenge room. After you beat a challenge room, the enemies become stronger. Your goal is to beat the boss at the 15th room. Are you ready to continue?(y/n) ")

	game_loop(user1, 0)
	#floor 1 boss(riddle)
	riddle()

	#floor 2
	while roomCounter > 5 and roomCounter < 10:
		level = Room(roomCounter)
		level.floor(randint(1,5), randint(1,10), randint(1,3))
		enter = sInput("You are on room " + str(roomCounter) + ". You see a room with a " + level.enemyLvl[0] + ". Will you enter? (y/n) ")
		if enter == "y" or enter == "yes":
			#if enemy outspeeds sequence
			newHealth = user1.health
			if user1.speed < level.enemyLvl[2]:
				enemyAttack = user1.health - level.enemyLvl[1]
				newHealth = enemyAttack
				if newHealth <= 0:
					sPrint("The enemy swings at you, the blow lethal. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
					sPrint("GAME")
					sPrint("OVER")
					exit()
				fleeOrNo = sInput("The enemy blindly swings at you, dealing damage. You originally had " + str(user1.health) + " health, but now you have " + str(newHealth) + " health. Do you want to flee? (y/n) ")
				if fleeOrNo == "y" or fleeOrNo == "yes":
					sPrint("You barely escape the clutches of the enemy.")
					roomCounter = roomCounter + 1
					continue
				else:
					userAttack = level.enemyLvl[3] - user1.strength
					newEnemyHealth = userAttack
					while newEnemyHealth > 0:
						sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
						enemyAttack = newHealth - level.enemyLvl[1]
						if enemyAttack <= 0:
							sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
							sPrint("GAME")
							sPrint("OVER")
							exit()
						sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
						newHealth = enemyAttack
						newEnemyHealth = newEnemyHealth - user1.strength
					if newEnemyHealth <= 0:
						sPrint("You decide to fight the enemy. You swing with great force at the enemy, vanquishing it. You move to the back of the room to take a look at your spoils.")
			#if user outspeeds sequence
			elif user1.speed >= level.enemyLvl[2]:
				userAttack = level.enemyLvl[3] - user1.strength
				newEnemyHealth = userAttack
				while newEnemyHealth > 0:
					sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
					enemyAttack = newHealth - level.enemyLvl[1]
					if enemyAttack <= 0:
						sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
						sPrint("GAME")
						sPrint("OVER")
						exit()
					sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
					newHealth = enemyAttack
					newEnemyHealth = newEnemyHealth - user1.strength
				if newEnemyHealth <= 0:
					sPrint("You vanquish the enemy. You move to the back of the room to take a look at your spoils.")
			user1.potionUpg(level.potionType)
			sPrint("You find a " + level.potionType + ". You consume the potion, increasing your stats. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			if level.ifGear == "Lv.2 Sword" :
					user1.floor2gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel stronger. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.2 Shield" :
					user1.floor2gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.2 Armor" :
					user1.floor2gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "None":
				sPrint("You find no gear in the room.") 
			roomCounter = roomCounter + 1
		else:
			sPrint("You decide to skip the room, moving on to the next one.")
			roomCounter = roomCounter + 1
	decision = sInput("You come to a clearing in the dungeon. It looks like an archway. Proceed? (y/n): ")
	while decision == "n" or decision == "no":
		decision = sInput("You try turning back, only to realize the way you came is completely blocked off. You have no choice but to enter.")
		decision = 0
	sPrint("You enter the room. In the middle is a garguantuan beast. It has ginormous appendages, and is chewing on the armor of a fallen knight. It lets out an intense roar that pierces your eardrums once it sees you.")
	room10boss = sInput("You see the beast is blocking the exit. You have to face this creature. You are faced with 4 options, brave Knight. what wILL you do? Will you: A: try to lunge at it? B: try to leap on top of it to control it? C: try to run around it?")
	while roomCounter == 10:
		if room10boss == "A" or room10boss == "a":
			sPrint("Your pitiful attempt to lunge at the beast is met with a brutal swing of its arms. It's huge muscles send you flying in the air, and you crash into a wall, your entire body broken. With another quick movement of it's arm, it crushes you, and you are splattered like a bug all over the dungeon floor. Your journey comes to an abrupt end. Your final thoughts are - Maybe another soul can KILL this beast.(Hint: look at the strangely capitalized letters.)")
			sPrint("GAME")
			sPrint("OVER")
			exit()
		elif room10boss == "B" or room10boss == "b":	
			sPrint("You wait until the beast is vulnerable to climb on top of it's arms. It bucks and thrashes, but you stay on top of it, clinging for life. Just when it seems like you are about to reach the beast's head, it grabs you with the other arm. It holds you in front of it's mangled face. It's breath is foul, and you can see the blood covering it's mouth. Almost instantly, it thrusts you towards its mouth. You are chewed up and swallowed, another soul taken by the dungeon. Maybe another soul can KILL this beast.(Hint: look at the strangely capitalized letters.)")
			sPrint("GAME")
			sPrint("OVER")
			exit()
		elif room10boss == "C" or room10boss == "c":
			sPrint("You pray that your wits and speed can save you from the beast. You dodge it's swings, and confuse the beast as to which way you're going. You make your way around the beast, and are able to see the exit. Just when you thought you could escape, the beast sits back, covering the exit. You run full force into it's gelatinous side, and you are knocked back. The beast, unsteady, begins to wobble. Just before you can move, its full force lands on top of you. You are smooshed under the beasts unfathomable weight. Maybe another soul can KILL this beast.(Hint: look at the strangely capitalized letters.)")
			sPrint("GAME")
			sPrint("OVER")
			exit()
		elif room10boss == "kill" or room10boss == "Kill" or room10boss == "KILL":
			sPrint("You discard all the other options. The only way to take care of this beast is to kill it. You run back and forth, dizzying and exhausting the beast. It roars as it loses it's energy. It's arms fall flat, and you leap on top of them, climbing towards it's head. Once there, you drive your fists into the beasts eyes. It cries out and retaliates, but you make sure its eyes are nothing more than a bloody pulp. The beast collapses on the ground, wailing out. While it squirms, you jump off its head and grab loose debris from the ground. You repeatedly bash the debris into its skull, until the beast becomes limp. You have conquered this beast. You move to the next set of rooms.")
			roomCounter = roomCounter + 1
			continue
		room10boss = sInput("You must fight it! Find a way to dodge it, or KILL it.(Options: A: try to Lunge at it? B: try to Leap on top of it to control it? C: try to run around it?)")
	#floor 3
	while roomCounter > 10 and roomCounter < 15:
		level = Room(roomCounter)
		level.floor(randint(1,5), randint(1,10), randint(1,3))
		enter = sInput("You are on room " + str(roomCounter) + ". You see a room with a " + level.enemyLvl[0] + ". Will you enter? (y/n) ")
		if enter == "y" or enter == "yes":
			#if enemy outspeeds sequence
			newHealth = user1.health
			if user1.speed < level.enemyLvl[2]:
				enemyAttack = user1.health - level.enemyLvl[1]
				newHealth = enemyAttack
				if newHealth <= 0:
					sPrint("The enemy swings at you, the blow lethal. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
					sPrint("GAME")
					sPrint("OVER")
					exit()
				fleeOrNo = sInput("The enemy blindly swings at you, dealing damage. You originally had " + str(user1.health) + " health, but now you have " + str(newHealth) + " health. Do you want to flee? (y/n) ")
				if fleeOrNo == "y" or fleeOrNo == "yes":
					sPrint("You barely escape the clutches of the enemy.")
					roomCounter = roomCounter + 1
					continue
				else:
					userAttack = level.enemyLvl[3] - user1.strength
					newEnemyHealth = userAttack
					while newEnemyHealth > 0:
						sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
						enemyAttack = newHealth - level.enemyLvl[1]
						if enemyAttack <= 0:
							sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
							sPrint("GAME")
							sPrint("OVER")
							exit()
						sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
						newHealth = enemyAttack
						newEnemyHealth = newEnemyHealth - user1.strength
					if newEnemyHealth <= 0:
						sPrint("You decide to fight the enemy. You swing with great force at the enemy, vanquishing it. You move to the back of the room to take a look at your spoils.")
			#if user outspeeds sequence
			elif user1.speed >= level.enemyLvl[2]:
				userAttack = level.enemyLvl[3] - user1.strength
				newEnemyHealth = userAttack
				while newEnemyHealth > 0:
					sPrint("You swing at the enemy, dealing " + str(user1.strength) + " damage. The enemy has " + str(newEnemyHealth) + " health left.")
					enemyAttack = newHealth - level.enemyLvl[1]
					if enemyAttack <= 0:
						sPrint("The enemy swings at you. Your exhausted body can't take the blow. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
						sPrint("GAME")
						sPrint("OVER")
						exit()
					sPrint("The enemy swings at you, dealing " + str(level.enemyLvl[1]) + " damage. You had " + str(newHealth) + " health. Now you have " + str(enemyAttack) + " health left.")
					newHealth = enemyAttack
					newEnemyHealth = newEnemyHealth - user1.strength
				if newEnemyHealth <= 0:
					sPrint("You vanquish the enemy. You move to the back of the room to take a look at your spoils.")
			user1.potionUpg(level.potionType)
			sPrint("You find a " + level.potionType + ". You consume the potion, increasing your stats. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			if level.ifGear == "Lv.3 Sword" :
					user1.floor3gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel stronger. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.3 Shield" :
					user1.floor3gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "Lv.3 Armor" :
					user1.floor3gear(level.ifGear)
					sPrint("Along with the potion, you find a " + level.ifGear + ". You equip the " + level.ifGear + ". You feel more durable. Your stats are now: Strength: " + str(user1.strength) + ", Speed: " + str(user1.speed) + ", Health: " + str(user1.health) + ".")
			elif level.ifGear == "None":
				sPrint("You find no gear in the room.")
			roomCounter = roomCounter + 1
		else:
			sPrint("You decide to skip the room, moving on to the next one.")
			roomCounter = roomCounter + 1
	bossHealth = 25
	bossSpeed = 5
	bossStrength = 7
	sPrint("After the final dungeon room, you see the exit. You sprint towards it, but just before you reach it, the entrance closes!")
	sPrint("You turn back, only to face a demon with 2 horns portruding from its skull.")
	sPrint("Well, well, well. It seems you have reached the end of my dungeon. It says. You don't respond, standing in front of the demon courageously. ")
	sPrint("You don't talk much, huh? He pulls out 2 humongous swords. No one has ever escaped my wrath. Today will be no different. You prepare for battle.")
	while roomCounter == 15:
		#if demon outspeeds
			newHealth = user1.health
			if user1.speed < bossSpeed:
				bossAttack = user1.health - bossStrength
				newHealth = bossAttack
				if newHealth <= 0:
					sPrint("The demon takes one quick swing at you, and you are split in half. Right before you die, you hear his cruel laugh. You die on the cold, dark dungeon floor. Maybe another soul can conquer the unrelenting dungeon.")
					sPrint("GAME")
					sPrint("OVER")
					exit()
				else:
					sPrint("The demon swings its massive swords at you dealing " + str(bossStrength) + " damage. You had " + str(user1.health) + " health. Now you have " + str(newHealth) + " health left.")
					userAttack = bossHealth - user1.strength
					newBossHealth = userAttack
					while newBossHealth > 0:
						sPrint("You swing with all your might at the demon, dealing " + str(user1.strength) + " damage. The demon has " + str(newBossHealth) + " health left.")
						bossAttack = newHealth - bossStrength
						if bossAttack <= 0:
							sPrint("The demon swings at you with his swords. You put up a good fight, but are ultimately no match for his raw power. You die on the cold, dark dungeon floor another victim taken. Maybe another soul can kill the demon.")
							sPrint("GAME")
							sPrint("OVER")
							exit()
						sPrint("The demon swings at you, dealing " + str(bossStrength) + " damage. You had " + str(newHealth) + " health. Now you have " + str(bossAttack) + " health left.")
						newHealth = bossAttack
						newBossHealth = newBossHealth - user1.strength
					if newBossHealth <= 0:
						sPrint("You swing, using all your might. The demon may think it is superior, but it is no match for your determination and grit. You kill the demon, freeing the dungeon from its evil tyrant.")
						roomCounter = roomCounter + 1
						continue
			#if user outspeeds sequence
			elif user1.speed >= bossSpeed:
				userAttack = bossHealth - user1.strength
				newBossHealth = userAttack
				while newBossHealth > 0:
					sPrint("You swing at the demon, dealing " + str(user1.strength) + " damage. The demon has " + str(newBossHealth) + " health left.")
					bossAttack = newHealth - bossStrength
					if bossAttack <= 0:
						sPrint("The demon swings at you with his swords. You put up a good fight, but are ultimately no match for his raw power. You die on the cold, dark dungeon floor another victim taken. Maybe another soul can conquer the dungeon.")
						sPrint("GAME")
						sPrint("OVER")
						exit()
					sPrint("The demon swings at you, dealing " + str(bossStrength) + " damage. You had " + str(newHealth) + " health. Now you have " + str(bossAttack) + " health left.")
					newHealth = bossAttack
					newBossHealth = newBossHealth - user1.strength
				if newBossHealth <= 0:
					sPrint("After, a long battle, you take one final swing at the demon. Its evil is no match for your pure heart, and you kill the demon. You have freed this dungeon from its curse.")
					roomCounter = roomCounter + 1
					continue
	sPrint("You stand over the demon's dead body, the hero of the dungeon. You exit the dungeon, and take in the fresh air. You are alive, and the cool breeze kisses your face. Congratulations")
	sPrint("YOU")
	sPrint("WIN")
	sPrint("WINNING STATS:")
	sPrint("Username: " + user1.name)
	sPrint("Strength: " + str(user1.strength))
	sPrint("Speed: " + str(user1.speed))
	sPrint("Health: " + str(user1.health))
	sPrint("Thank you for playing! - This game was made by Maximo Salinas-Miner")
	exit()
main()



	


