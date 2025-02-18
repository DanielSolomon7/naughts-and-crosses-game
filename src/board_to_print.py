def board_to_print(given_board):
   value = ""
   board = f"""   
 {given_board[0][0]} | {given_board[0][1]} | {given_board[0][2]} 
-----------
 {given_board[1][0]} | {given_board[1][1]} | {given_board[1][2]} 
-----------
 {given_board[2][0]} | {given_board[2][1]} | {given_board[2][2]} 
"""
   print(board)
   return board
