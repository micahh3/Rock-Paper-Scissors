# Rock Paper Scissors! Day 4

print("Welcome to Rock, Paper, Scissors! Please decide who will be P1 and P2.")
p1 = input("You will be Player 1! What is your name?")
p2 = input("You will be Player 2! What is your name?")

p1 = input("Rock, Paper, or Scissors?")
p2 = input("Rock, Paper, or Scissors?")

# P1 and P2 TIE
if p1 == ("Scissors") and p2 == ("Scissors"):
    print("Tie")
    
if p1 == ("Rock") and p2 == ("Rock"):
    print("Tie")

if p1 == ("Paper") and p2 == ("Paper"):
    print("Tie")



if p1 == ("Rock") and p2 == ("Scissors"):
        print("P1 wins!")

if p1 == ("Rock") and p2 == ("Paper"):
        print("P2 wins!")

if p1 == ("Scissors") and p2 == ("Paper"):
        print("P1 wins!")

if p1 == ("Paper") and p2 == ("Rock"):
        print("P1 wins!")

if p1 == ("Scissors") and p2 == ("Rock"):
        print("P2 wins!")

if p1 == ("Paper") and p2 == ("Scissors"):
        print("P2 wins!")


#DONE
    



