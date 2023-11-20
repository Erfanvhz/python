import random

def fisherman_game():
    balance = 0
    prize_threshold = 100  # عدد خاص برای جایزه
    hook = False

    while True:
        print(f"Balance: ${balance}")
        
        weight = float(input("Enter the weight of fish (in kilograms, positive for buying, negative for selling): "))

        if weight > 0:
            cost = weight * 2
            balance -= cost
        else:
            earnings = -weight * 2
            balance += earnings

        if balance > prize_threshold and not hook:
            print("Congratulations! You've earned a prize (hook)!")
            hook = True

        if balance < 0:
            penalty = abs(balance) * 0.1
            balance -= penalty
            print(f"Oops! You've incurred a penalty of ${penalty}")

if __name__ == "__main__":
    fisherman_game()
