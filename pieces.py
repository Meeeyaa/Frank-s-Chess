from cmu_112_graphics import*

################################################################################

class Piece(object):

  def __init__(self, color, image, x, y):
    self.color = color
    self.image = image
    self.x = x
    self.y = y

  def get_color(self):
    return self.color 

  def get_row(self, app, y):
    return int((y - app.top_margin)/app.cell_height)
  
  def get_col(self, app, x):
    return int((x - app.side_margin)/app.cell_width)
  
  def get_x_coord(self, app, col):
    return (((app.cell_width)*(col)) + app.side_margin) + app.cell_width/2

  def get_y_coord(self, app, row):
    return (((app.cell_height)*(row)) + app.top_margin) + app.cell_height/2
  
  def draw(self, app, canvas):
    x = self.x
    y = self.y

    if (self.color == "black"):
      canvas.create_image(x, y, image=ImageTk.PhotoImage(self.image))
    else:
      canvas.create_image(x, y, image=ImageTk.PhotoImage(self.image))


###########################################

class Bishop(Piece):

  def is_valid_move(self, app, new_x, new_y):
    #bishop can move multiple sqaures diagonally
    #one up/down, one left/right

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)
    piece_row, piece_col = self.get_row(app, self.y), self.get_col(app, self.x)

    #check if is legal move for bishop and is row is within board bounds
    if (((piece_row - new_row) == 0 and abs(piece_col - new_col) <= 7)
        or (abs(piece_row - new_row) <= 7 and (piece_col - new_col) == 0)
        or (abs(piece_row - new_row) >= 2 and abs(piece_col - new_col) == 1) 
        or (abs(piece_row - new_row) == 1 and abs(piece_col - new_col) >= 2)
        or (new_row < 0 and new_row > 7 and new_col < 0 and new_col > 7)):
      return False
    
    else:
      return True 
  

###########################################

class King(Piece):
  def is_valid_move(self, app, new_x, new_y):
    #king can move one square in every direction

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)
    piece_row, piece_col = self.get_row(app, self.y), self.get_col(app, self.x)

    #check if is legal move for king and is row is within board bounds
    
    if ((abs(new_row - piece_row) == 1 and abs(new_col - piece_col) == 0) 
        or (abs(new_row - piece_row) == 0 and abs(new_col - piece_col) == 1)
        or (abs(new_row - piece_row) == 1 and abs(new_col - piece_col) == 1) 
        and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
      return True
    
    else:
      return False


###########################################

class Knight(Piece):
  def is_valid_move(self, app, new_x, new_y):
    #knight can only move two squares up, one square right or left

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)
    piece_row, piece_col = self.get_row(app, self.y), self.get_col(app, self.x)

    #check if is legal move for knight and is row is within board bounds
    if ((abs(new_row - piece_row) == 2 and abs(new_col - piece_col) == 1) 
        or (abs(new_row - piece_row) == 1 and abs(new_col - piece_col) == 2) 
        and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
      return True
    
    else:
      return False


###########################################

class Pawn(Piece):
  def __init__(self, color, image, move_count, x, y):
    self.color = color
    self.image = image
    self.move_count = move_count
    self.x = x
    self.y = y

  def is_stuck(self, app):
    for piece in app.board_pieces:
      guess_piece_row = piece.get_row(app, piece.y)
      guess_piece_col = piece.get_col(app, piece.x)

      if (self.color == "black"):
        if (((self.get_row(app, self.y) + 1) == guess_piece_row)
          and (self.get_col(app, self.x) - guess_piece_col == 0)):
          print(f'stuck!')   
          return True
      else:
        if (((self.get_row(app, self.y) - 1) == guess_piece_row)
          and (self.get_col(app, self.x) - guess_piece_col == 0)):
          print(f'stuck!')   
          return True
     
    return False
  

  def can_attack(self, app):
    potential_attacks = set()

    for piece in app.board_pieces:
      guess_piece_row = piece.get_row(app, piece.y)
      guess_piece_col = piece.get_col(app, piece.x)
      guess_color = piece.color

      if (self.color == "black"):
        if (guess_color == "white" and ((self.get_row(app, self.y) + 1) == guess_piece_row)
          and ((self.get_col(app, self.x) + 1 == guess_piece_col) 
               or (self.get_col(app, self.x) - 1 == guess_piece_col))):
          print(f'can attack at: {(1, guess_piece_col)}')
          potential_attacks.add(guess_piece_col)

      else:
        if (guess_color == "black" and ((self.get_row(app, self.y) - 1) == guess_piece_row)
          and ((self.get_col(app, self.x) + 1 == guess_piece_col)
               or (self.get_col(app, self.x) - 1 == guess_piece_col))):
          print(f'can attack at: {(1, guess_piece_col)}')
          potential_attacks.add(guess_piece_col)
        
    return potential_attacks




  def is_valid_move(self, app, new_x, new_y):
    #pawn can only move one square forward, or diagonally to attack

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)
    piece_row, piece_col = self.get_row(app, self.y), self.get_col(app, self.x)

    #check if is legal move for pawn and is row is within board bounds
    #check if there is piece in front

    potential_attacks = self.can_attack(app)

    if (self.color == "black"):
      
      if (len(potential_attacks) != 0):
        for opponent_col in potential_attacks:
          if (new_row - piece_row == 1 and new_col == opponent_col):
            return True
      
      if(app.en_passant_piece != app.null_piece):
        if (new_row - piece_row == 1 and new_col == app.en_passant_piece.get_col(app, app.en_passant_piece.x)):
          return True
      
      if (self.is_stuck(app)):
        return False
          
      else:
        if((new_row - piece_row == 1 and piece_col - new_col == 0) 
            and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
          print(f'is valid move')
          return True
        


    elif (self.color == "white"):

      if (len(potential_attacks) != 0):
        for opponent_col in potential_attacks:
          if (piece_row - new_row == 1 and new_col == opponent_col):
            return True
        
      if (self.is_stuck(app)):
        return False
      
      if (app.en_passant_piece != app.null_piece):
        if (piece_row - new_row == 1 and new_col == app.en_passant_piece.get_col(app, app.en_passant_piece.x)
            or (piece_row - new_row == 1 and piece_col - new_col == 0
            and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7)):
          return True 
        
      else:
        if((piece_row - new_row == 1 and piece_col - new_col == 0) 
            and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
          print(f'is valid move')
          return True
        


###########################################

class Queen(Piece):
  def is_valid_move(self, app, new_x, new_y):
    #queen can move multiple spaces in any direction

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)

    #only need to check if move is within board bounds
    if (new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
      return True
    
    else:
      return False



###########################################

class Rook(Piece):
  def is_valid_move(self, app, new_x, new_y):
    #rook can move multiple sqaures left/right or up/down

    new_row, new_col = self.get_row(app, new_y), self.get_col(app, new_x)
    piece_row, piece_col = self.get_row(app, self.y), self.get_col(app, self.x)

     #check if is legal move for rook and is row is within board bounds
    if (((piece_row - new_row) == 0 and abs(piece_col - new_col) <= 7)
        or (abs(piece_row - new_row) <= 7 and (piece_col - new_col) == 0)
        and new_row >= 0 and new_row <= 7 and new_col >= 0 and new_col <= 7):
      return True
    
    else:
      return False
  
  
