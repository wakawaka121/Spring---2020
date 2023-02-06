"""
File: cb_utils.py
Author: Derek Tominaga
Description: contains functions to creating a representation
of a cracker barrel game, change the board if a move is legal.
Course: CSC 120, Spring 2020
"""
import moves

def empty_board(n):
    assert n > 0
    board = []
    count = 0
    for i in range(n):
        row_dict = {}
        for j in range(i+1):
            row_dict[count] = "0"
            count+=1
        board.append(row_dict)
    return board

def set_board(n, board_str):
    board = empty_board(n)
    count = 0
    for i in board:
        for j in i:
            i[count] = board_str[count]
            count+=1
    return board

def legal_move(board,mov):
    legal_status = [False, False, False]
    for i in board:
        if mov[0] in i and i[mov[0]] == "1":
            legal_status[0] = True
        if mov[1] in i and i[mov[1]] == "1":
            legal_status[1] = True
        if mov[2] in i and i[mov[2]] == "0":
            legal_status[2] = True
    if False in legal_status:
        return False
    else:
        return True

def legal_move_interface(board_str, mov):
    legal_status = [False,False,False]
    for hole in range(len(mov)):
        if hole <= 1 and board_str[mov[hole]] == "1":
            legal_status[hole] = True
        if hole > 1 and board_str[mov[hole]] == "0":
            legal_status[hole] = True
    if False in legal_status:
        return False
    else:
        return True

def all_legal_moves(size,board):
    legal_set = set()
    all_moves = moves.all_moves(size)
    for move in all_moves:
        if legal_move(board, move) == True:
            legal_set.add(move)
    return legal_set

def all_legal_moves_interface(size, board_str):
    legal_set = set()
    all_moves = moves.all_moves(size)
    for move in all_moves:
        if legal_move_interface(board_str,move) == True:
            legal_set.add(move)
    return legal_set

def update_board(board,mov):
    for position in board:
        if mov[0] in position:
            position[mov[0]] = "0"
        if mov[1] in position:
            position[mov[1]] = "0"
        if mov[2] in position:
            position[mov[2]] = "1"
    return board

def update_board_interface(board_str,mov):
    new_board = ""
    for i in range(len(board_str)):
        if i not in (mov[0],mov[1],mov[2]):
            new_board += board_str[i]
        else:
            if i in (mov[0],mov[1]):
                new_board += "0"
            else:
                new_board += "1"
    return new_board

"""
def main():
    new_board = empty_board(4)
    print(new_board)
    game_board = set_board(new_board, "110001100101011")
    print(game_board)
    new_game_board = update_board(game_board, (0,1,3))
    print(new_game_board)
    moves = all_legal_moves(5,game_board)
    print(moves)
    print(legal_move(game_board, (5,4,3)))
    print (legal_move_interface("110001100101011", (14,13,12)))
    print(all_legal_moves_interface(5,"110001100101011"))
    print(all_legal_moves_interface(4,"0110011011"))
    print(len("110001100101011"))
    print( update_board_interface("110001100101011", (0,1,3) )   )
main()
"""
#print(all_legal_moves_interface(4,"0111111111"))