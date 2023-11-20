import random

class JungleGame:
    def __init__(self, players):
        self.players = players
        self.deck = self.create_deck()
        self.hands = {player: [] for player in players}

    def create_deck(self):
        symbols = ["Lion", "Monkey", "Snake", "Elephant", "Parrot"]
        deck = symbols * 10  # 10 cards for each symbol
        random.shuffle(deck)
        return deck

    def distribute_cards(self):
        for _ in range(5):
            for player in self.players:
                card = self.deck.pop()
                self.hands[player].append(card)

    def play_round(self):
        for player in self.players:
            print(f"{player}'s turn:")
            self.display_hand(player)
            choice = input("Choose a card to play: ")
            if choice in self.hands[player]:
                self.hands[player].remove(choice)
                print(f"{player} played {choice}")
            else:
                print("Invalid choice. Try again.")

    def display_hand(self, player):
        print(f"{player}'s hand: {', '.join(self.hands[player])}")

    def calculate_scores(self):
        scores = {player: 0 for player in self.players}
        for player in self.players:
            for card in self.hands[player]:
                # Assign scores based on card values (you can customize this part)
                if card == "Lion":
                    scores[player] += 5
                elif card == "Monkey":
                    scores[player] += 3
                elif card == "Snake":
                    scores[player] += 2
                elif card == "Elephant":
                    scores[player] += 4
                elif card == "Parrot":
                    scores[player] += 1
        return scores

    def play_game(self):
        self.distribute_cards()

        for _ in range(5):  # 5 rounds
            self.play_round()

        scores = self.calculate_scores()
        winner = max(scores, key=scores.get)
        print(f"\nGame Over! {winner} wins with {scores[winner]} points.")

if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2 to 5): "))
    if 2 <= num_players <= 5:
        players = [input(f"Enter the name of player {i+1}: ") for i in range(num_players)]
        game = JungleGame(players)
        game.play_game()
    else:
        print("Invalid number of players. Please enter a number between 2 and 5.")
