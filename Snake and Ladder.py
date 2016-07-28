
#TESTING#TESTINGAGAING
import time
import random
from itertools import cycle

def activePlayers(playerList):
    """Method to determine how many players will play(Max of 4)"""
    active_players = 0
    time.sleep(0.5)
    done = False
    while done is not True: 
        for player in playerList:
            valid_input = False
            while valid_input is not True:
                active_prompt = input("{0} | 1)Playing 2)Not Playing".format(player["name"]))
                if active_prompt == "1":
                    player["active"] = True
                    print("{0} is active".format(player["name"]))
                    active_players = active_players + 1
                    valid_input = True
                elif active_prompt == "2":
                    player["active"] = False
                    print("{0} is not active".format(player["name"]))
                    valid_input = True
                else:
                    print("Invalid input. Try again")
                    time.sleep(0.5)
        if active_players <= 0:
            time.sleep(0.5)
            print("You can't start a game with no players. Try Again")
        else:
            done = True

def assignBots(playerList):
    """Method to assign if players will be bots or human"""
    time.sleep(0.5)
    for player in playerList:
        if player["active"] is True:#Check if player is active
            valid_input = False
            while valid_input is not True:
                bot_prompt = input("{0} | 1)User 2)Bot".format(player["name"]))
                if bot_prompt == "2":
                    player["bot"] = True
                    print("{0} is assigned as a bot".format(player["name"]))
                    valid_input = True
                elif bot_prompt == "1":
                    player["bot"] = False
                    print("{0} is assigned as a user".format(player["name"]))
                    valid_input = True
                else:
                    print("Invalid input. Try again")
            time.sleep(0.5)
        else:
            None#...
            
def enterName(playerList):
    """Method for entering a name for the player, and automatically generate a random name for bots"""
    time.sleep(0.5)
    bot_names = ["Snek Bot", "Saitama Bot", "Ekans Bot", "Arbok Bot", "Moon Moon Bot", "Alpha Bot", "Gear Bot", "Sparky Bot", "Rob Bot", "Isetron Bot", "Sneople Bot"]
    for player in playerList:
        previous_name = player["name"]
        time.sleep(0.5)
        if player["active"] is True:
            if player["bot"] is True:
                generated_name = random.randrange(0, len(bot_names))
                name = bot_names[generated_name]
                bot_names.pop(generated_name)
            else:
                name = input("{0} | Enter your name".format(player["name"]))
            player["name"] = name
            print("{0} changed name to {1}".format(previous_name, name))
            
        else:
            None


def rollDice():
    """This method is for rolling dice"""
    print("Rolling dice...")
    time.sleep(1)
    for i in range(1,4):
        time.sleep(0.3)
        print("-")
    time.sleep(0.4)
    rolled_number =random.choice(range(1,7))
    print("-{0}-".format(rolled_number))
    time.sleep(1)
    return rolled_number


def playerTurn(player):
    """Function for each turn of the player"""
    if player["active"] is True:
        time.sleep(0.5)
        print("-----|-----|-----")
        time.sleep(0.1)
        print("{0}'s turn".format(player["name"]))
        time.sleep(0.5)
        #-----Roll Dice-----
        roll_valid = False
        while roll_valid is not True:
            if player["bot"] is not True:
             
                roll_dice = input("Type 'r' to roll dice")
            elif player["bot"] is True:#Automatically roll if the player is a bot
                roll_dice = "r"
                roll_valid = True
            if roll_dice == "r":
                player["score"] += rollDice()
                time.sleep(0.5)
                print("{0}'s position is now {1}".format(player["name"], player["score"]))
                roll_valid = True
            else:
                print("Invalid Response")
            time.sleep(0.5)
    else:
        None

