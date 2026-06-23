import random

print("🎮 Number Guessing Game")

print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-200)")

choice = int(input("Choose difficulty (1/2/3): "))

if choice == 1:
    limit = 50
elif choice == 2:
    limit = 100
else:
    limit = 200

secret_number = random.randint(1, limit)
attempts = 0

print(f"\nGuess the number between 1 and {limit}")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"\n🎉 Correct! You guessed it in {attempts} attempts.")
        break
    