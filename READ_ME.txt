___ Frank's Chess ___
Project started: 03/03/2023
Finished (not reaally): 03/10/2023

This is a simple implementation of a two-player chess game

**SCREEN IS NOT RESIZEABLE**, resizing disrupts proper game functionality due to
how I implemented the game (results in errors in button clicks and piece movement)

Otherwise, Frank's Chess follows the standard rules of chess:

Piece Movement Rules:
1. Bishop-- can only move diagonally
^^ bug with valid bishop movemnt-- bishops is allowed to move non-diagonally when
moving farther than two squares ^^
2. King-- can move one space in every direction
3. Knight-- can only move in 'L' shape (two spaces left/right, one space up/down)
4. Pawn-- moves one space forward, can move diagonally to take
5. Queen-- moves in any direction, any amount of spaces
6. Rook-- can only move left/right or up/direction


Other Rules:
--Castling--
7. If king has been moved or the rook attempting to be used for castling has been
moved, you can no longer castle.

--Pawn Promotion--
8. Once a Pawn has reached the back line of it's opponent's ranks, it can be
promoted to any other piece of the player's choosing.
^^ players will be prompted to select which piece they would like to promote their
pawn to in the terminal ^^

--En Passant--
9. In the case where two pawns are horizontally adjacent to one another, if the
attacking pawn has moved three squares forward and the pawn-to-be-taken has moved 
two squares forward, then the attacking pawn can move diagonally to take the other
pawn.
^^ for this rule, the current implementation is such that any opposing pawns
adjacent to each other that have travelled only three squares forward and two
squares foward, respectively, are permitted to do the en passant move
BUT: does this respect the fact that the en passant move must be done in the move
directly following when the pawn-to-be-taken has moved two squares up??? no :/ ^^

--Absolute Pin--
10. If a piece is protecting king from being checked, the piece cannot move in
such a way that puts the king in check.

--Relative Pin--
11.



franks rules the ranks



Source for Images Used:
https://dani-maccari.itch.io/pixel-chess
