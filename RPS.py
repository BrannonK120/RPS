#
#       project: lyrics finder and counter
#        author: Lucas Gonzalez<lgonzalez2918617@woonsocketschools.com>
#        author: Brannon Khounvichith<bkhounvichith2818353@woonsocketschools.com>
#
#  date written: 10/10/2024
#
#   description:RpsVL
#

value=True
player1num=0
player2num=0
print("Rock Paper Scissors Lizard Spock")
print("Please put only Capital R,P,S,V for Spock,and L for Lizard")
while value:
    name1 = input("What is your name you will be player one? :")
    name2 = input("What is your name you will be player two? :")
    player1 = input("Player one what would you like to select(P,R or S,V,L)? :")
    player2 = input("Player two what would you like to select(P,R or S,V,L)?? :")
    if player1=="R" and player2=="S":
        print("Player 1 has won")
        player1num+=1

    if player1=="S" and player2=="S":
        print("Draw")
        continue1 = input("Would you like to continue? :")
        player1num+=0
        player2num+=0

    if player1 == "R" and player2 == "S":
        print("Player 1 has won")
        player1num+=1


    if player1 == "S" and player2 == "R":
        print("Player 2 has won")
        player2num+=1


    if player1 == "P" and player2 == "S":
        print("Player 2 has won")
        player1num+=1


    if player1 == "S" and player2 == "P":
        print("Player 1 has won")
        player1num+=1

    if player1 == "R" and player2 == "P":
        print("Player 2 has won")
        player2num+=1

    if player1 == "P" and player2 == "R":
        print("Player 1 has won")
        player1num+=1
    if player1=="P" and player2=="P":
        print("Draw")
        player1num += 0
        player2num += 0

    if player1 =="S" and player2=="S":
        print("Player 2 wins")
        player2num += 0
        player1num += 0

    if player1 == "L" and player2 == "R":
          print("Player 1 has won")
          player1num += 1

    if player1 =="R" and player2=="L":
        print("Player 2")
        player2num += 1

    if player1 =="L" and player2=="L":
        print("Draw")
        player1num += 0
        player2num += 0

    if player1 =="V" and player2=="V":
        print("Draw")
        player1num += 0
        player2num += 0

    if player1 =="L" and player2=="P":
        print("Player 1 wins")
        player1num += 1

    if player1 =="P" and player2=="L":
        print("Player 2 wins")
        player2num += 1

    if player1 =="S" and player2=="L":
        print("Player 1 wins")
        player1num += 1

    if player1 =="L" and player2=="S":
        print("Player 2 wins")
        player2num += 1

    if player1 =="L" and player2=="V":
        print("Player 1 wins")
        player1num += 1

    if player1 =="V" and player2=="L":
        print("Player 2 wins")
        player2num += 1

    if player1 =="V" and player2=="R":
        print("Player 1 wins")
        player1num += 1

    if player1 =="R" and player2=="V":
        print("Player 2 wins")
        player2num += 1

    if player1 =="V" and player2=="S":
        print("Player 1 wins")
        player1num += 1

    if player1 =="S" and player2=="V":
        print("Player 2 wins")
        player2num += 1

    if player1 =="V" and player2=="P":
        print("Player 2 wins")
        player2num += 1

    if player1 =="P" and player2=="V":
        print("Player 1 wins")
        player2num += 1



    print("Player one has",player1num,"wins and player 2 has",player2num,"wins")
    continue1=input("Do you want to continue? :")

    if continue1=="No" or continue1=="no":
        value=False
        print("The final score was",player1num,"for",name1,"and",player2num,"for",name2)
