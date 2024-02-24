from Role import NewKnightMove,QueenMove,BiShopMove,BasicUtility
import random
from chessLib.position import Position


class PlayGame():
    def __init__(self):
        boards = []
        for i in range(8):
            col = ["0"]*8
            boards.append(col)
        self.boards = boards
        self.points = []
        self.database = {}


    def customrizedPlayWithComputer(self,):
        '''
        start the game to play with computer
        '''
        print("--------------------- prepared ---------------------")
        print(
            f"your  position [{self.player.position.x} {self.player.position.y}] computer position [{self.computer.position.x} {self.computer.position.y}]")
        print("---------------------game start---------------------")
        self.showBoard()
        cp = self.computer.name[0].lower()
        up = self.player.name[0].lower()
        while True:
            print("the round of player")
            while True:
                x1 = int(input("please input the x axis of player"))
                y1 = int(input("please input the y axis of player"))
                if (x1,y1) in self.player.allPosition():
                    break
                else:
                    print(f"you can not position your pawns at that places [{x1} {y1}]")
            self.newDots(x1, y1, up)
            self.newDots(self.player.position.x, self.player.position.y, "0")
            self.database[(x1, y1)] = up
            del self.database[(self.player.position.x, self.player.position.y)]
            self.player.move(Position(x1, y1))
            if self.is_live(self.computer) == False:
                print("you win the game")
                break
            print()
            print("the round of computer")
            lengthc = len(self.computer.allPosition())
            if (self.player.position.x,self.player.position.y) in self.computer.allPosition():
                print(f"{self.computer.name} moves from [{self.computer.position.x} {self.computer.position.y}] to [{self.player.position.x} {self.player.position.y}]")
                print("you lose the game")
                break
            flag = False
            for des in self.computer.allPosition():
                if des not in self.player.allPosition():
                    flag = True

            while True:
                des = self.computer.allPosition()[random.randint(0, lengthc - 1)]
                if des not in self.player.allPosition() or not flag:
                    break
            self.newDots(des[0], des[1], cp)
            self.newDots(self.computer.position.x, self.computer.position.y, "0")
            self.database[(des[0], des[1])] = cp
            del self.database[(self.computer.position.x, self.computer.position.y)]
            self.computer.move(Position(des[0], des[1]))
            self.showBoard()




    def customrizedPlayWithPlayer(self, ):
        '''
        start the game to play with another player
        '''
        print("--------------------- prepared ---------------------")
        print(f"player1  position [{self.player1.position.x} {self.player1.position.y}] player2 position [{self.player2.position.x} {self.player2.position.y}]")
        print("---------------------game start---------------------")
        self.showBoard()
        p1 = self.player1.name[0].lower()
        p2 = self.player2.name[0].lower()
        while True:
            print("the round of player1")
            while True:
                x1 = int(input("please input the x axis of player 1"))
                y1 = int(input("please input the y axis of player 1"))
                if (x1,y1) in self.player1.allPosition():
                    break
                else:
                    print(f"you can not position your pawns at that places [{x1} {y1}]")
            self.newDots(x1, y1, p1)
            self.newDots(self.player1.position.x, self.player1.position.y, "0")
            self.database[(x1, y1)] = p1
            del self.database[(self.player1.position.x, self.player1.position.y)]
            self.player1.move(Position(x1, y1))
            if self.is_live(self.player2) == False:
                print("player 1 win the game")
                break
            print()
            print("the round of player2")
            while True:
                x2 = int(input("please input the x axis of player 1"))
                y2 = int(input("please input the y axis of player 1"))
                if (x2, y2) in self.player2.allPosition():
                    break
                else:
                    print(f"you can not position your pawns at that places [{x2} {y2}]")
            self.newDots(x2, y2, p2)
            self.newDots(self.player2.position.x, self.player2.position.y, "0")
            self.database[(x2, y2)] = p2
            del self.database[(self.player2.position.x, self.player2.position.y)]
            self.player2.move(Position(x2, y2))
            if self.is_live(self.player1) == False:
                print("player 2 win the game")
                break
            self.showBoard()






    def autoPlay(self,moveNums):
        '''
        you can just let the game excute automatically
        Parameters
        moveNums:the rounds game is played automatically
        '''
        for i in range(moveNums):
            if i%3==0 and self.knight.state=="live":
                lengthk = len(self.knight.allPosition())
                des = self.knight.allPosition()[random.randint(0,lengthk-1)]
                self.newDots(des[0],des[1],"k")
                self.newDots(self.knight.position.x,self.knight.position.y,"0")
                self.database[(des[0],des[1])]="k"
                del self.database[(self.knight.position.x,self.knight.position.y)]
                self.knight.move(Position(des[0],des[1]))
                if self.is_live(self.bishop) == False and self.is_live(self.queen) == False:
                    print("knight win the game")
                    break
            if i%3==1 and self.queen.state=="live":
                lengthq = len(self.queen.allPosition())
                des = self.queen.allPosition()[random.randint(0,lengthq-1)]
                self.newDots(des[0], des[1], "q")
                self.newDots(self.queen.position.x, self.queen.position.y, "0")
                self.database[(des[0],des[1])] = "q"
                del self.database[(self.queen.position.x,self.queen.position.y)]
                self.queen.move(Position(des[0],des[1]))
                if self.is_live(self.knight) == False and self.is_live(self.bishop) == False:
                    print("queen win the game")
                    break
            if i%3==2 and self.bishop.state=="live":
                lengthb = len(self.bishop.allPosition())
                des = self.bishop.allPosition()[random.randint(0,lengthb-1)]
                self.newDots(des[0], des[1], "b")
                self.newDots(self.bishop.position.x, self.bishop.position.y, "0")
                self.database[(des[0],des[1])] = "b"
                del self.database[(self.bishop.position.x,self.bishop.position.y)]
                self.bishop.move(Position(des[0],des[1]))
                if self.is_live(self.knight) == False and self.is_live(self.queen) == False:
                    print("bishop win the game")
                    break
        self.showBoard()


    def setup(self,):
        '''
        please input the positions of knight, queens and bishop in order
        '''
        kx = int(input("please submit the position of knight in x axis"))
        ky = int(input("please submit the position of knight in y axis"))
        qx = int(input("please submit the position of queen in x axis"))
        qy = int(input("please submit the position of queen in y axis"))
        bx = int(input("please submit the position of bishop in x axis"))
        by = int(input("please submit the position of bishop in y axis"))

        self.knight = NewKnightMove(Position(kx,ky))
        self.queen = QueenMove(Position(qx,qy))
        self.bishop = BiShopMove(Position(bx,by))
        self.newDots(kx,ky,"k")
        self.newDots(qx,qy,"q")
        self.newDots(bx,by,"b")
        self.newPlayer(kx,ky,"k")
        self.newPlayer(qx,qy,"q")
        self.newPlayer(bx,by,"b")

        self.showBoard()


    def randomSetup(self,):
        '''
        you can set an unpredictable start
        '''
        nums = []
        for i in range(6):
            nums.append(random.randint(1,8))
        self.knight = NewKnightMove(Position(nums[0], nums[1]))
        self.queen = QueenMove(Position(nums[2], nums[3]))
        self.bishop = BiShopMove(Position(nums[4], nums[5]))
        self.newDots(nums[0],nums[1], "k")
        self.newDots(nums[2],nums[3], "q")
        self.newDots(nums[4],nums[5], "b")
        self.newPlayer(nums[0],nums[1], "k")
        self.newPlayer(nums[2],nums[3], "q")
        self.newPlayer(nums[4],nums[5], "b")
        self.showBoard()


    def custmorized_setup(self,):
        while True:
            key = input("enter 1 to play with the computer\nenter 2 to play with another player")
            if key == "1" or key == "2":
                break
            else:
                print("wrong input")
        if key == "1":
            key2 = input("please input the role type of computer\n"
                         "k represents knight,q represents queen, b represents bishop")
            key3 = input("please input the role type of yourself\n"
                         "k represents knight,q represents queen, b represents bishop")
            self.computer = self.set_player(key2)
            self.player = self.set_player(key3)
            self.newDots(self.computer.position.x,self.computer.position.y,key2)
            self.newPlayer(self.computer.position.x,self.computer.position.y,key2)
            self.newDots(self.player.position.x,self.player.position.y,key3)
            self.newPlayer(self.player.position.x,self.player.position.y,key3)
            self.customrizedType = "p2c"

        if key == "2":
            key2 = input("please input the role type of palyer1\n"
                         "k represents knight,q represents queen, b represents bishop")
            key3 = input("please input the role type of palyer2\n"
                         "k represents knight,q represents queen, b represents bishop")
            self.player1 = self.set_player(key2)
            self.player2 = self.set_player(key3)
            self.newDots(self.player1.position.x, self.player1.position.y, key2)
            self.newPlayer(self.player1.position.x, self.player1.position.y, key2)
            self.newDots(self.player2.position.x, self.player2.position.y, key3)
            self.newPlayer(self.player2.position.x, self.player2.position.y, key3)
            self.customrizedType = "p2p"


    def set_player(self,key:str) -> BasicUtility:
        """
        to create a new player
        :param key: the type of the player
        :return: a newly created player
        """
        nums = []
        for i in range(2):
            nums.append(random.randint(1, 8))
        if key.lower() == "k":
            return NewKnightMove(Position(nums[0],nums[1]))
        if key.lower() == "q":
            return QueenMove(Position(nums[0], nums[1]))
        if key.lower() == "b":
            return BiShopMove(Position(nums[0], nums[1]))
        raise ValueError("wrong input of key for set_player")






    def newPlayer(self, x, y: int, types: str):
        '''
        record the players still alive
        '''
        self.database[(x, y)] = types


    def newDots(self, x, y: int, types: str):
        '''
        to change the board when we move a player
        '''
        self.boards[8 - y][x - 1] = types

    def showBoard(self):
        '''
        0 represents empty,k represents knight,q represents queen, b represents bishop
        '''
        print("-----------------")
        print("The Chess Game")
        for col in self.boards:
            for i in range(len(col)):
                print(col[i]+"\t",end="")
            print()
        print("----------------->")
        print()


    def showPointsinBoard(self,):
        '''
        exhibit the existing participants
        '''
        for point in self.points:
            print(f"[{point[0]} {point[1]}] --> {self.boards[8-point[1]][point[0]+1]}")


    def is_live(self,player :BasicUtility) -> bool:
        '''
        judge whether a player is still alive
        '''
        if self.boards[8-player.position.y][player.position.x-1] != player.name[0].lower() and player.state=="live":
            player.state = "dead"
            print(f"the {player.name[0]} in [{player.position.x} {player.position.y}] is killed by {self.boards[8-player.position.y][player.position.x-1]}")
            return False
        return True

