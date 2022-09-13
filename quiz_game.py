
from random import randint


print("choose a game to play")
playing = input("game 1  or game 2 \n")


def check(Ans, choice, x):
    if Ans == choice:
        x = x + 1
    return x


if playing == "game 1":

    value = randint(1, 5)
    po = int(input("guess a number from 1 to 5 =>"))
    # print(value)

    if value == po:
        print("correct ans")
    else:
        print(f"incorrect guess ,the correct answer was {value}")


else:
    p = 0
    print("Q1. first person to land on moon")
    print("Option A => Neil armstrong \nOption B => buzz Aldrin \nOption C =>me \nOption D => you \n")
    p = check("a", input("option "), p)

    print("Q2. who is the current prime miniter of india")
    print("Option A => Ramnath kovind\nOption B => Narendra /modi\nOption C =>Amit shah\nOption D =>Manmohan singh\n")
    p = check("b", input("option "), p)

    print("Your score is ", p)
