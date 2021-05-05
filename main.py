### Para correrlo python3 main.py

class Neighbours:
    def setNeighbour(self,direction,box):
        setattr(self, direction, box)


class SquareNeighbours(Neighbours):
    def __init__(self,top=None, bottom= None, left = None, right = None):
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left


class HexagonNeighbours(Neighbours):
    def __init__(self,top=None, bottom= None, 
        topLeft = None, topRight = None, 
        bottomLeft=None, bottomRight=None, 
        twoRight=None,twoLeft=None):
        self.top = top
        self.bottom = bottom
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.twoLeft = twoLeft
        self.twoRight = twoRight



class Box: 
    def __init__(self,neighbours = None, value = None, position=0): 
        self.neighbours = neighbours
        self.value = value
        self.position = position

    def addNeighbour(self,direction,box):
        self.neighbours.setNeighbour(direction,box)

    def getPosition(self):
        return self.position
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def printValueOrPosition(self):
        if not self.value:
            print(self.position, end="   ")
        else:
            print(self.value,end="   ")

        


class SquareBox(Box):
    def __init__(self,neighbours = None, value = None, position=0): 
        neighbours = SquareNeighbours()
        super().__init__(neighbours,value,position)


class HexagonBox(Box):
    def __init__(self,neighbours = None, value = '', position=0): 
        neighbours = HexagonNeighbours()
        super().__init__(neighbours,value,position)


class Board:
    def __init__(self, initial_box=None):
        self.initial_box = initial_box

class Piece:
    def __init__(self, initial_box=None):
        self.wasUsed = False
        self.initial_box = initial_box


class SquarePiece(Piece):
    def __init__(self, box0 = None):
        if not box0:
            box0 = SquareBox()
        super().__init__(box0)
    
    def printPiece(self):
        i = self.initial_box
        j = self.initial_box

        while i != None:
            while j!= None:
                j.printValueOrPosition()
                j = j.neighbours.right
            print("")
            i = i.neighbours.bottom
            j = i


