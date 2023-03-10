from cmu_112_graphics import*
from pieces import*
from check import*

###############################################################################

################# MODEL FUNCTIONS ########################

def appStarted(app):
  #screens
  app.mode = "start"


  #image for board
  app.board = app.scaleImage(app.loadImage("board_plain_03.png"), app.width/200)


  #dimensions for "invisible" grid:
  #margins are 232 --> calculation: app.width/x = 232, x = ? 
  #not completely accurate calculation for needs, off by 1 or 2
  app.side_margin = app.width/5.6    
  app.top_margin = app.height/5.6    

  app.cell_width = (app.width - 2*app.side_margin)/8
  app.cell_height = (app.height - 2*app.top_margin)/8




  #images for black pieces:
  app.b_bishop = app.scaleImage(app.loadImage("B_Bishop.png"), app.width/400)
  app.b_king = app.scaleImage(app.loadImage("B_King.png"), app.width/400)
  app.b_knight = app.scaleImage(app.loadImage("B_Knight.png"), app.width/400)
  app.b_pawn = app.scaleImage(app.loadImage("B_Pawn.png"), app.width/400)
  app.b_queen = app.scaleImage(app.loadImage("B_Queen.png"), app.width/400)
  app.b_rook = app.scaleImage(app.loadImage("B_Rook.png"), app.width/400)
  app.null_piece = app.loadImage("BlackPieces-Sheet.png")



  #images for white pieces:
  app.w_bishop = app.scaleImage(app.loadImage("W_Bishop.png"), app.width/400)
  app.w_king = app.scaleImage(app.loadImage("W_King.png"), app.width/400)
  app.w_knight = app.scaleImage(app.loadImage("W_Knight.png"), app.width/400)
  app.w_pawn = app.scaleImage(app.loadImage("W_Pawn.png"), app.width/400)
  app.w_queen = app.scaleImage(app.loadImage("W_Queen.png"), app.width/400)
  app.w_rook = app.scaleImage(app.loadImage("W_Rook.png"), app.width/400)


  #initializations of all 64 pieces, order from top left to bottom right

  #black back line
  app.b_rook_1 = Rook("black", app.b_rook, (((app.cell_width)*(0)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_knight_1 = Knight("black", app.b_knight, (((app.cell_width)*(1)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_bishop_1 = Bishop("black", app.b_bishop, (((app.cell_width)*(2)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_queen_0 = Queen("black", app.b_queen, (((app.cell_width)*(3)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_king_0 = King("black", app.b_king, (((app.cell_width)*(4)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_bishop_2 = Bishop("black", app.b_bishop, (((app.cell_width)*(5)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_knight_2 = Knight("black", app.b_knight, (((app.cell_width)*(6)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  app.b_rook_2 = Rook("black", app.b_rook, (((app.cell_width)*(7)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2)
  

  #black front line
  app.b_pawn_1 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(0)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_2 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(1)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_3 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(2)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_4 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(3)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_5 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(4)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_6 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(5)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_7 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(6)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)
  app.b_pawn_8 = Pawn("black", app.b_pawn, 0, (((app.cell_width)*(7)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(1)) + app.top_margin) + app.cell_height/2)


  #white front line
  app.w_pawn_1 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(0)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_2 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(1)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_3 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(2)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_4 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(3)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_5 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(4)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_6 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(5)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_7 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(6)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)
  app.w_pawn_8 = Pawn("white", app.w_pawn, 0, (((app.cell_width)*(7)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(6)) + app.top_margin) + app.cell_height/2)


  #white back line
  app.w_rook_1 = Rook("white", app.w_rook, (((app.cell_width)*(0)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_knight_1 = Knight("white", app.w_knight, (((app.cell_width)*(1)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_bishop_1 = Bishop("white", app.w_bishop, (((app.cell_width)*(2)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_queen_0 = Queen("white",app.w_queen, (((app.cell_width)*(3)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_king_0 = King("white", app.w_king, (((app.cell_width)*(4)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_bishop_2 = Bishop("white", app.w_bishop, (((app.cell_width)*(5)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_knight_2 = Knight("white", app.w_knight, (((app.cell_width)*(6)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)
  app.w_rook_2 = Rook("white", app.w_rook, (((app.cell_width)*(7)) + app.side_margin) + app.cell_width/2, (((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2)


  app.null_piece = Pawn("black", app.null_piece, 0, 0, 0)


  
  app.board_pieces = [app.b_rook_1, app.b_knight_1, app.b_bishop_1, app.b_queen_0,
                      app.b_king_0, app.b_bishop_2, app.b_knight_2, app.b_rook_2,
                      app.b_pawn_1, app.b_pawn_2, app.b_pawn_3, app.b_pawn_4,
                      app.b_pawn_5, app.b_pawn_6, app.b_pawn_7, app.b_pawn_8,
                      app.w_rook_1, app.w_knight_1, app.w_bishop_1, app.w_queen_0,
                      app.w_king_0, app.w_bishop_2, app.w_knight_2, app.w_rook_2,
                      app.w_pawn_1, app.w_pawn_2, app.w_pawn_3, app.w_pawn_4,
                      app.w_pawn_5, app.w_pawn_6, app.w_pawn_7, app.w_pawn_8]
  
  app.b_taken_pieces = []
  app.w_taken_pieces = []


  app.pawns = [app.b_pawn_1, app.b_pawn_2, app.b_pawn_3, app.b_pawn_4,
               app.b_pawn_5, app.b_pawn_6, app.b_pawn_7, app.b_pawn_8,
               app.w_pawn_1, app.w_pawn_2, app.w_pawn_3, app.w_pawn_4,
               app.w_pawn_5, app.w_pawn_6, app.w_pawn_7, app.w_pawn_8]


  #movement flags
  app.mouse_select = True
  app.mouse_place = False
  app.piece_found = False
  app.invalid_move = False

  app.selected_piece = app.null_piece

  app.mouse_x = 0
  app.mouse_y = 0

  app.player_turn = True
  app.player_turn_error = False


  #castling check
  app.cannot_castle = set()
  app.can_castle = True


  #en passant check
  app.can_en_passant = False
  app.en_passant_piece = app.null_piece


  #checking check



  #game over/checkmate check
  #use recursive backtracking? --> maybe not idk



  #game over
  app.game_over = False



########################## START SCREEN ##################################


def start_mousePressed(app, event):
  #pressing start button
  if (app.width*(1/8) <= event.x <= app.width*(3/8)
      and app.width*(3/4) <= event.y <= app.height - app.top_margin):
    app.mode = "game"


  #pressing help button
  elif (app.width*(5/8) <= event.x <= app.width*(7/8)
      and app.width*(3/8) <= event.y <= app.height - app.top_margin):
    app.mode = "help"




################# START VIEW HELPER FUNCTION ########################

def drawHelpButton(app, canvas):
  #button
  canvas.create_rectangle(app.width*(5/8), app.height*(3/4),
                          app.width*(7/8), app.height - app.top_margin,
                          fill = "white")

  #text
  canvas.create_text((app.width*(7/8) + app.width*(5/8))/2,
                     (app.height - app.top_margin + app.height*(3/4))/2,
                     text = "HELP", fill = "black", font = f"System 18 bold")


def drawStartButton(app, canvas):
  #button
  canvas.create_rectangle(app.width*(1/8), app.height*(3/4),
                          app.width*(3/8), app.height - app.top_margin,
                          fill = "white")

  #text
  canvas.create_text((app.width*(3/8) + app.width*(1/8))/2,
                     (app.height - app.top_margin + app.height*(3/4))/2,
                     text = "START", fill = "black", font = f"System 18 bold")


def drawTitle(app, canvas):
  canvas.create_text(app.width/2, app.height/3, text = "Frank's Chess",
                     fill = "black", font = f"System 48 bold")



def drawBackground(app, canvas):
  canvas.create_rectangle(0, 0, app.width, app.height, fill = "light slate grey")




################# START VIEW FUNCTION ########################

def start_redrawAll(app, canvas):

  #draw background color
  drawBackground(app, canvas) 
      
  #drawing title
  drawTitle(app, canvas)

  #draw star button
  drawStartButton(app, canvas)

  #draw help/instructions button
  drawHelpButton(app, canvas)



################# HELP CONTROLLER FUNCTIONS ########################

def help_mousePressed(app, event):
  #pressing back button
  if (app.width*(2/8) <= event.x <= app.width*(6/8)
      and app.width*(3/4) <= event.y <= app.height - app.top_margin):
    app.mode = "start"




################# HELP VIEW HELPER FUNCTIONS ########################

def drawText(app, canvas):
  canvas.create_text((app.width*(6/8) + app.width*(2/8))/2,
                     app.height/2,
                     text = "CHESS! CHESS CHES?? CHESS....", 
                     fill = "black", font = f"System 18 bold")



def drawBackButton(app, canvas):
  #button
  canvas.create_rectangle(app.width*(2/8), app.height*(3/4),
                          app.width*(6/8), app.height - app.top_margin,
                          fill = "white")

  #text
  canvas.create_text((app.width*(6/8) + app.width*(2/8))/2,
                     (app.height - app.top_margin + app.height*(3/4))/2,
                     text = "RETURN TO START", 
                     fill = "black", font = f"System 18 bold")




################# HELP VIEW FUNCTION ########################

def help_redrawAll(app, canvas):

  #draw background color
  drawBackground(app, canvas) 

  #draw text
  drawText(app, canvas)

  #draw back button
  drawBackButton(app, canvas)




######################## GAME MODEL FUNCTIONS #############################

def restartApp(app):
  appStarted(app)




################# GAME CONTROLLER HELPER FUNCTIONS ########################

def removePiece(app):
  #remove taken piece from list of playable pieces

  for piece in app.board_pieces:
    opponent_piece_row = piece.get_row(app, piece.y)
    opponent_piece_col = piece.get_col(app, piece.x)
    opponent_color = piece.color

    piece_row = app.selected_piece.get_row(app, app.selected_piece.y)
    piece_col = app.selected_piece.get_col(app, app.selected_piece.x)

    if (piece_row == opponent_piece_row and piece_col == opponent_piece_col 
        and opponent_color != app.selected_piece.color):
        
      if (opponent_color == "black"):
        app.w_taken_pieces.append(piece)
        app.board_pieces.remove(piece)
      else:
        app.b_taken_pieces.append(piece)
        app.board_pieces.remove(piece)
  
    
    elif (abs(piece_row - opponent_piece_row) == 1 and piece_col == opponent_piece_col 
        and opponent_color != app.selected_piece.color):
      if (app.en_passant_piece != app.null_piece):
        
        if (opponent_color == "black"):
          app.w_taken_pieces.append(piece)
          app.board_pieces.remove(piece)
        else:
          app.b_taken_pieces.append(piece)
          app.board_pieces.remove(piece)



def selectPiece(app, color, mouse_x, mouse_y):
  #find which piece has been clicked on to move

  mouse_row, mouse_col = getCell(app, mouse_x, mouse_y)
  for piece in app.board_pieces:
    guess_piece_row = piece.get_row(app, piece.y)
    guess_piece_col = piece.get_col(app, piece.x)
    guess_color = piece.color

    if ((mouse_row == guess_piece_row) and (mouse_col == guess_piece_col)
        and color == guess_color):
      app.piece_found = True
      return piece
    
  app.piece_found = False

  return app.null_piece


def isSquareTaken(app):
  #find whether the square hat has been clicked on is already occupied

  mouse_row, mouse_col = getCell(app, app.mouse_x, app.mouse_y)

  for piece in app.board_pieces:
    guess_piece_row = piece.get_row(app, piece.y)
    guess_piece_col = piece.get_col(app, piece.x)
    guess_color = piece.color

    piece_color = app.selected_piece.color

    if (mouse_row == guess_piece_row
        and mouse_col == guess_piece_col
        and guess_color == piece_color):
      return True
  
  return False


def pieceBetween(app):
  #find whether there are any pieces btwn select piece location and location
  #attempting to place at

  mouse_row, mouse_col = getCell(app, app.mouse_x, app.mouse_y)

  if (mouse_col < app.selected_piece.get_col(app, app.selected_piece.x)):
    for piece in app.board_pieces:
      guess_piece_row = piece.get_row(app, piece.y)
      guess_piece_col = piece.get_col(app, piece.x)

      if (mouse_row == guess_piece_row
          and mouse_col < guess_piece_col < app.selected_piece.get_col(app, app.selected_piece.x)):
        return True
  
  elif (mouse_col > app.selected_piece.get_col(app, app.selected_piece.x)):
    for piece in app.board_pieces:
      guess_piece_row = piece.get_row(app, piece.y)
      guess_piece_col = piece.get_col(app, piece.x)

      if (mouse_row == guess_piece_row
          and mouse_col > guess_piece_col > app.selected_piece.get_col(app, app.selected_piece.x)):
        return True
  
  return False


# In the case where two pawns are horizontally adjacent to one another, if the
# attacking pawn has moved three squares forward and the pawn to be taken has moved 
# two squares forward, then the attacking pawn can move diagonally to take the other
# pawn.
def enPassant(app):
  for pawn_1 in app.pawns:
    for pawn_2 in app.pawns:

      #if pawns are adjacent
      if (pawn_1.color != pawn_2.color and pawn_1.get_row(app, pawn_1.y) == pawn_2.get_row(app, pawn_2.y)
          and abs(pawn_1.get_col(app, pawn_1.x) - pawn_2.get_col(app, pawn_2.x)) == 1):
        #if attacking pawn has moved three squares
        #and taken pawn has moved two squares

        if (pawn_1.move_count == 3 and pawn_2.move_count == 2):
          app.en_passant_piece = pawn_2
          return True

        elif(pawn_2.move_count == 3 and pawn_1.move_count == 2):
          app.en_passant_piece = pawn_1
          return True

  app.en_passant_piece = app.null_piece      
  return False




################# GAME CONTROLLER FUNCTIONS ########################

def game_keyPressed(app, event):
  if (event.key == "r" or event.key == "R"): 
    restartApp(app)


def game_timerFired(app):
  enPassant(app)
  tempCheck(app)


def get_x_coord(app, col):
    return (((app.cell_width)*(col)) + app.side_margin) + app.cell_width/2


def get_y_coord(app, row):
  return (((app.cell_height)*(row)) + app.top_margin) + app.cell_height/2


def getCell(app, x, y):
  col = int((x - app.side_margin)/app.cell_width)
  row = int((y - app.top_margin)/app.cell_height)
  return (row, col)


def game_mousePressed(app, event):

  if (not app.game_over):
  
    if (app.mouse_select and not app.mouse_place):
      app.invalid_move = False
      app.can_castle = True

      #find piece player wants to move
      if (app.player_turn):
        print(f'white turn: {app.player_turn}')
        app.selected_piece = selectPiece(app, "white", event.x, event.y)
        print(f'white piece selected = {app.piece_found}')
        if (app.piece_found):
          app.mouse_select = False
          app.mouse_place = True
          app.player_turn_error = False
        else:
          app.player_turn_error = True
      
      else:
        print(f'black turn: {app.player_turn}')
        app.selected_piece = selectPiece(app, "black", event.x, event.y)
        print(f'black piece selected = {app.piece_found}')
        if (app.piece_found):
          app.mouse_select = False
          app.mouse_place = True
          app.player_turn_error = False
        else:
          app.player_turn_error = True


    elif (app.mouse_place and not app.mouse_select):
      #place down piece in new square
      app.mouse_x = event.x
      app.mouse_y = event.y

      if (app.selected_piece.is_valid_move(app, app.mouse_x, app.mouse_y)
            and not isSquareTaken(app)
            and not (app.selected_piece.image == app.w_pawn or app.selected_piece.image == app.b_pawn)):
        
        app.invalid_move = False
        new_row, new_col = getCell(app, app.mouse_x, app.mouse_y)
        app.selected_piece.x = app.selected_piece.get_x_coord(app, new_col)
        app.selected_piece.y = app.selected_piece.get_y_coord(app, new_row)
        app.player_turn = not app.player_turn
        app.mouse_place = False
        app.mouse_select = True
        removePiece(app)

      elif (app.selected_piece.is_valid_move(app, app.mouse_x, app.mouse_y)
            and not isSquareTaken(app)
            and (app.selected_piece.image == app.w_pawn or app.selected_piece.image == app.b_pawn)):
          
        mouse_row, mouse_col = getCell(app, app.mouse_x, app.mouse_y)

        print(f'mouse_row = {mouse_row}')

        mouse_x = get_x_coord(app, mouse_col)
        mouse_y = get_y_coord(app, mouse_row)

        if (app.selected_piece.color == "white" and mouse_row == 0):

          w_new_piece = input("Pawn Promotion! What piece do you want: ")

          if (w_new_piece == "frank"):
            app.w_pawn_9 = Queen("white", app.w_pawn, mouse_x, mouse_y)
            app.board_pieces.append(app.w_pawn_9)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
        
          elif (w_new_piece == "rook"):
            app.w_rook_3 = Rook("white", app.w_rook, mouse_x, mouse_y)
            app.board_pieces.append(app.w_rook_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
          
          elif (w_new_piece == "knight"):
            app.w_knight_3 = Knight("white", app.w_knight, mouse_x, mouse_y)
            app.board_pieces.append(app.w_knight_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
            
          elif (w_new_piece == "bishop"):
            app.w_bishop_3 = Bishop("white", app.w_bishop, mouse_x, mouse_y)
            app.board_pieces.append(app.w_bishop_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
            
          elif (w_new_piece == "queen"):
            app.w_queen_1 = Queen("white",app.w_queen, mouse_x, mouse_y)
            app.board_pieces.append(app.w_queen_1)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn

          elif (w_new_piece == "king"):
            app.w_king_1 = King("white", app.w_king, mouse_x, mouse_y)
            app.board_pieces.append(app.w_king_1)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn


        elif(app.selected_piece.color == "black" and mouse_row == 7):

          b_new_piece = input("Pawn Promotion! What piece do you want: ")
          
          if (b_new_piece == "frank"):
            app.b_pawn_9 = Queen("black", app.b_pawn, mouse_x, mouse_y)
            app.board_pieces.append(app.b_pawn_9)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
        
          elif (b_new_piece == "rook"):
            app.b_rook_3 = Rook("black", app.b_rook, mouse_x, mouse_y)
            app.board_pieces.append(app.b_rook_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
          
          elif (b_new_piece == "knight"):
            app.b_knight_3 = Knight("black", app.b_knight, mouse_x, mouse_y)
            app.board_pieces.append(app.b_knight_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
            
          elif (b_new_piece == "bishop"):
            app.b_bishop_3 = Bishop("black", app.b_bishop, mouse_x, mouse_y)
            app.board_pieces.append(app.b_bishop_3)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
            
          elif (b_new_piece == "queen"):
            app.b_queen_1 = Queen("black",app.b_queen, mouse_x, mouse_y)
            app.board_pieces.append(app.b_queen_1)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn

          elif (b_new_piece == "king"):
            app.b_king_1 = King("white", app.b_king, mouse_x, mouse_y)
            app.board_pieces.append(app.b_king_1)
            app.selected_piece.move_count += 1
            app.board_pieces.remove(app.selected_piece)
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
          

        else:
          app.invalid_move = False
          new_row, new_col = getCell(app, app.mouse_x, app.mouse_y)
          app.selected_piece.x = app.selected_piece.get_x_coord(app, new_col)
          app.selected_piece.y = app.selected_piece.get_y_coord(app, new_row)
          app.selected_piece.move_count += 1
          app.player_turn = not app.player_turn
          app.mouse_place = False
          app.mouse_select = True
          removePiece(app)
            

      elif(not app.selected_piece.is_valid_move(app, app.mouse_x, app.mouse_y)
          or isSquareTaken(app)):
        
        if (app.selected_piece == app.w_king_0):
          mouse_row, mouse_col = getCell(app, app.mouse_x, app.mouse_y)
          rook_1_row = app.w_rook_1.get_row(app, app.w_rook_1.y)
          rook_1_col = app.w_rook_1.get_col(app, app.w_rook_1.x)
          rook_2_row = app.w_rook_2.get_row(app, app.w_rook_2.y)
          rook_2_col = app.w_rook_2.get_col(app, app.w_rook_2.x)

          print(f"piece btwn: {pieceBetween(app)}")

          if((not pieceBetween(app)) and (app.w_rook_1 not in app.cannot_castle
                                      and app.w_king_0 not in app.cannot_castle)
            and (mouse_row == rook_1_row and mouse_col == rook_1_col)):
            #castle -- king moves two spaces to the left, rook moves to the spot
            #one col right of the king

            app.can_castle = True

            curr_col = app.selected_piece.get_col(app, app.selected_piece.x)
            app.selected_piece.x = app.selected_piece.get_x_coord(app, curr_col - 2)

            new_rook_col = app.selected_piece.get_col(app, app.selected_piece.x) + 1
            app.w_rook_1.x = app.w_rook_1.get_x_coord(app, new_rook_col)
            app.cannot_castle.add(app.selected_piece)
            app.cannot_castle.add(app.w_rook_1)
            print("castled white king w/ rook 1")
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
          
          elif((not pieceBetween(app)) and (app.w_rook_2 not in app.cannot_castle
                                        and app.w_king_0 not in app.cannot_castle)
              and (mouse_row == rook_2_row and mouse_col == rook_2_col)):
            #castle -- king moves two spaces right, rook moves to the spot on the
            #one col left of the king

            app.can_castle = True

            curr_col = app.selected_piece.get_col(app, app.selected_piece.x)
            app.selected_piece.x = app.selected_piece.get_x_coord(app, curr_col + 2)

            new_rook_col = app.selected_piece.get_col(app, app.selected_piece.x) - 1
            app.w_rook_2.x = app.w_rook_2.get_x_coord(app, new_rook_col)
            app.cannot_castle.add(app.selected_piece)
            app.cannot_castle.add(app.w_rook_2)
            print("castled white king w/ rook 2")
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn
          
          else:
            
            if (not (mouse_row == rook_1_row and mouse_col == rook_1_col
                    or (mouse_row == rook_2_row and mouse_col == rook_2_col))):
              app.invalid_move = False
              app.can_castle = True
              app.mouse_select = True
              app.mouse_place = False
            else:
              print(f'cannot castle')
              app.can_castle = False
              app.invalid_move = False
              app.mouse_select = True
              app.mouse_place = False

            
        elif (app.selected_piece == app.b_king_0):
          mouse_row, mouse_col = getCell(app, app.mouse_x, app.mouse_y)
          rook_1_row = app.b_rook_1.get_row(app, app.b_rook_1.y)
          rook_1_col = app.b_rook_1.get_col(app, app.b_rook_1.x)
          rook_2_row = app.b_rook_2.get_row(app, app.b_rook_2.y)
          rook_2_col = app.b_rook_2.get_col(app, app.b_rook_2.x)

          if((not pieceBetween(app)) and (app.b_rook_1 not in app.cannot_castle
                                      and app.b_king_0 not in app.cannot_castle)
            and (mouse_row == rook_1_row and mouse_col == rook_1_col)):
            #castle -- king moves two spaces to the left, rook moves to the spot
            #one col right of the king

            app.can_castle = True

            curr_col = app.selected_piece.get_col(app, app.selected_piece.x)
            app.selected_piece.x = app.selected_piece.get_x_coord(app, curr_col - 2)

            new_rook_col = app.selected_piece.get_col(app, app.selected_piece.x) + 1
            app.b_rook_1.x = app.b_rook_1.get_x_coord(app, new_rook_col)
            app.cannot_castle.add(app.selected_piece)
            app.cannot_castle.add(app.b_rook_1)
            print("castled black king w/ rook 1")
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn

          elif((not pieceBetween(app)) and (app.b_rook_2 not in app.cannot_castle
                                        and app.b_king_0 not in app.cannot_castle)
              and (mouse_row == rook_2_row and mouse_col == rook_2_col)):
            #castle -- king moves two spaces right, rook moves to the spot on the
            #one col left of the king

            app.can_castle = True

            curr_col = app.selected_piece.get_col(app, app.selected_piece.x)
            app.selected_piece.x = app.selected_piece.get_x_coord(app, curr_col + 2)

            new_rook_col = app.selected_piece.get_col(app, app.selected_piece.x) - 1
            app.b_rook_2.x = app.b_rook_2.get_x_coord(app, new_rook_col)
            app.cannot_castle.add(app.selected_piece)
            app.cannot_castle.add(app.b_rook_2)
            print("castled black king w/ rook 2")
            app.mouse_select = True
            app.mouse_place = False
            app.player_turn = not app.player_turn

          else:
            
            if (not (mouse_row == rook_1_row and mouse_col == rook_1_col
                    or mouse_row == rook_2_row and mouse_col == rook_2_col)):
              app.invalid_move = False 
              app.can_castle = True
              app.mouse_select = True
              app.mouse_place = False
            else:
              print(f'cannot castle')
              app.can_castle = False
              app.invalid_move = False
              app.mouse_select = True
              app.mouse_place = False

      else:
        app.invalid_move = True
        #print("invalid move")
        app.mouse_select = True
        app.mouse_place = False
        print(f'placing piece, invalid move? : {app.invalid_move}')
    




################# GAME VIEW HELPER FUNCTIONS ########################
 
def drawGrid(app, canvas):
  for i in range(0, 8):
    for j in range(0, 8):
      canvas.create_rectangle((app.cell_width*j) + app.side_margin,
                              (app.cell_height*i) + app.top_margin,
                              app.cell_width*(j+1) + app.side_margin,
                              app.cell_height*(i+1) + app.top_margin,
                              fill = "white", width = 2)
      

def drawBoard(app, canvas):
  canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.board))


def drawPlayingPieces(app, canvas):
  for piece in app.board_pieces:
    piece.draw(app, canvas)


def drawPlayerTurn(app, canvas):
  if (app.player_turn):
    canvas.create_text((((app.cell_width)*(7)) + app.side_margin) + app.cell_width/2,
                       ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.8,
                       text = "Player One Turn...", fill = "white", font = "System 16 bold")

  else:
    canvas.create_text((((app.cell_width)*(0)) + app.side_margin) + app.cell_width/2,
                       ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.8,
                       text = "Player Two Turn...", fill = "white", font = "System 16 bold")
    

def errorMessages(app, canvas):
  if (app.invalid_move):
    canvas.create_text(app.cell_width*(6),
                      ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.25,
                      text = "Invalid Move!", fill = "white", font = f"System 18 bold")
    canvas.create_text(app.cell_width*(6),
                      ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.25,
                      text = "Try Again...", fill = "white", font = f"System 18 bold")
    
  if (app.player_turn_error):
    if(app.player_turn):
      canvas.create_text(app.cell_width*(6),
                        ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.25,
                        text = "Player One Turn!", fill = "white", font = f"System 18 bold")
    else:
      canvas.create_text(app.cell_width*(6),
                        ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.25,
                        text = "Player Two Turn!", fill = "white", font = f"System 18 bold")

  if (not app.can_castle):
    canvas.create_text(app.cell_width*(6),
                      ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.25,
                      text = "Cannot Castle!", fill = "white", font = f"System 18 bold")
  
  if (app.en_passant_piece != app.null_piece):
    if (app.player_turn and app.en_passant_piece.color == "black"):
      canvas.create_text(app.cell_width*(6),
                        ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.25,
                        text = "En Passant Possible", fill = "white", font = f"System 18 bold")
    
    elif (not app.player_turn and app.en_passant_piece.color == "white"):
      canvas.create_text(app.cell_width*(6),
                        ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.25,
                        text = "En Passant Possible", fill = "white", font = f"System 18 bold")



def drawTakenPieces(app, canvas):
  for i in range(0, len(app.b_taken_pieces)):
    canvas.create_image((((app.cell_width)*((7) - i/2)) + app.side_margin) + app.cell_width/2,
                        ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.5,
                        image=ImageTk.PhotoImage(app.b_taken_pieces[i].image))
    
  for i in range(0, len(app.w_taken_pieces)):
    canvas.create_image((((app.cell_width)*(i/2)) + app.side_margin) + app.cell_width/2,
                        ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.9,
                        image=ImageTk.PhotoImage(app.w_taken_pieces[i].image))
    

def drawGameOver(app, canvas):
  canvas.create_text(app.cell_width*(6),
                        ((((app.cell_height)*(0)) + app.top_margin) + app.cell_height/2) - app.top_margin/1.25,
                        text = "Game Over!", fill = "black", font = f"System 48 bold")
  if (app.player_turn):
    canvas.create_text(app.cell_width*(6),
                          ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.8,
                          text = "Black Wins", fill = "black", font = f"System 48 bold")
  else:
    canvas.create_text(app.cell_width*(6),
                          ((((app.cell_height)*(7)) + app.top_margin) + app.cell_height/2) + app.top_margin/1.8,
                          text = "White Wins", fill = "black", font = f"System 48 bold")


################# GAME VIEW FUNCTION ########################

def game_redrawAll(app, canvas):

  #draw background color
  drawBackground(app, canvas)

  #draw "invisible" grid
  drawGrid(app, canvas) 
      
  #drawing board
  drawBoard(app, canvas)

  #place pieces
  drawPlayingPieces(app, canvas)

  #draw taken pieces
  drawTakenPieces(app, canvas)

  if (app.game_over):
    #game over label
    drawGameOver(app, canvas)
  
  else:
    #draw turn labels
    drawPlayerTurn(app, canvas)

    #draw error messages
    errorMessages(app, canvas)




runApp(width = 800, height = 800)