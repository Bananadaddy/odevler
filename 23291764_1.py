import random

#Function to simulate throwing two dices with 6 faces
#We return the values of those two dices
def zar_at():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)

    return dice1, dice2

#Determine score and goal
score = 0
dice1, dice2 = zar_at()
goal = dice1 + dice2

#If I get 7 or 11 on my first roll, I win!
#If I get 2, 3 or 12 on my first roll, I lose!
#If I get 4, 5, 6, 8, 9 or 10 the number I get becomes my goaled score
if goal == 7 or goal == 11:
    print(f"Kazanirsiniz, you rolled a {goal} on first try")
elif goal == 2 or goal == 3 or goal == 12:
    print(f"Kaybedersiniz, you rolled a {goal} on first try") 
else:
    print(f"You rolled a {goal}, this will be your goal point")
#Roll the dice until I get the goal score
    for p in range(1000):
        dice1, dice2 = zar_at()
        score = dice1 + dice2
        print(f"You rolled a(n) {score}")

        #If I roll a 7 before making the point, I lose!
        if score == 7:
            print(f"Kaybedersiniz, you rolled {score} before scoring {goal}")
            break
        if score == goal:
            print(f"Kazandiniz, rolled by {p+1} time(s)")
            break
        if score != goal:
            continue
