import random;

options = ["R","P","S"]

#function to check the rules for a winner 
def check_move(player_choice, comp_choice):
    if (player_choice == comp_choice):
        return True;
    elif (player_choice == "R" and comp_choice == "S"):
        return "player won";
    elif (player_choice == "S" and comp_choice == "R"):
        return "CPU won";
    elif (player_choice == "P" and comp_choice == "R"):
        return "player won";
    elif (player_choice == "R" and comp_choice == "P"):
        return "CPU won";
    elif (player_choice == "S" and comp_choice == "P"):
        return "player won";
    elif (player_choice == "S" and comp_choice == "P"):
        return "CPU won";

#converts list char to equivalent word
def char_to_word(char):
    if (char == "R"):
        return "Rock"
    elif (char == "P"):
        return "Paper"
    else:
        return "Scissors" 

def game():
    #checks if user input is present in list
    while(True):
        player_choice = input("pick an option between R, P, S:\n");
        if (player_choice in options):
            break;
        print("Input selection is invalid\n");
    
    #gets the computer choice
    cpu_choice = random.choice(options);
    print(f"Player ({char_to_word(player_choice)}): CPU ({char_to_word(cpu_choice)})");
    #checks for winner or a tie
    result = check_move(player_choice, cpu_choice);

    if (result == True): game(); #for a tie, the game runs again
    else: print(result);


game();
