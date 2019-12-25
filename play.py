import numpy as np
import sys

def play1(gold):

	while True:

		gold = np.random.randint(gold, size = 1) + 1
		print("[You] rolls " + str(gold))

		if gold == 1:

			print("You lose")
			return

		gold = np.random.randint(gold, size = 1) + 1
		print("[PC] rolls " + str(gold))

		if gold == 1:

			print("You win")
			return

def play2(gold):

	while True:

		gold = np.random.randint(gold, size = 1) + 1
		print("[PC] rolls " + str(gold))

		if gold == 1:

			print("You win")
			return

		gold = np.random.randint(gold, size = 1) + 1
		print("[You] rolls " + str(gold))

		if gold == 1:

			print("You lose")
			return

def play3(gold):
	roll1 = 0
	roll2 = 0
	
	while roll1 == roll2:
		roll1 = np.random.randint(100, size = 1) + 1
		print("[You] rolls (for start) " + str(roll1))
		roll2 = np.random.randint(100, size = 1) + 1
		print("[PC] rolls (for start) " + str(roll2))

		if roll1 > roll2:
			play1(gold)

		if roll2 > roll1:
			play2(gold)

if __name__ == "__main__":
	stype = int(str(sys.argv[1]))
	gold = raw_input("Enter the ammount of gold: ")
	g_int = int(gold)
	if stype is 1:
		play1(g_int*10)
	elif stype is 2:
		play2(g_int*10)
	elif stype is 3:
		play3(g_int*10)
