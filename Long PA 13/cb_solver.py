"""
File: cb_solver.py
Author: Derek Tominaga
Description: This program will take a size and a config string
to find all solutions to the cracker barrel game. Will import cb_utils.py
Course: CSC 120, Spring 2020
"""

import moves
import cb_utils
import copy

def cb_one(size, config):
    """
    This functions takes two paramater to find a single
    solution to a cracker barrel game with a given
    configuration.
    size: is an int that determines number of "rows"
    config: is a string of 1's and 0's that give the
    status of the "board" (1 = pin exists, 0 = no pin)
    return: a string of list of tuples telling a solution
    (multiple may be possible, but only one is returned)
    """
    assert size >=4
    #calls helper to formate into a string
    return str((cb_one_helper(size,config)))

def cb_one_helper(size,config):
    """
    This function takes two paramaters to assists
    cb_one and recursively find the solution to
    cb_one.
    size: is a int that determines number of "rows"
    config: is a string of 1's and 0's that give the
    status of the "board" (1 = pin exists, 0 = no pin)
    return: a list of tuples
    """
    game_board = cb_utils.set_board(size, config)
    pins = 0
    if is_solved(game_board):
        return []
    #use all_legal_moves_interface with size and config to get all
    ##possible moves, (config will change as you recurse deeper)
    for move in cb_utils.all_legal_moves_interface(size,config):
        new_board_str = cb_utils.update_board_interface(config,move)
        recursive_moves = cb_one_helper(size, new_board_str)
        if recursive_moves is not None:
            return [move] + recursive_moves

def cb_all(size,config):
    """
    This functions takes two paramater to find all
    solutions to a cracker barrel game with a given
    configuration.
    size: is an int that determines number of "rows"
    config: is a string of 1's and 0's that give the
    status of the "board" (1 = pin exists, 0 = no pin)
    return: a string of a set of lists of tuples telling all
    possible solutions
    """
    assert size >= 4
    #moves made for a solution
    moves_solution = []
    #all solutions
    solution_paths = set()
    #gets internal representation of the board(list of dictionaries)
    board_status = cb_utils.set_board(size, config)
    cb_all_helper(board_status, moves_solution,solution_paths)
    if len(solution_paths) == 0:
        return None
    else:
        return solution_paths

def cb_all_helper(board_status, moves_solution, solution_paths):
    """
    This function takes three paramaters to assists
    cb_all and recursively find the solution to
    cb_all.
    board_status: is a list of dicionaries, number of dicionaries
    corresponds to number of rows, number elements in each
    dictionary corresponds to number of pins in each row.
    moves_solution: is a list of tuples, that represent a move
    all tuples in move_solution will lead to a soultion
    solution_paths: is a set of list of tuples that represent all
    possible moes to find a solution
    """
    moves = cb_utils.all_legal_moves(len(board_status), board_status)
    if len(moves) == 0 and is_solved(board_status):
        #updates solution_paths with a path of moves
        solution_paths.add(str(moves_solution))
    else:
        for move in moves:
            board_copy = copy.deepcopy(board_status)
            new_board_status = cb_utils.update_board(board_copy,move)
            cb_all_helper(new_board_status, moves_solution + [move], solution_paths)


def is_solved(board_status):
    """
    This function takes one paramater to determine of
    the game is solved or now.
    board_status: is internal representation of the boar
    (is a list of dicionaries)
    return: a boolean
    """
    number_of_pins = 0
    #each row is a dict
    for row in board_status:
        #each pin is a key of a dict
        for pin,status in row.items():
            if status == "1":
                number_of_pins += 1
    #more then one pin means not solved
    if number_of_pins > 1:
        return False
    else:
        return True
