from tkinter import *
from tkinter.colorchooser import *
import json
import sys
import math
import time
import random

# Game dimensions:
CELL_SIZE = 22
NUM_ROWS = 15
NUM_COLS = 15
# Width and height are +1 because of the extra pixels added by grid lines.
# +4 and the end because tkinter canvas won't draw pixels if either co-ordinate is below 4?
WIDTH  = 1 + (CELL_SIZE + 1) * NUM_ROWS + 4
HEIGHT = 1 + (CELL_SIZE + 1) * NUM_COLS + 4

DELAY = 150
SOLID_WALLS = True

# Colours:
SNAKE_DEFAULT_COLOUR = "#FF3300"
GRID_BACKGROUND_COLOUR_1 = "#000066"
GRID_BACKGROUND_COLOUR_2 = "#191975"
GRID_LINE_COLOUR = "#4D4D94"
WINDOW_TITLE = "Multisnake"
DEFAULT_FONT = ("Arial", "12")

class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        return Vector2(self.x + vec.x, self.y + vec.y)

    def toString(self):
        return "x: {0}, y: {1}".format(self.x, self.y)
    
class Snake():
    def __init__(self, idNum, name, colour, startPos):
        self.idNum = idNum
        self.name = name
        self.colour = colour
        self.startPos = startPos

        # Set defaults
        self.gridPos = Vector2(startPos.x, startPos.y)
        self.direction = 0
        self.alive = True
        self.score = 0
        self.ready = False
        self.hasRoundStarted = False

    def reset(self):
        #creating a new Vector2 fixes bug where gridPos and startPos refer to the same memory location
        self.gridPos = Vector2(self.startPos.x, self.startPos.y)
        self.direction = 0
        self.alive = True
        self.ready = False
        self.hasRoundStarted = False

    def update(self):
        self.hasRoundStarted = True
        if self.alive:
            d = self.direction
            if d == 0:
                self.gridPos.y -= 1
            elif d == 1:
                self.gridPos.x += 1
            elif d == 2:
                self.gridPos.y += 1
            else:
                self.gridPos.x -= 1

    def canTurn(self, d):
        return sorted([self.direction,d]) != [0,2] and sorted([self.direction,d]) != [1,3]

    def turn(self, d):
        self.ready = True
        # Prevent the snake from turning back on itself, but if the round hasn't started yet they can turn where they like.

        if self.canTurn(d) or not self.hasRoundStarted:
            self.direction = d
        else:
            return

    def isReady(self):
        return self.ready

    def changePosModuloGridSize(self, gridWidth, gridHeight):
        self.gridPos.x %= gridWidth
        self.gridPos.y %= gridHeight

    def die(self):
        print("Snake with id {0} died!".format(self.idNum))
        self.alive = False
        return

class HumanSnake(Snake):
    def __init__(self, idNum, name, colour, startPos, inputManager, movementKeys):
        Snake.__init__(self, idNum, name, colour, startPos)
        self.isHuman = True

        # Bind movement keys.
        # Important not to do this in a loop or the lambdas will retain the value of the last loop variable
        inputManager.bind(movementKeys[0], lambda: self.turn(0))
        inputManager.bind(movementKeys[1], lambda: self.turn(1))
        inputManager.bind(movementKeys[2], lambda: self.turn(2))
        inputManager.bind(movementKeys[3], lambda: self.turn(3))

