"""
Name:- Ankur Bodhak
Regd No:- 1801106086
Branch:- Textile Engineering
Institute Name:- College of Engineering and Technology,Bhubaneswar,Odisha,India
Name of the project:- Dice Rolling Simulator.

About the Project:-
  In this project we will be creating a classic rolling dice simulator with the help of basic Python's 
  random.randint(){This function generates a random number in the given range..}. 
  Here we will be using the random module since we randomize the dice simulator for random outputs.

"""

import random 


x = "y"

while x == "y": 
	
	# Gnenerates a random number 
	# between 1 and 6 (including 
	# both 1 and 6) 
	no = random.randint(1,6) 
	
	if no == 1: 
		print("[-----]") 
		print("[     ]") 
		print("[  0  ] ") 
		print("[     ]") 
		print("[-----]") 
	if no == 2: 
		print("[-----]") 
		print("[  0  ]") 
		print("[     ]") 
		print("[  0  ]") 
		print("[-----]") 
	if no == 3: 
		print("[-----]") 
		print("[     ]") 
		print("[0 0 0]") 
		print("[     ]") 
		print("[-----]") 
	if no == 4: 
		print("[-----]") 
		print("[0   0]") 
		print("[     ]") 
		print("[0   0]") 
		print("[-----]") 
	if no == 5: 
		print("[-----]") 
		print("[0   0]") 
		print("[  0  ]") 
		print("[0   0]") 
		print("[-----]") 
	if no == 6: 
		print("[-----]") 
		print("[0 0 0]") 
		print("[     ]") 
		print("[0 0 0]") 
		print("[-----]") 
		
	x=input("press y to roll again and n to exit:") 
	print("\n") 

	
