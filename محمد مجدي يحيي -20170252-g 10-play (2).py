board = [0,1,2,
     3,4,5,
     6,7,8]
boardLog = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

player = 'a' 

def tic_tac_toe ():
    print ('|' ,board[0],'|',board[1] ,'|', board[2],'|')
    print ('--------------------')
    print ('|' ,board[3],'|',board[4] ,'|', board[5],'|')
    print ('--------------------')
    print ('|' ,board[6],'|',board[7] ,'|', board[8],'|')

def move(x1,x2):
    board[x2] = x1
    boardLog[x2] = 1
    tic_tac_toe()

def odd (x, x2):
    while  (x%2!=0):
        x = int(input ('enter an even number'))
    
    move (x ,x2)      

def even (x ,x2) :
    while  (x%2==0):
        x = int(input ('enter an odd number'))
    
    move (x ,x2)        

def winner():
    if (boardLog[0] + boardLog[1] + boardLog[2] == 3):
      if (board[0]+board [1]+board[2]==15):
          print ('you are the winner')
          return True
    if (boardLog[0] + boardLog[3] + boardLog[6] == 3):
      if (board[0]+board [3]+board[6]==15):
          print ('you are the winner')
          return True
    if (boardLog[1] + boardLog[4] + boardLog[7] == 3):
      if (board[1]+board [4]+board[7]==15):
          print ('you are the winner')
          return True
    if (boardLog[3] + boardLog[4] + boardLog[5] == 3):
      if (board[3]+board [4]+board[5]==15):
          print ('you are the winner')
          return True
    if (boardLog[2] + boardLog[5] + boardLog[8] == 3):
      if (board[2]+board [5]+board[8]==15):
          print ('you are the winner')
          return True
    if (boardLog[6] + boardLog[7] + boardLog[8] == 3):
      if (board[6]+board [7]+board[8]==15):
          print ('you are the winner')
          return True

    else: return False

def turn(s):
    print ('its '+ s +' turn')
    x = int (input ('enter the number: '))
    x1 = int (input ('enter the places number: '))
    if x1==ValueError :
        print ("not number")
    if x1>8:
        print ("not in board")
    if x1<0 :
        print ("not in borad")
    if x==ValueError:
        print("try again")
    if player == 'a':
        even(x, x1)
    else: odd(x, x1)
    if boardLog[x1]==1:
        print ("try again")
        

print('Tic Tac Toe')
print ('player A should enter even numbers only'+' and player B should enter odd numbers only')
print ('the player with the ood numbers start')
tic_tac_toe ()
while (True):
    turn(player)
    if winner(): break
    else:
        if player == 'a': player = 'b'



