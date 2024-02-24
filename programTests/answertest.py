#Write your unit tests here
import time

from Game import PlayGame

def autoPlay():
    '''
    this function can start the game automatically with a knight,a queen and a bishop
    '''
    game = PlayGame()
    while True:
        key = input("press key r to player the auto game with a random start\n"
                    "press key s to play the auto game with customlized start")
        if key.lower()=="r" or key.lower()=="s":
            break
        print("please input in guidance")
    if key == "r":
        game.randomSetup()
    else:
        game.setup()
    while True:
        try:
            rounds = int(input("please input an integer which represents the rounds of the game"))
            break
        except:
            print("input an integer")
    game.autoPlay(rounds)


def customrizedPlay():
    '''
    in this fucntion,you can choose whether to play with the computer or to play with a person
    '''
    game = PlayGame()
    game.custmorized_setup()
    if game.customrizedType == "p2p":
        game.customrizedPlayWithPlayer()
    else:
        game.customrizedPlayWithComputer()


if __name__ == "__main__":
    while True:
        try:
            key = int(input("1.看电脑自己对战\n2.自己参与对战\n"))
            if key==2:
                customrizedPlay()
            else:
                autoPlay()
            break
        except:
            print("请输入1或2")

    time.sleep(20)

