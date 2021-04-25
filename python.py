# Start Variables Scores Players
Score_Player_One = 0
Score_Player_Two = 0
# End Variables Scores Players


# Start Variables Name Players
Name_Player_One = input("Please Player One Enter Your Name : ")
Name_Player_Two = input("Please Player Two Enter Your Name : ")
# End Variables Name Players


while True:
    # Start Section See the Result
    if (Score_Player_One == 3 or Score_Player_Two == 3):
        print("******************** See The Results ********************")
        print(f"Results {Name_Player_One} Is {Score_Player_One}")
        print(f"Results {Name_Player_Two} Is {Score_Player_Two}")
        break
    # End Section See the Result


    # Start Variables Players
    Player_One = input("Please Player One Enter rock or paper or scissors : ")
    Player_Two = input("Please Player Two Enter rock or paper or scissors : ")
    # End Variables Players


    # Start If Player One For Information Entrance
    if (Player_One == "rock" or Player_One == "paper" or Player_One == "scissors"):
        print(f"Player One Is : {Player_One}")
    else:
        Player_One = input("Please Player One Enter rock or paper or scissors : ")
    # End If Player One For Information Entrance


    # Start If Player Two For Information Entrance
    if (Player_Two == "rock" or Player_Two == "paper" or Player_Two == "scissors"):
        print(f"Player Two Is : {Player_Two}")
    else:
        Player_Two = input("Please Player Two Enter rock or paper or scissors : ")
    # End If Player Two For Information Entrance


    # Start If For Rules of the game
    if (Player_One == "rock" and Player_Two == "rock"):
        print(f"{Name_Player_One} Is Equal {Name_Player_Two}")
    elif (Player_One == "rock" and Player_Two == "paper"):
        print(f"{Name_Player_Two} Is Wins")
        Score_Player_Two+=1
    elif (Player_One == "rock" and Player_Two == "scissors"):
        print(f"{Name_Player_One} Is Wins")
        Score_Player_One+=1


    if (Player_One == "paper" and Player_Two == "paper"):
        print(f"{Name_Player_One} Is Equal {Name_Player_Two}")
    elif (Player_One == "paper" and Player_Two == "rock"):
        print(f"{Name_Player_One} Is Wins")
        Score_Player_One+=1
    elif (Player_One == "paper" and Player_Two == "scissors"):  
        print(f"{Name_Player_Two} Is Wins")
        Score_Player_Two+=1


    if (Player_One == "scissors" and Player_Two == "scissors"):
        print(f"{Name_Player_One} Is Equal {Name_Player_Two}")
    elif (Player_One == "scissors" and Player_Two == "rock"):
        print(f"{Name_Player_Two} Is Wins")
        Score_Player_Two+=1
    elif (Player_One == "scissors" and Player_Two == "paper"):
        print(f"{Name_Player_One} Is Wins")
        Score_Player_One+=1
    # End If For Rules of the game