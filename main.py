board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

col = int(input('X player, select a column 1-3: '))
row = int(input('X player, select a row 1-3: '))
col -=1
row -=1


if board[row][col] == '-':
  board[row][col] = 'X'
else: 
  print('That spot is already taken')
  col = int(input('X player, select a column 1-3: '))
  row = int(input('X player, select a row 1-3: '))
  col -=1
  row -=1
print(board[0])
print(board[1])
print(board[2])

col = int(input('O player, select a column 1-3: '))
row = int(input('O player, select a column 1-3: '))
col -= 1
row -= 1

if board[row][col] == '-':
  board[row][col] = 'O'
else: 
  print ('That spot is already taken')
  col = int(input('O player, select a column 1-3: '))
  row = int(input('O player, select a column 1-3: '))
  col -= 1
  row -= 1
print(board[0])
print(board[1])
print(board[2])
