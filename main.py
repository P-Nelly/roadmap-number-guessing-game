import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.difficulty_levels = {
            1: ("Easy", 10),
            2: ("Medium", 5),
            3: ("Hard", 3)
        }
        self.high_scores = {
            "Easy": float('inf'),
            "Medium": float('inf'),
            "Hard": float('inf')
        }

    def welcome_message(self):
        print("\nWelcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}.")
        print("\nPlease select the difficulty level:")
        for level, (name, chances) in self.difficulty_levels.items():
            print(f"{level}. {name} ({chances} chances)")

    def get_difficulty(self):
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice in self.difficulty_levels:
                    difficulty, chances = self.difficulty_levels[choice]
                    print(f"\nGreat! You have selected the {difficulty} difficulty level.")
                    print("Let's start the game!")
                    return difficulty, chances
                print("Invalid choice. Please select a valid difficulty level.")
            except ValueError:
                print("Please enter a valid number.")

    def get_hint(self, target):
        hints = [
            f"The number is {'even' if target % 2 == 0 else 'odd'}",
            f"The number is between {(target // 10) * 10} and {(target // 10) * 10 + 10}",
            f"The sum of its digits is {sum(int(d) for d in str(target))}"
        ]
        return random.choice(hints)

    def play_round(self, difficulty, chances):
        target_number = random.randint(self.min_number, self.max_number)
        attempts = 0
        start_time = time.time()

        while attempts < chances:
            remaining = chances - attempts
            print(f"\nYou have {remaining} {'chance' if remaining == 1 else 'chances'} left.")
            
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < self.min_number or guess > self.max_number:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}.")
                    continue

                attempts += 1

                if guess == target_number:
                    elapsed_time = round(time.time() - start_time, 2)
                    print(f"\nCongratulations! You guessed the correct number in {attempts} attempts!")
                    print(f"Time taken: {elapsed_time} seconds")
                    
                    # Update high score
                    if attempts < self.high_scores[difficulty]:
                        self.high_scores[difficulty] = attempts
                        print(f"New high score for {difficulty} difficulty!")
                    
                    return True
                
                print("Incorrect!", end=" ")
                if guess < target_number:
                    print("The number is greater than your guess.")
                else:
                    print("The number is less than your guess.")

            except ValueError:
                print("Please enter a valid number.")

        print(f"\nGame Over! The number was {target_number}.")
        return False

    def display_high_scores(self):
        print("\n=== High Scores ===")
        for difficulty, score in self.high_scores.items():
            if score != float('inf'):
                print(f"{difficulty}: {score} attempts")
            else:
                print(f"{difficulty}: No high score yet")

    def play(self):
        while True:
            self.welcome_message()
            difficulty, chances = self.get_difficulty()
            self.play_round(difficulty, chances)
            
            if input("\nWould you like to play again? (y/n): ").lower() != 'y':
                self.display_high_scores()
                print("\nThanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play() 