class ComputerSnake(Snake):
    def __init__(self, idNum, name, colour, startPos, strength):
        Snake.__init__(self, idNum, name, colour, startPos)
        self.strength = strength
        self.isHuman = False

    def isReady(self):
        return True

    def turn(self, gameBoard):
        if self.strength == 1:
            self.alg1(gameBoard)
        elif self.strength == 2:
            self.alg2(gameBoard)
        elif self.strength == 3:
            self.alg3(gameBoard)
        else:
            print("ERROR: no function found corresponding to snake strength of: " + str(self.strength))
            sys.exit()

    def alg1(self, gameBoard):
        # Greedy algorithm. Only look at the surrounding cells and pick one that's not solid.
        dirs = [0,1,2,3]
        random.shuffle(dirs)
        for d in dirs:
            if not self.canTurn(d):
                continue
            
            if d == 0:
                cell = Vector2(self.gridPos.x, self.gridPos.y-1)
            elif d == 1:
                cell = Vector2(self.gridPos.x+1, self.gridPos.y)
            elif d == 2:
                cell = Vector2(self.gridPos.x, self.gridPos.y+1)
            else:
                cell = Vector2(self.gridPos.x-1, self.gridPos.y)

            
            if gameBoard.getCellData(cell) == 0:# the cell is empty
                self.direction = d
                break

    def alg2(self, gameBoard):
        # Look two squares ahead and find the path with the most space.
        def getNeighbours(cell):
             return [Vector2(cell.x, cell.y-1),
                     Vector2(cell.x+1, cell.y),
                     Vector2(cell.x, cell.y+1),
                     Vector2(cell.x-1, cell.y)]

        # Return 0 if cell is not empty
        # Else get the number of open cells around the given cell
        def spaceFunc(cell):
            if gameBoard.getCellData(cell) != 0:
                return 0
            else:
                space = 0
                for c in getNeighbours(cell):
                    cellData = gameBoard.getCellData(c)
                    if cellData == 0: space += 1
                return space

        bestDir = 0
        bestSpaceFunc = 0

        # Introduce some non-determinism
        neighbours = getNeighbours(self.gridPos)
        dirs = [0,1,2,3]
        random.shuffle(dirs)
        for d in dirs:
            neighbour = neighbours[d]
            cellData = gameBoard.getCellData(neighbour)
            if cellData != 0:
                continue
            else:
                space = 0
                for c in getNeighbours(neighbour):
                    # Don't worry about it turning back and considering the current cell
                    # because the spaceFunc would be 0 anyway
                    space += spaceFunc(c)

                if space > bestSpaceFunc:
                    bestSpaceFunc = space 
                    bestDir = d

        self.direction = bestDir

    def alg3(self, gameBoard):
        # Uses floodfill to get the direction with the most available space.
        x = self.gridPos.x
        y = self.gridPos.y 
        neighbours = [(x, y-1), (x+1, y), (x,y+1), (x-1,y)]

        # Introduces randomness by shifting the possible directions a bit
        if random.random() < 0.2:
            shift = random.randint(0,3)
        else:
            shift = self.direction
        dirs = [0,1,2,3]
        dirs = dirs[shift:] + dirs[:shift]

        bestArea = 0
        bestDir  = self.direction
        checkedCells = set()
        for d in dirs:
            cell = neighbours[d]

            if gameBoard.getCellData(Vector2(*cell)) != 0 or cell in checkedCells:
                # it's solid or checked.
                continue
            else:
                (area, checked) = self.alg3_getArea(cell, gameBoard)
                checkedCells = checkedCells.union(checked)
                if area > bestArea:
                    bestArea = area 
                    bestDir = d

        self.direction = bestDir

    def alg3_getArea(self, cell, gameBoard):
        # assumes that the cell is empty
        area = 0
        checked = set() 
        stack = [cell] 

        while len(stack) > 0:
            (x, y) = stack.pop()

            if not (x,y) in checked and gameBoard.getCellData(Vector2(x,y)) == 0:
                area += 1
                checked.add((x,y))
                if x > 0:
                    stack.append((x - 1, y))
                if x < (gameBoard.width - 1):
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < (gameBoard.height - 1):
                    stack.append((x, y + 1))

        return (area, checked)

class GameBoard():
    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.board = []
        for i in range (0, height):
            self.board.append([])
            for j in range(0, width):
                self.board[i].append(0)

    def reset(self):
        for i in range (0, self.height):
            for j in range(0, self.width):
                self.board[i][j] = 0

    # mark the cell as occupied with the respective snake's id number
    def markCell(self, vecPos, idNum):
        self.board[vecPos.y][vecPos.x] = idNum

    def _isCellOutOfBounds(self, vecPos):
        isTooSmall = vecPos.y < 0 or vecPos.x < 0
        isTooLarge = vecPos.y > self.height - 1 or vecPos.x > self.width - 1
        return isTooSmall or isTooLarge

    def getCellData(self, vecPos):
        # cellData is -1 for out of bounds, 0 for empty or something > 0 for occupied
        if self._isCellOutOfBounds(vecPos):
            return -1
        else:
            return self.board[vecPos.y][vecPos.x]

    def didSnakeHitSomething(self, snake):
        data = self.getCellData(snake.gridPos)
        if data == 0:
            return False
        else:
            return True

