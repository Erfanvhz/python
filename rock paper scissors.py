def rps_game(player1_choice, player2_choice):
    choices = ['rock', 'paper', 'scissors']

    if player1_choice not in choices or player2_choice not in choices:
        return "please choose : (rock,paper,scissors)"

    if player1_choice == player2_choice:
        
        return "even! both players chose same thing"

    if (
        (player1_choice == 'rock' and player2_choice == 'scissors') or
        (player1_choice == 'paper' and player2_choice == 'rock') or
        (player1_choice == 'scissors' and player2_choice == 'paper')
    ):
        return "player one won! ".format(player1_choice, player2_choice)
    else:
        return "player two won! ".format(player2_choice, player1_choice)

#input
player1_choice = input("player one, choose : rock or paper or scissors? ")
player2_choice = input("player two, choose : rock or paper or scissors? ")

#result
result = rps_game(player1_choice, player2_choice)
print(result)
