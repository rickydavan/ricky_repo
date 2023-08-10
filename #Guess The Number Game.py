#Guess The Number Game
import random

def guess_number():
  """Plays a game of guess the number."""

  # Generate a random number between 1 and 100.
  number = random.randint(1, 100)

  # Ask the user to guess the number.
  guess = -1
  while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))

    # Tell the user if their guess is too high or too low.
    if guess > number:
      print("Your guess is too high.")
    elif guess < number:
      print("Your guess is too low.")

  # Tell the user if they guessed the number correctly.
  if guess == number:
    print("Congratulations! You guessed the number!")

if __name__ == "__main__":
  guess_number()
