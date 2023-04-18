import random

def play_rps():
    # Display game instructions
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose your move by entering the corresponding number:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # Get user input
    user_move = int(input("What's your move? "))

    # Generate computer move
    computer_move = random.randint(1, 3)

    # Determine winner
    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == 1 and computer_move == 3) or \
         (user_move == 2 and computer_move == 1) or \
         (user_move == 3 and computer_move == 2):
        print("You won!")
    else:
        print("Computer won!")

    # Display computer move
    if computer_move == 1:
        print("Computer chose Rock")
    elif computer_move == 2:
        print("Computer chose Paper")
    else:
        print("Computer chose Scissors")
        
  
  play_rps()
