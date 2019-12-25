import numpy as np
import sys

def deathroll(gold):

	gold = gold*10
	steps = 0

	while gold != 1:
		steps += 1
		gold = np.random.randint(gold+1, size = 1) + 1 

	if steps%2 == 0:
		return steps, 1, 0

	else:
		return steps, 0, 1


def deathroll2(gold):

	gold = gold*10
	steps = 0

	while gold != 1:
		steps += 1
		gold = np.random.randint(gold+1, size = 1) + 1 

	if steps%2 == 0:
		return steps, 0, 1

	else:
		return steps, 1, 0


def deathroll3(gold):
	
	us = np.random.randint(2, size = 1)
	
	if us == 0:
		return deathroll(gold)

	else:
		return deathroll2(gold)
	

def simulation(gold, times, sim):

	r_steps = 0.0
	r_u1 = 0
	r_u2 = 0

	for a in range(int(times)):

		if sim == "1":
			steps, u1, u2 = deathroll(int(gold))

		elif sim == "2":
			steps, u1, u2 = deathroll2(int(gold))

		elif sim == "3":
			steps, u1, u2 = deathroll3(int(gold))

		r_steps += steps
		r_u1 += u1
		r_u2 += u2

	print("Simulation is complete! User1 has won " + str(r_u1) + " times and User2 has won " + str(r_u2) + " times.")
	r_steps = r_steps/int(times)
	print("Average steps = " + str(r_steps))
	print("Percentages are(u1,u2) = " + str(100 * float(r_u1)/int(times)) + " and " + str(100 * float(r_u2)/int(times)))

if __name__ == "__main__":

	stake = str(sys.argv[1])
	simulations = str(sys.argv[2])
	stype = str(sys.argv[3])
	print ("Simulating a deathroll of " + stake + " golds for " + simulations + " times.")
	simulation(stake, simulations, stype)
