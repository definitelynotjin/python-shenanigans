import random


def guessing_random_num():
    secret_num = random.randint(1, 10)
    player_name = str(input("Welcome traveler, insert your name: "))
    print(
        f"Very well, {player_name}. I have chosen a number, now it's your job to guess. 3 chances or you'll be dead"
    )
    for attempt in range(3):
        try:
            guess = int(input(f"Guess {attempt + 1}/3: "))
            if guess == secret_num:
                print(f"You have won, {player_name}. The number was {secret_num}")
                break
            elif guess > secret_num:
                print("Too high")
            else:
                print("Too low")
        except ValueError:
            print("That is not a number")
        continue
    else:
        print(f"You have lost, {player_name}. The number was {secret_num}")


guessing_random_num()
