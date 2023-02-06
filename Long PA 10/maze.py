"""
File: maze.py
Author: Derek Tominaga
Description: This file contains a class that defines
a maze object. The maze can represet all possible paths
between vertecies.
Course: CSC 120, Spring 2020
"""
class Maze:
    """
    This class represents a maze object, it is represented
    by vertex and their connections to one another.
    _maze attribute is private.

    Contains Methods to:
        __init__: constructor
        _build_maze: builds a dictionary, that represents
        a vertex and all possible direct connections.
        solve: used to find a possible path from one
        vertex to another.
        solve_helper: helper funciton to recursively
        find a path.

    """

    def __init__(self,edge_list):
        """
        This constructor method takes one parameter
        to construct the a maze object.
        edge_list: is a list of list, each inner list
        has two strins that represent a vertex and a direct
        neighboring vertex.
        """
        self._maze = self._build_maze(edge_list)


    def _build_maze(self, edge_list):
        """
        This method takes one parameter to build
        the pp(possible path) connections from
        a vertex.
        edge_list: is a list of list, each inner list
        has two strings that represent a vertex and its
        a direct "neighbor/connection".
        retun: a maze_dict, which is a dictionary with keys
        as a vertex and values as a set of possible connections
        """
        maze_dict = {}
        for edge in edge_list:
            if edge[0] in maze_dict:
                maze_dict[edge[0]].add(edge[1])
            if edge[1] in maze_dict:
                maze_dict[edge[1]].add(edge[0])
            if edge[0] not in maze_dict:
                maze_dict[edge[0]] = set(edge[1])
            if edge[1] not in maze_dict:
                maze_dict[edge[1]] = set(edge[0])
        return maze_dict


    def solve(self,src,dest):
        """
        This method takes 2 parameters to find a path
        from a vertex to another vertex.
        slove method will call a helper method
        that will recursively find a path if one exists.
        src: is a string, that represent the vertex from
        which you start.
        dest: represent the vertex that is the destination
        return: is a list of strings that represents the
        path(multiple paths may exists) from src to dest.
        """
        visited = []
        return self.solve_helper(src, dest, visited)

    def solve_helper(self, src, dest, visited):
        """
        This method takes 3 parameters and functions
        recursively to help solve find a path form
        one vertx to another w/o getting caught in
        a loop or going to the same vertext twice.
        src: is a string, that represent the vertex from
        which you start.
        dest: a string represent the vertex that is the
        destination
        return: a list of strings that represent the
        path(multiple paths may exists) from src to dest
        """
        if src in visited:
            return None
        if src == dest:
            return [src]
        else:
            visited.append(src)
            for vertex in self._maze[src]:
                #potential path vertex
                pp_vertex = self.solve_helper(vertex,dest,visited)
                if pp_vertex is not None:
                    return [src] + pp_vertex