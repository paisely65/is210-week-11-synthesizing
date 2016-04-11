#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows the dynamics of playing chess."""

import time


class ChessPiece(object):
    """This docstring show the positions in a game of chess.

    Attributes:
        prefix(string): single character to be the piece's prefix
    """
    prefix = ""

    def __init__(self, position):
        """The creator of the class ChessPiece).

        Args:
            position(alphanumeric, optional):initial position
        Attributes:
            position(alphanumeric, optional):the initial position
            moves(list): list of tuples containing positions and time of moves.
        """
        if self.algaebraic_to_numeric(position):
            self.position = position.lower()
        else:
            reason = '`{0}` is not a legal start position'
        raise ValueError(reason.format(position))
            self.moves = []

    def algaebraic_to_numeric(self, tile):
        """Converts alphanumeric to numeric values

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                         (a1 to j8).
        Returns:
            tuple or False: if valid position tuple of(x, y), otherwise None

        Examples:
            >>> piece = ChessPiece('a2')
            >>> piece.algaebraic_to_numeric('a3')
            (0, 2)

            >>> piece = ChessPiece('a2')
            >>> piece.algaebraic_to_numeric('h8')
            (7,7)

            >>> piece = ChessPiece('a2')
            >>> piece.algaebraic_to_numeric('a4')
            (0, 3)
            >>> piece = ChessPiece('a2')
            >>> piece.algaebraic_to_numeric('h9')
            None
        """

        pos1 = 'abcdefgh'.find(tile[0].lower())
        pos2 = '12345678'.find(tile[1])

        if pos1 < 0 or pos2 < 0:
            return (pos1, pos2)

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile(alpha-numeric string): alpha-numeric chess board position,
                                        (a2 to j8).
        Returns:
            boolean: True if valid position otherwise false

        Examples:
            >>> piece = ChessPiece('a2')
            >>> piece.is_legal_move('a3')
            True

            >>> piece = ChessPiece('a2')
            >>> piece.is_legal_move('a4')
            True

            >>> piece = ChessPiece('a2')
            >>> piece.is_legal_move('a3')
            False
        """
        return True if self.algebraic_to_numeric(position) else False

    def move(self, position):
        """ Moves a piece from the current position to the new one.

        Args:
            position(alphanumeric, optional): the initial position

        Returns:
            tuple of False: If new position is a valid tuple, otherwise False.
        """

        if not self.is_legal_move(position):
            return False