class InputManager():
    def __init__(self):
        self.bindings = {}
        MASTER.bind('<KeyPress>', self.handleKeyPress) # unbind from input_manager

    def handleKeyPress(self, event):
        key = event.keysym
        if key in self.bindings:
            self.bindings[key]()

    def bind(self, keySym, callback):
        self.bindings[keySym] = callback

    def unbindAll(self):
        self.bindings = {}
        MASTER.unbind('<KeyDown>') # unbind from input_manager

class UIManager():
    def __init__(self, master):
        self.master = master
        self.widgets = {}
        self.defaultFont = ("Arial", "12")

    def setupGame(self, snakes):
        headings = ["Name", "Colour", "Score"]
        numRowsUsed = 0
        for i in range(0, len(headings)):
            w = Label(self.master, font=("Arial","12", "bold"), justify="center", text=headings[i])
            w.grid(row=0, column=i)

        numRowsUsed += 1

        self.widgets["snakeInfo"] = {}
        for snake in snakes:
            snakeWidgets = {}
            name = Label(self.master, font=self.defaultFont, justify="center", text=snake.name)
            name.grid(row=numRowsUsed, column=0)
            snakeWidgets["name"] = name

            colour = Canvas(self.master, width=30, height=30)
            colour.create_rectangle(0,0,30,30,fill=snake.colour)
            colour.grid(row=numRowsUsed, column=1)
            snakeWidgets["colour"] = colour

            score = Label(self.master, font=self.defaultFont, justify="center", text=str(snake.score))
            score.grid(row=numRowsUsed, column=2)
            snakeWidgets["score"] = score

            self.widgets["snakeInfo"][snake.name] = snakeWidgets

            numRowsUsed += 1

        statusLine = Label(self.master, font=self.defaultFont, justify="center", text="")
        statusLine.grid(row=numRowsUsed, column=0, columnspan=3, pady=5)
        numRowsUsed += 1
        self.statusLine = statusLine

        canvas = Canvas(self.master, width=WIDTH, height=HEIGHT, borderwidth=2)
        canvas.grid(row=numRowsUsed, column=0, columnspan=3, pady=10, padx=10)
        self.canvas = canvas
        self.renderScenery()

    def updateSnakeScores(self, snakes):
        print("Updating snake scores.")
        for snake in snakes:
            print("Score: " + str(snake.score))
            self.widgets["snakeInfo"][snake.name]["score"]["text"] = str(snake.score)

        self.master.update_idletasks()

    def setStatusLine(self, msg):
        self.statusLine["text"] = msg

    def renderSnakes(self, snakes):
        for snake in snakes:
            if snake.alive == True:
                snakeHeadPosition = snake.gridPos
                self.renderSquare(snakeHeadPosition, snake.colour)

    def renderSquare(self, vecPos, colour=SNAKE_DEFAULT_COLOUR):
        # + 1px so as to not coincide with grid lines
        xpos = 4 + vecPos.x * (CELL_SIZE + 1) 
        ypos = 4 + vecPos.y * (CELL_SIZE + 1)
        
        self.canvas.create_rectangle(xpos,           ypos,
                                     xpos+CELL_SIZE, ypos+CELL_SIZE,
                                     fill=colour)
    
    def renderScenery(self):
        self.canvas.delete("all") # removes all leftover objects on the canvas
        for i in range(0, NUM_COLS + 1):
            x = (CELL_SIZE + 1) * i + 4
            self.canvas.create_line(x, 4, x, HEIGHT, fill=GRID_LINE_COLOUR)

        for i in range(1, NUM_ROWS + 1):
            y = (CELL_SIZE + 1) * i + 4
            self.canvas.create_line(4, y, WIDTH, y, fill=GRID_LINE_COLOUR)
            
        
        # Fill in the alternating cell background pattern
        colourNum = 1
        for i in range(0, NUM_ROWS):
            for j in range(0, NUM_COLS):
                if colourNum == 1:
                    colour = GRID_BACKGROUND_COLOUR_1
                    colourNum = 2
                else:
                    colour = GRID_BACKGROUND_COLOUR_2
                    colourNum = 1
                vec = Vector2(j,i)
                self.renderSquare(vec, colour)

            if NUM_COLS % 2 == 0:
                if colourNum == 2: colourNum = 1
                else: colourNum = 2

    def renderRoundOverBox(self, text):
        mid_xpos = WIDTH / 2
        mid_ypos = HEIGHT / 2
        box_width = min(200, WIDTH)
        padding = 10
        
        self.canvas.create_rectangle(mid_xpos - box_width/2, mid_ypos-75,
                                mid_xpos + box_width/2, mid_ypos+75,
                                fill="peach puff")
        self.canvas.create_text((mid_xpos, mid_ypos),
                           text=text,
                           font=("Arial", "24"),
                           justify="center",
                           width=box_width - 2*padding)

    def renderGameOverBox(self, text):
        mid_xpos = WIDTH / 2
        mid_ypos = HEIGHT / 2
        box_width = min(300, WIDTH)
        padding = 10
        
        self.canvas.create_rectangle(mid_xpos - box_width/2, mid_ypos-125,
                                mid_xpos + box_width/2, mid_ypos+125,
                                fill="peach puff")
        self.canvas.create_text((mid_xpos, mid_ypos),
                           text=text,
                           font=("Arial", "24"),
                           justify="center",
                           width=box_width - 2*padding)


