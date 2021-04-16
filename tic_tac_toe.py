# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:39:49 2021

@author: Dusan
"""
# Last modified on 16.04.2021
# ----- Global Variables -----

# Game Board
board = ["-", "-","-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still goin
game_still_going = True

# Who won? Or Tie? 
winner = None

# Whos turn is it
current_player = "X"


def display_board(): 
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Play the game of tic tac toe
def play_game():
    
    # Display initial board
    display_board()
    
    #While the game is still going
    while game_still_going:
        
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        # Check if the game has ended
        check_if_game_over()
        
        # Flip to the other player
        flip_player()
        
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
        

# Handle a single turn of an arbitraty player
def handle_turn(player):
    
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:
        while  position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input, Choose the position from 1-9: ")
        
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("You cant go there, try again!")
    
    board[position] = player
    display_board()
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Set up global variable
    global winner
    # Check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
    

def flip_player():
    # Global variables we need
    global current_player
    # If one was playing, the other one has a turn
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows habe all the same value(and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3: 
        game_still_going = False 
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the colums habe all the same value(and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3: 
        game_still_going = False 
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the diagonal habe all the same value(and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2: 
        game_still_going = False 
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return
play_game()


# board
# display board
# paly game
# handle turn 
# check win
    # Check rows
    # check columns
    # check diagonals 
# check tie
# flip player


