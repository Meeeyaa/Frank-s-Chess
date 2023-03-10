from cmu_112_graphics import*
from pieces import*

################################################################################

#check whether either king is being threated:
#loop through all pieces on the board, for each piece check whether it can attack
#king from all possible directions

# def get_x_coord(app, col):
#     return (((app.cell_width)*(col)) + app.side_margin) + app.cell_width/2

# def get_y_coord(app, row):
#   return (((app.cell_height)*(row)) + app.top_margin) + app.cell_height/2

# directions = {(0, -1), (0, 1),
#               (-1, 0), (1, 0), 
#               (-1, -1), (-1, 1), 
#               (1, -1), (1, 1)}

# def checkingByBishop(app):
#   for direction in directions:
#     dir_row, dir_col = direction

#     dir_x = get_x_coord(app, dir_col)
#     dir_y = get_y_coord(app, dir_row)

#     app.b_bishop_1.is_valid_move(app, dir_x, dir_y)



# def checkingByKing(app):

# def checkingByKnight(app):

# def checkingByPawn(app):

# def checkingByQueen(app):

# def checkingByRook(app):


# def check(app):
#   if(app.b_king_0):
#     if(checkingByBishop(app) or checkingByKing or checkingByKnight(app)
#        or checkingByPawn or checkingByQueen(app) or checkingByRook(app)):
#       return True
  
#   elif(app.w_king_0):
#     if(checkingByBishop(app) or checkingByKing or checkingByKnight(app)
#        or checkingByPawn or checkingByQueen(app) or checkingByRook(app)):
#       return True
  
#   else:
#     return False





#temporary check:
def tempCheck(app):
  if(app.b_king_0 in app.w_taken_pieces or app.w_king_0 in app.b_taken_pieces):
    app.game_over = True
  else:
    app.game_over = False