class GameManager():
    def __init__(self, gameSettings):
        self.numRows = gameSettings["numRows"]
        self.numCols = gameSettings["numCols"]
        self.solidWalls = gameSettings["solidWalls"]
        self.speed = gameSettings["speed"]
        self.maxScore = gameSettings["maxScore"]

        # Fix this ugliness!
        global DELAY
        global NUM_ROWS
        global NUM_COLS
        global WIDTH
        global HEIGHT
        DELAY = 100 - self.speed + 10
        NUM_ROWS = self.numRows
        NUM_COLS = self.numCols
        WIDTH  = 1 + (CELL_SIZE + 1) * self.numCols + 4
        HEIGHT = 1 + (CELL_SIZE + 1) * self.numRows + 4

        
        self.numPlayers = 0
        self.playerData = []
        self.snakes = []
        self.gameBoard = GameBoard(NUM_ROWS, NUM_COLS)
        self.numDeadSnakes = 0
        self.gameOver = False
        self.allSnakesReady = False
        self.paused = False
        self.pauseTime = 0
        self.reRenderScenery = True
        self.UIManager = None #set in start

    def start(self, snakeData):        
        self.UIManager = UIManager(MASTER)
        self.InputManager = InputManager()
        self.numPlayers = len(snakeData)

        # Given n players, construct a n-sided regular polygon and use the vertices to decide on snake starting points.
        middlePoint = Vector2( round(NUM_COLS/2), round(NUM_ROWS/2) )
        radius = ((NUM_COLS/2) * 0.6 + (NUM_ROWS/2) * 0.6) / 2
        theta = 2*math.pi / self.numPlayers
        startPoints = []
        for i in range(0, self.numPlayers):
            x = radius * math.cos(theta * i)
            y = radius * math.sin(theta * i)
            point = Vector2.add(middlePoint, Vector2(round(x), round(y)))
            startPoints.append(point)

        # Create snake objects and add them to players list, using the starting points just created.
        for i in range(1, self.numPlayers + 1):
            idNum      = i
            name       = snakeData[i-1]["name"]
            colour     = snakeData[i-1]["colour"]
            startPoint = startPoints[i-1]
            isHuman    = snakeData[i-1]["isHuman"]

            if name == "":
                name = "Player " + str(idNum)

            if isHuman:
                keys = snakeData[i-1]["movementKeys"]
                s = HumanSnake(idNum, name, colour, startPoint, self.InputManager, keys)
            else:
                strength = snakeData[i-1]["strength"]
                s = ComputerSnake(idNum, name, colour, startPoint, strength)

            self.snakes.append(s)
            self.gameBoard.markCell(s.gridPos, s.idNum)
            print("Snake made. idNum: {0}, name: {1}".format(idNum, name))

        self.UIManager.setupGame(self.snakes)

    def endRound(self):
        print("Round over.")
        self.gameBoard.reset()
        self.allSnakesReady = False
        self.reRenderScenery = True 

        if self.numDeadSnakes == self.numPlayers: #multiple snakes died simultaneously so it's a draw
            self.UIManager.renderRoundOverBox("It's a draw!")
        else:
            for snake in self.snakes:
                if snake.alive:
                    winning_snake = snake
                    winning_snake.score += 1
                    if winning_snake.score == self.maxScore:
                        self.endGame(winning_snake)
                        return

            self.UIManager.renderRoundOverBox("{0} wins the round.".format(winning_snake.name))

        for snake in self.snakes:
            snake.reset()
            self.gameBoard.markCell(snake.gridPos, snake.idNum) #fixes bug where snake starting cell is not marked on grid

        self.UIManager.updateSnakeScores(self.snakes)
        self.numDeadSnakes = 0
        self.pause(1000)

    def endGame(self, winningSnake):
        print("Game ending.")
        self.gameOver = True

        secondHighestScore = 0
        for snake in self.snakes:
            if snake != winningSnake and snake.score > secondHighestScore:
                secondHighestScore = snake.score

        scoreDelta = winningSnake.score - secondHighestScore
        if scoreDelta > round(self.maxScore * 0.5):
            victoryMessage = "{0} demolishes the opposition!".format(winningSnake.name)
        elif scoreDelta > round(self.maxScore * 0.25):
            victoryMessage = "A sound victory by {0}.".format(winningSnake.name)
        else:
            victoryMessage = "{0} wins. A close game!".format(winningSnake.name)

        self.UIManager.updateSnakeScores(self.snakes)
        self.UIManager.renderGameOverBox("Game over. " + victoryMessage)
        self.InputManager.unbindAll()
        self.pause(5000)

    def pause(self, duration):
        self.paused = True
        self.pauseTime = duration

    def getSnakeById(self, idNum):
        return self.snakes[idNum-1]

    def update(self): 
        if self.numDeadSnakes >= self.numPlayers - 1:
            self.endRound()
            return
            
        if not self.allSnakesReady:
            numReadySnakes = 0
            for snake in self.snakes:
                if snake.isReady():
                    numReadySnakes += 1
                else:
                    idleSnake = snake

            if numReadySnakes == self.numPlayers:
                self.allSnakesReady = True
                self.UIManager.setStatusLine("Round started.")
            else:
                numSnakesToGo = self.numPlayers - numReadySnakes
                if numSnakesToGo == 1:
                    self.UIManager.setStatusLine("Still waiting for {0} to be ready. Come on!".format(idleSnake.name))
                else:
                    self.UIManager.setStatusLine("Still waiting for {0} players to be ready.".format(numSnakesToGo))

        else:
            for snake in self.snakes:
                if snake.alive:
                    if not snake.isHuman:
                        snake.turn(self.gameBoard)

                    snake.update()

                    cellData = self.gameBoard.getCellData(snake.gridPos)
                    if cellData == -1: #the snake hit a wall
                        if SOLID_WALLS:
                            snake.die()
                            self.numDeadSnakes += 1
                        else:
                            snake.changePosModuloGridSize(NUM_COLS, NUM_ROWS)
                            self.gameBoard.markCell(snake.gridPos, snake.idNum)
                    elif cellData == 0: #the snake is fine
                        self.gameBoard.markCell(snake.gridPos, snake.idNum)
                    else: # the snake hit an occupied cell
                        snake.die()
                        self.numDeadSnakes += 1
        
    def render(self):
        if self.reRenderScenery:
            self.reRenderScenery = False
            self.UIManager.renderScenery()
            self.UIManager.renderSnakes(self.snakes)
        else:
            self.UIManager.renderSnakes(self.snakes)

    def loop(self):
        if self.gameOver:
            # Restart main menu
            for child in MASTER.winfo_children():
                child.grid_forget()
            m = MainMenu(MASTER)
            m.start()
            print("Starting main menu.")
            return
            
        else:
            if self.reRenderScenery:
                for snake in self.snakes:
                    snake.ready = False #quick fix to stop snakes shooting off as soon as next round starts

            self.update()
            if self.paused:
                MASTER.after(DELAY + self.pauseTime, self.loop)
                self.paused = False
                self.pauseTime = 0
            else:
                self.render()
                MASTER.after(DELAY, self.loop)

