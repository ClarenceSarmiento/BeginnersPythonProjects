"""Create a Number Guessing Bot that will guess the
user's number. """

import random
import colorama
from colorama import Fore, Style


def title():
    colorama.init()
    print(Fore.GREEN)
    print("""  _   _                 _                  _____                     _               ____        _   
 | \\ | |               | |                / ____|                   (_)             |  _ \\      | |  
 |  \\| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |_) | ___ | |_ 
 | . ` | | | | '_ ` _ \\| '_ \\ / _ \\ '__| | | |_ | | | |/ _ \\/ __/ __| | '_ \\ / _` | |  _ < / _ \\| __|
 | |\\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\\__ \\__ \\ | | | | (_| | | |_) | (_) | |_ 
 |_| \\_|\\__,_|_| |_| |_|_.__/ \\___|_|     \\_____|\\__,_|\\___||___/___/_|_| |_|\\__, | |____/ \\___/ \\__|
                                                                              __/ |                  
                                                                             |___/     """)
    print(Style.RESET_ALL)


def user_number():
    # prompts the user for the secret number
    secret_number = int(input("Enter your secret number: "))
    return secret_number


def bot(sec_num, start, end, life):
    while life != 0:
        # Bot will randomly selected random numbers from 0 to 100
        random_number = random.randint(start, end)
        # Check the random number if not equal to the secret number, if True, execute the following codes.
        if random_number != sec_num:
            print(f"Bot[life:{life}]: 'Human - is your number {random_number}?'")
            response = str(input("User: ")).lower()
            if response == "lower":
                if sec_num < random_number:
                    end = random_number - 1
                    bot(sec_num, start, end, life - 1)
                    break
                else:
                    print(f"Bot: 'Human - You cheated! Your number is {sec_num} and my guessed is {random_number}.'\n")
                    break
            elif response == "higher":
                if sec_num > random_number:
                    start = random_number + 1
                    bot(sec_num, start, end, life - 1)
                    break
                else:
                    print(f"Bot: 'Human - You cheated! Your number is {sec_num} and my guessed is {random_number}.'\n")
                    break
            else:
                print("Bot: 'Human - You entered an Invalid Response.'\n")
                break
        else:
            print("Bot: 'Human - I guessed your number!'")
            print(f"Bot: 'Human - Your number is {random_number}!'\n")
            break
    else:
        print("\nGame Over!!!")
    return True


def play(game):
    while not game:
        game = bot(user_number(), start=0, end=100, life=8)
        if game:
            ask = str(input("Bot: 'Human - Do you want to play again? y/n:' ")).lower()
            print()
            if ask == "y":
                game = False
                play(game)
            elif ask == "n":
                game = True
                play(game)
    else:
        exit()


title()
play(False)