def snakeAndLadder_check(player):
    """This method checks if the player landed on a snake or a ladder, and change the player's current position to a new one"""
    snakes = {99:62,97:84,95:75,92:89,84:67,81:41,77:64,73:53,66:55,63:43,59:22,57:44,50:31,33:13,37:4,39:22,23:3,29:12,14:5,19:2,45:36, 87:67, 91:70}#Positions of snakes in the board
    ladders = {1:20, 6:35, 10:30, 17:24, 25:36,28:48,34:46,40:61,43:58,49:52,51:90,54:67,65:85,72:89,79:82,83:96,88:93, 26:56}#Positions of ladders in the board
    if player["score"] in snakes:#Code for when the player landed on snake
        pointsEarned = -10
        print("{0} encountered a snake on {1}!!".format(player["name"], player["score"]))
        time.sleep(1)
        player["score"] = snakes[player["score"]]
        print("{0} has been sent back to {1}".format(player["name"], player["score"]))
        time.sleep(0.5)
    elif player["score"] in ladders:#Code for when the player landed on ladder
        pointsEarned = 10
        print("Oh look, you found a ladder on {0}. {1} goes forward to {2}".format(player["score"], player["name"], ladders[player["score"]]))
        time.sleep(0.5)
        updatePoints(player,pointsEarned)
        player["score"] = ladders[player["score"]]
        
def checkForWin(player):
    """This method checks if the player won by having over 100 score"""
    win = False
    if player["score"] >= 100:#100
        win = True
    else:
        win = False
    return win


def resetScore(playerList):
    """Method for resetting the player's score"""
    for player in playerList:
        player["score"] = 0

def displayScore(playerList):
    """Function to display the player's score"""
    for player in playerList:
        if player["active"] is True:
            print("{0} : {1}".format(player["name"], player["score"]))
            
        else:
            None
            
def menuSettings(setting):
    print("---Settings---")
    time.sleep(0.5)
    settings_loop = 0
    for i in setting:
        setting_counter += 1#WIP
        print("{0}:{1}".format(i,setting[i]))
    print("1)Change Setting 2)Return to Main Menu")
    while settings_loop == 0:
        settings_loop = 1


def updatePoints(player, n):
    player["points"] += n
    if n < 0:
        print("{0} points".format(n))
    elif n > 0:
        print("+{0} points".format(n))
    time.sleep(0.5)

def main():
    program_running = True
    while program_running is True:#MAIN LOOP FOR THE ENTIRE PROGRAM
        #MAIN MENU
        print("-----Main Menu-----")
        time.sleep(0.5)
        mainMenu_prompt = input("1)Start Game 2)Settings 3)How to play")
        time.sleep(0.5)
        if mainMenu_prompt == "1":
            print("---Start Game---")
            #------Initialize players------
            player1 = {"name" : "Player1", "score": 0 ,"points": 0}
            player2 = {"name" : "Player2", "score": 0 ,"points": 0 }
            player3 = {"name" : "Player3", "score": 0 ,"points": 0}
            player4 = {"name" : "Player 4", "score": 0 ,"points": 0}
            players = [player1, player2, player3, player4]
            activePlayers = []
            #----Decide active players----
            activePlayers(players)#Determine active players
            print("-----|-----|-----")
            assignBots(players)#Determine bots in the game
            print("-----|-----|-----")
            enterName(players)#Enter name for each available players
            print("-----|-----|-----")
            #-------Start Game-------
            match_played = False
            playing_game = True
            print("Start match")
            while playing_game is True:#Loop for playing the game
                if match_played is True:#MENU AFTER A MATCH HAS BEEN PLAYED
                    afterMatch_prompt = input("1)Play Again 2)Main Menu 3)Exit Game")
                    if afterMatch_prompt == "1":
                        resetScore(players)
                    elif afterMatch_prompt == "2":#GO BACK TO MAIN MENU
                        playing_game = False
                        break
                    elif afterMatch_prompt == "3":#Exit Game
                        exit()#)@#)@(#)@()#(FIX ROLL VALIDITY
                match_over = False
                while match_over is not True:#Loop for playing a match
                    match_played = True
                    time.sleep(1)
                    for player in players:#Players turn
                        if match_over is True:
                            break
                        playerTurn(player)#Player Turns
                        snakeAndLadder_check(player)#Check for snake or ladders
                        displayScore(players)#Display scores of each players
                        if checkForWin(player) is True:#CHECK FOR WINNERS
                           time.sleep(0.5)
                           print("We have a winner!")
                           time.sleep(0.7)
                           print("{0} won with a score of {1}".format(player["name"], player["score"]))
                           match_over = True
                           time.sleep(1)
        elif mainMenu_prompt == "2":
            settings = {"resistSnakes":False, "Option2":True, "Option3":True,"Option 4":False}
            menuSettings(settings)
        elif mainMenu_prompt == "3":
            print("---Tutorial---")
        else:
            print("Invalid Response. Try again")
    time.sleep(0.5)
main()
