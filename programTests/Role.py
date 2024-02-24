from chessLib.move import KnightMove
from chessLib.position import Position


class BasicUtility:
    def __init__(self, position: Position, name="Basic"):
        self.position = position
        self.name = name
        self.state = "live"

    def currentPosition(self) -> Position:
        print(f"The chess position is [{self.position.x} {self.position.y}] now")
        return self.position
    

    def move(self, destination: Position):
        if (destination.x, destination.y) in self.allPosition():
            print(f"{self.name} moves from [{self.position.x} {self.position.y}] to [{destination.x} {destination.y}]")
            self.position = destination
        else:
            raise ValueError(f"[{destination.x} {destination.y}] does not meet the requirements for {self.name}")

    def isInBoard(self, x, y: int) -> bool:
        return (1 <= x <= 8 and 1 <= y <= 8)


class NewKnightMove(BasicUtility,KnightMove):
    def __init__(self, position: Position, name="Knight"):
        super().__init__(position, name)

    def allPosition(self) -> list:
        positions = []
        for position in self.valid_moves(self.position):
            positions.append((position.x,position.y))
        return positions


class QueenMove(BasicUtility):
    def __init__(self, position: Position, name="Queen"):
        super().__init__(position, name)

    def allPosition(self) -> list:
        positions = []
        for i in range(4):
            qx = 0
            qy = 0
            if i < 2:
                qx = 1 - 2 * (i % 2)

            else:
                qy = 1 - 2 * (i % 2)
            for i in range(1, 8):
                newX = self.position.x + qx * i
                newY = self.position.y + qy * i
                if self.isInBoard(newX, newY):
                    positions.append((newX, newY))
                else:
                    break
        for i in range(4):
            qx = 1 - 2 * (i % 2)
            if i < 2:
                qy = 1
            else:
                qy = -1
            for i in range(1, 8):
                newX = self.position.x + qx * i
                newY = self.position.y + qy * i
                if self.isInBoard(newX, newY):
                    positions.append((newX, newY))
                else:
                    break
        return positions


class BiShopMove(BasicUtility):
    def __init__(self, position: Position, name="BiShop"):
        super().__init__(position, name)

    def allPosition(self) -> list:
        positions = []
        for i in range(4):
            qx = 1 - 2 * (i % 2)
            if i < 2:
                qy = 1
            else:
                qy = -1
            for i in range(1, 8):
                newX = self.position.x + qx * i
                newY = self.position.y + qy * i
                if self.isInBoard(newX, newY):
                    positions.append((newX, newY))
                else:
                    break
        return positions