class MainMenu():
    class PlayerEntryRow():
        def __init__(self, master, rowNum):
            self.deleted = False
            self.colourPickerColour = SNAKE_DEFAULT_COLOUR
            self.rowNum = rowNum
            self.name = ""
            self.colour = SNAKE_DEFAULT_COLOUR
            self.movementKeys = ['w','d','s','a']
            self.isComputer = False
            self.computerStrength = 1
            
            nameEntry = Entry(master, font=("Arial", "12"), justify="center")
            nameEntry.grid(row=rowNum, column=0)
            self.nameEntry = nameEntry

            colourPicker = Canvas(master, width=30, height=30)
            colourPicker.create_rectangle(0,0,30,30,fill=SNAKE_DEFAULT_COLOUR)
            colourPicker.grid(row=rowNum, column=1)
            colourPicker.bind("<Button-1>", self.editColour)
            self.colourPicker = colourPicker

            movementOptions = [
                "WASD",
                "YGHJ",
                "PL;'",
                "Arrow keys"
            ]
            defaultKeys = StringVar(master)
            defaultKeys.set(movementOptions[0])
            movementKeysPicker = OptionMenu(master, defaultKeys, *tuple(movementOptions))
            movementKeysPicker.grid(row=rowNum, column=2)
            self.movementKeysPicker = movementKeysPicker

            computerOption = IntVar()
            computerOption.set(0) #human by default
            isComputerCheckbutton = Checkbutton(master, variable=computerOption)
            isComputerCheckbutton.var = computerOption
            isComputerCheckbutton.grid(row=rowNum, column=3)
            self.isComputerCheckbutton = isComputerCheckbutton

            computerStrengthScale = Scale(master, from_=1, to=3, orient="horizontal")
            computerStrengthScale.grid(row=rowNum, column=4)
            self.computerStrengthScale = computerStrengthScale

            if rowNum > 2:
                # There must be a minimum of two players so don't allow the user to delete the 1st or 2nd player
                deleteButton = Button(master, font=DEFAULT_FONT, justify="center", text="Delete", command=self.delete)
                deleteButton.grid(row=rowNum, column=5)
                self.deleteButton = deleteButton

        def editColour(self, event):
            (rgbVals, colourString) = askcolor()
            self.colourPicker.create_rectangle(0,0,30,30,fill=colourString)
            self.colourPickerColour = colourString
            print("Edit colour: " + colourString)

        def getPlayerData(self):
            name = self.nameEntry.get()
            colour = self.colourPickerColour
            if self.isComputerCheckbutton.var.get() == 1:
                isComputer = True 
            else:
                isComputer = False
            strength = self.computerStrengthScale.get() 
            keys = self.movementKeysPicker["text"]
            if keys == "WASD":
                print("Keys: WASD")
                keys = ['w','d','s','a']
            elif keys == "YGHJ":
                print("Keys: YGHJ")
                keys = ['y','j','h','g']
            elif keys == "PL;'":
                print("Keys: PL;'")
                keys = ['p', 'quoteright', 'semicolon', 'l']
            elif keys == "Arrow keys":
                print("Keys: Arrow keys")
                keys = ['Up', 'Right', 'Down', 'Left']
            else:
                print("getPlayerData(): movementKeysPicker value not recognized! - " + keys)

            playerData = {}
            playerData["name"] = name
            playerData["colour"] = colour
            playerData["isHuman"] = not isComputer 
            playerData["strength"] = strength
            playerData["movementKeys"] = keys

            return playerData

        def delete(self):
            self.deleted = True
            # Delete all the widgets
            self.nameEntry.grid_forget()
            self.colourPicker.grid_forget()
            self.movementKeysPicker.grid_forget()
            self.deleteButton.grid_forget()
            self.isComputerCheckbutton.grid_forget()
            self.computerStrengthScale.grid_forget()

        #END OF PlayerEntryRow

    class GameSettings():
        def __init__(self, master):
            self.master = master
            # Field labels
            gridNumColsLabel = Label(master, text="Grid width", font=DEFAULT_FONT)
            gridNumRowsLabel = Label(master, text="Grid height", font=DEFAULT_FONT)
            speedScaleLabel  = Label(master, text="Speed", font=DEFAULT_FONT)
            solidWallsLabel  = Label(master, text="Solid walls?", font=DEFAULT_FONT)
            maxScoreLabel    = Label(master, text="Max score", font=DEFAULT_FONT)
            
            gridNumColsLabel.grid(row=0, column=0)
            gridNumRowsLabel.grid(row=0, column=1)
            speedScaleLabel.grid(row=0, column=2)
            solidWallsLabel.grid(row=0, column=3)
            maxScoreLabel.grid(row=0, column=4)
            
            # Fields
            self.gridNumColsScale   = Scale(master, from_=5, to=50, orient="horizontal")
            self.gridNumRowsScale   = Scale(master, from_=5, to=50, orient="horizontal")
            self.speedScale         = Scale(master, from_=1, to=100, orient="horizontal")
            solidWallsVar = IntVar()
            solidWallsVar.set(1)
            self.solidWallsCheckbutton = Checkbutton(master, variable=solidWallsVar)
            self.solidWallsCheckbutton.var = solidWallsVar
            self.maxScoreScale = Scale(master, from_=1, to=30, orient="horizontal")

            self.gridNumColsScale.set(30)
            self.gridNumRowsScale.set(30)
            self.speedScale.set(50)
            self.maxScoreScale.set(10)

            self.gridNumColsScale.grid(row=1, column=0)
            self.gridNumRowsScale.grid(row=1, column=1)
            self.speedScale.grid(row=1, column=2)
            self.solidWallsCheckbutton.grid(row=1, column=3)
            self.maxScoreScale.grid(row=1, column=4)

        def getGameSettings(self):
            numCols = self.gridNumColsScale.get()
            numRows = self.gridNumRowsScale.get()
            speed = self.speedScale.get()
            if self.solidWallsCheckbutton.var.get() == 1:
                solidWalls = True
            else:
                solidWalls = False
            maxScore = self.maxScoreScale.get()
            
            gameSettings = {"numCols": numCols, "numRows": numRows, "speed": speed, "solidWalls": solidWalls, "maxScore": maxScore}
            print("Game settings: " + str(gameSettings))
            return gameSettings

        #END OF GameSettings

    def __init__(self, master):
        self.master = master
        self.defaultFont = ("Arial", "12")
        self.numRowsUsed = 0
        self.ready = False
        self.playerEntryFrame = None # set in start method
        self.playerEntryRows = []

    def start(self):
        print("Started main menu")
        # Main title
        title = Label(self.master, font=("Arial", "16", "bold"), justify="center", text="Multisnake", padx=15, pady=15)
        title.grid(row=0, column=0)
        self.numRowsUsed += 1

        gameSettingsFrame = Frame(width=WIDTH, pady=10)
        gameSettingsFrame.grid(row=self.numRowsUsed)
        self.numRowsUsed += 1
        self.gameSettings = self.GameSettings(gameSettingsFrame)
        
        # Buttons
        buttonFrame = Frame(width=WIDTH)
        buttonFrame.grid(row=self.numRowsUsed, columnspan=3)
        # Add new player button
        newPlayerButton = Button(buttonFrame, text="Add a player", command=self.addPlayerEntryRow)
        newPlayerButton.grid(row=self.numRowsUsed, column=0)
        # Play button
        playButton = Button(buttonFrame, text="Play!", command=self.play)
        playButton.grid(row=self.numRowsUsed, column=1)
        # Quit button
        quitButton = Button(buttonFrame, text="Quit :(", command=self.quit)
        quitButton.grid(row=self.numRowsUsed, column=2)
        self.numRowsUsed += 1

        # Player entry frame
        self.playerEntryFrame = Frame()
        self.playerEntryFrame.grid(row=self.numRowsUsed)
        self.numRowsUsed += 1
        
        # Column headings
        headings = ["Name", "Colour", "Movement keys", "Is computer", "Computer strength"]
        for i in range(0, len(headings)):
            w = Label(self.playerEntryFrame, font=("Arial","12", "bold"), justify="center", text=headings[i])
            w.grid(row=0, column=i)

        # Should be a minimum of 2 players
        self.addPlayerEntryRow()
        self.addPlayerEntryRow()
        print("Finished creating menu widgets")

    def addPlayerEntryRow(self):
        row = self.PlayerEntryRow( self.playerEntryFrame, len(self.playerEntryRows)+1 ) #+1 due to labels row
        self.playerEntryRows.append(row) 
        
    def quit(self):
        self.master.destroy()
        sys.exit()

    def play(self):
        print("Playing game")
        playerData = []
        for row in self.playerEntryRows:
            if not row.deleted:
                playerData.append(row.getPlayerData())

        gameSettings = self.gameSettings.getGameSettings()

        # Remove all UI elements present.
        for child in MASTER.winfo_children():
            child.grid_forget()

        print("Player data: " + str(playerData))
        gm = GameManager(gameSettings)
        gm.start(playerData)
        gm.loop()

MASTER = Tk()
MASTER.wm_title(WINDOW_TITLE)
MASTER.resizable(width=False, height=False)

MAIN_MENU = MainMenu(MASTER)
MAIN_MENU.start()

MASTER.mainloop()