class SquareBoard(Board):
    def __init__(self):
        box0 = SquareBox()
        super().__init__(box0)
        self.generateBoard()
    
    def printBoard(self):

        i = self.initial_box
        j = self.initial_box

        while i != None:
            while j!= None:
                j.printValueOrPosition()
                j = j.neighbours.right
            print("")
            i = i.neighbours.bottom
            j = i

    def findBoxWithPosition(self,target):

        i = self.initial_box
        j = self.initial_box

        while i != None:
            while j!= None:
                position = j.getPosition()
                if position == target:
                    return j

                j = j.neighbours.right

            i = i.neighbours.bottom
            j = i
            
    
    def isPiecePlacementValid(self,piece,position):
        if piece.wasUsed == True:
            return False

        boxInPosition = self.findBoxWithPosition(position)  
        initBoxPiece = piece.initial_box
        i = initBoxPiece
        j = initBoxPiece
        k = boxInPosition 
        l = boxInPosition
        
        valid = True

        while i != None and k != None:
            while j!= None and l != None:
                value = l.getValue()
                if value != None:
                    valid = False              
                l = l.neighbours.right
                j = j.neighbours.right
            
            k = k.neighbours.bottom
            l = k 
            i = i.neighbours.bottom
            j = i

        if (i != None or j != None):
            valid = False

        return valid

    def takePiece(self,piece,position):
        # Quitar pieza del tablero
        boxInPosition = self.findBoxWithPosition(position)  
        initBoxPiece = piece.initial_box
        i = initBoxPiece
        j = initBoxPiece
        k = boxInPosition 
        l = boxInPosition
        piece.wasUsed = False

        while i != None and k != None:
            while j!= None and l != None:
                l.setValue(None)
                l = l.neighbours.right
                j = j.neighbours.right
            
            k = k.neighbours.bottom
            l = k 
            i = i.neighbours.bottom
            j = i



    def putPiece(self,piece,position):
        if self.isPiecePlacementValid(piece,position):

            boxInPosition = self.findBoxWithPosition(position)  
            initBoxPiece = piece.initial_box
            i = initBoxPiece
            j = initBoxPiece
            k = boxInPosition 
            l = boxInPosition
            piece.wasUsed = True

            while i != None and k != None:
                while j!= None and l != None:
                    value = j.getValue()
                    l.setValue(value)
                    l = l.neighbours.right
                    j = j.neighbours.right
                
                k = k.neighbours.bottom
                l = k 
                i = i.neighbours.bottom
                j = i
        else: 
            print("Invalido")
            

        if self.checkWin():
            print("Felicidades, ganaste")

    def checkWin(self):
        i = self.initial_box
        j = self.initial_box

        while i != None:
            while j!= None:
                value = j.getValue()
                if value == None:
                    return False

                j = j.neighbours.right

            i = i.neighbours.bottom
            j = i
        
        return True
            


    
    def generatePiecesForBoard(self):
        # Aqui se generarian las piezas pero para fines de este 
        # ejercicio se van a hardcodear

        pieces = []

        #PIEZA A
        ###########
        # A A   0 1
        # A A   2 3 
        # A A   4 5

        box0 = SquareBox(value='A',position=0)
        box1 = SquareBox(value='A',position=1)
        box2 = SquareBox(value='A',position=2)
        box3 = SquareBox(value='A',position=3)
        box4 = SquareBox(value='A',position=4)
        box5 = SquareBox(value='A',position=5)
    

        #Vecinos pieza A

        #box0
        box0.addNeighbour('bottom', box2)
        box0.addNeighbour('right', box1)

        #box1
        box1.addNeighbour('left', box0)
        box1.addNeighbour('bottom', box3)

        #box2
        box2.addNeighbour('top', box0)
        box2.addNeighbour('right', box3)
        box2.addNeighbour('bottom', box4)

        #box3
        box3.addNeighbour('top', box1)
        box3.addNeighbour('bottom', box5)
        box3.addNeighbour('left', box2)

        #box4
        box4.addNeighbour('top', box2)
        box4.addNeighbour('right', box5)
       
        #box5
        box5.addNeighbour('top', box3)
        box5.addNeighbour('left', box4)

        #Crear Pieza
        pieceA = SquarePiece(box0)

         
        #Pieza B
        ##########
        # B B  0 1 
        # B B  2 3
        
        box0 = SquareBox(value='B',position=0)
        box1 = SquareBox(value='B',position=1)
        box2 = SquareBox(value='B',position=2)
        box3 = SquareBox(value='B',position=3)

        #Vecinos pieza B

        #box0
        box0.addNeighbour('bottom', box2)
        box0.addNeighbour('right', box1)

        #box1
        box1.addNeighbour('left', box0)
        box1.addNeighbour('bottom', box3)
    
        #box2
        box2.addNeighbour('top', box0)
        box2.addNeighbour('right', box3)

        #box3
        box3.addNeighbour('top', box1)
        box3.addNeighbour('left', box2)

        #Crear Pieza
        pieceB = SquarePiece(box0)

        #Pieza C
        ######
        # C C   0 1
        box0 = SquareBox(value='C',position=0)
        box1 = SquareBox(value='C',position=1)

        #Vecinos
        box0.addNeighbour('right', box1)
        box1.addNeighbour('left', box0)

        #Crear Pieza
        pieceC = SquarePiece(box0)

        pieces.append(pieceA)
        pieces.append(pieceB)
        pieces.append(pieceC)

        return pieces


    def generateBoard(self):
         # Aqui se generaria el tablero pero para fines de este
        # ejercicio se va a hardcodear.
        # Tablero 0  1  2  3
        #         4  5  6  7
        #         8  9  10 11

        #Generando las boxes
        box1 = SquareBox(position=1)
        box2 = SquareBox(position=2)
        box3 = SquareBox(position=3)
        box4 = SquareBox(position=4)
        box5 = SquareBox(position=5)
        box6 = SquareBox(position=6)
        box7 = SquareBox(position=7)
        box8 = SquareBox(position=8)
        box9 = SquareBox(position=9)
        box10 = SquareBox(position=10)
        box11 = SquareBox(position=11)



        #Colocando los vecinos
        #box0
        self.initial_box.addNeighbour('right',box1)
        self.initial_box.addNeighbour('bottom',box4)
        
        #box1
        box1.addNeighbour('left',self.initial_box)
        box1.addNeighbour('right',box2)
        box1.addNeighbour('bottom',box5)

        #box2
        box2.addNeighbour('left',box1)
        box2.addNeighbour('right',box3)
        box2.addNeighbour('bottom',box6)

        #box3
        box3.addNeighbour('left', box2)
        box3.addNeighbour('bottom', box7)

        #box4
        box4.addNeighbour('top',self.initial_box)
        box4.addNeighbour('right',box5)
        box4.addNeighbour('bottom',box8)

        #box5
        box5.addNeighbour('left',box4)
        box5.addNeighbour('right',box6)
        box5.addNeighbour('top',box1)
        box5.addNeighbour('bottom',box9)

        #box6
        box6.addNeighbour('top',box2)
        box6.addNeighbour('bottom',box10)
        box6.addNeighbour('right',box7)
        box6.addNeighbour('left',box5)

        #box7
        box7.addNeighbour('top',box3)
        box7.addNeighbour('bottom',box11)
        box7.addNeighbour('left',box6)

        #box8
        box8.addNeighbour('top',box4)
        box8.addNeighbour('right',box9)

        #box9
        box9.addNeighbour('top',box5)
        box9.addNeighbour('left', box8)
        box9.addNeighbour('right', box10)

        #box10
        box10.addNeighbour('left',box9)
        box10.addNeighbour('right',box11)
        box10.addNeighbour('top',box6)

        #box11
        box11.addNeighbour('top',box7)
        box11.addNeighbour('left',box10)


def main():
    board = SquareBoard()
    print("Tablero")
    board.printBoard()
    print(" ")
    pieceA, pieceB, pieceC = board.generatePiecesForBoard()
    print("Pieza A")
    pieceA.printPiece()
    print(" ")
    print("Pieza B")
    pieceB.printPiece()
    print(" ")
    print("Pieza C")
    pieceC.printPiece()
    print(" ")
    print("Colocar pieza A en tablero")
    board.putPiece(pieceA, 0)
    board.printBoard()
    print("Colocar pieza A de nuevo (es inválido)")
    board.putPiece(pieceA, 0)
    print(" ")
    board.printBoard()
    print("Colocar pieza B en posicion inválida (es inválido)")
    board.putPiece(pieceB, 0)
    board.printBoard()
    print(" ")
    print("Colocar pieza B en tablero")
    board.putPiece(pieceB, 2)
    board.printBoard()
    print("")
    print("Retirar pieza B del tablero")
    board.takePiece(pieceB, 2)  
    board.printBoard()
    print("")
    print("Colocar pieza C en tablero")
    board.putPiece(pieceC, 10)
    board.printBoard()
    print("")

    print("Colocar pieza B de nuevo")
    board.putPiece(pieceB, 2)
    board.printBoard()

    input("Press Enter to continue...")

if __name__ == "__main__":
   main()
