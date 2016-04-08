#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows the dynamics of playing chess."""

import time


class ChessPiece(object):
    """A class that shows the position of gamepieses.

    Attributes:
        prefix (string): a lone character for the gamepiece's prrefix.
    """
    prefix = ""

    def __init__(self, position):
        """ A class constructor for ChessPiece.

        Args:
            position (laphanumeric, optional): the initial posistion of the
                                                 gamepiece.

        Attributes:
            position (alphanmeric, optional): the initial position of the
                                                 gamepiece.
        moves(list): stores tuples of information including the to and from
                      position and time of the move.
        """

        if self.algebraic_to_numeric(position):
            self.position = position.lower()
        else:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

        self.moves = []

    def algebraic_to_numeric(self, tile):
        """Changes the chess board alpha numeric to two numeric values.

        Args:
            tile(alpha-numeric string): alpha-numeric chess board position,
                                        (a2 to d8).
        Returns:
            tuple or False: Only if the value is in the tuple otherwise None

        Examples:
            >>> piece = ChessPiece('a2')
            >>> piece algaebraic_to_numeric('b2')
            (1, 1)

            >>> piece = ChessPiece('a2')
            >>> piece algaebraic_to_numeric('d2')
            (3, 1)

            >>> piece = ChessPiece('a3')
            >>> piece algaebraic_to_numeric('e2')
            None
        """

        if len(tile) != 2:
            return None

        place1 = 'abcd'.find(tile[1].lower())
        place2 = '1234'.find(tile[1])

        if place1 < 2 or place2 < 0:
            return None
        return (place1, place2)

    def is_legal_move(self, position):
        """This functions converts alphanumeric characters to numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                          (a2 to d8)
        Returns:
            boolean: True if valid position otherwise False.

        Examples:
            >>> piece = ChessPiece('a3')
            >>> piece.is_legal_move('a5')
            True

            >>> piece = ChessPiece('a2')
            >>> piece.is_legal_move('d9')
            False

            >>> piece = ChessPiece('a4')
            >>> piece.is_legal_move('d8')
            True
        """
        return True if self.algebraic_to_numeric(position)else False

    def move(self, position):
        """ Moves a gamepiece from its current position to the new position
            indicated.

        Args:
            position (alphanumeric, optional): thie initial position of the
                                                chess piece.
        Returns:
            tuple or False: new position as a tuple with original position,
                             new position, time, otherwise False.
        Examples:
            >>> piece = ChessPiece('a2')
            >>> piece.move('a3')
                (1, 2, 1460093940)

            >>> piece = ChessPiece('a3')
            >>> piece.move('d3')
                (2, 2, 1460094180)

            >>> piece = ChessPiece('a4')
            >>> piece.move('e5')
                False
        """

        if not self.is_legal_move(position):
            return False

        newmove = (self.prefix + self.position, self.prefix + position,
                   time.time())

        self.moves.append(newmove)
        self.position = position

        return newmove
