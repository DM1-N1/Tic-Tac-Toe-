print("Welcome to tick tack toe")
print("Time to pick who will be player one and who will be player 2")
player1=input("Enter your name player1")
player2=input("Enter your name player2")
print(player1,"Your player1")
print(player2,"Your player2")
game=[["","",""],
["","",""],
["","",""]]
def tic(row,where,p):
  r=0
  w=0
  if row=="top":
    r=0
  elif row=="middle":
    r=1
  elif row=="bottom":
    r=2

  if where=="left":
    w=0
  elif where=="middle":
    w=1
  elif where=="right":
    w=2
  print(r,w)

  if game[r][w]=="":
    game[r][w]=p
    print(game)
  else:
    print("Already used")
  
  a=game[0][0]
  b=game[1][0]
  c=game[2][0]
  d=game[0][1]
  e=game[1][1]
  f=game[2][1]
  g=game[0][2]
  h=game[1][2]
  i=game[2][2]

  #Checks to see if p1 wins
  if a and b and c==1:
    print("You win")
    quit()
  elif d and e and f==1:
    print("You win")
    quit()
  elif g and h and i==1:
    print("You win")
    quit() 
  elif a and d and g==1:
    print("You win")
    quit()    
  elif b and e and h==1:
    print("You win")
    quit()    
  elif c and f and i==1:
    print("You win")
    quit()
  elif a and e and i==1:
    print("You win")
    quit()
  elif c and e and g==1:
    print("You win")
    quit()
  
  
  #Checks to see if p2 wins
  if a and b and c==2:
   print("You win")
   quit()
  elif d and e and f==2:
    print("You win")
    quit()
  elif g and h and i==2:
    print("You win")
    quit() 
  elif a and d and g==2:
    print("You win")
    quit()    
  elif b and e and h==2:
    print("You win")
    quit()    
  elif c and f and i==2:
    print("You win")
    quit()
  elif a and e and i==2:
    print("You win")
    quit()
  elif c and e and g==2:
    print("You win")
    quit()
  
  
for i in range(0,4):

  print("Player1s turn")
  p=1
  row=input("Which row would you like to enter in top middle or bottom")
  where=input("Where in that row would you like to place ur mark left middle or right")
  tic(row,where,p)

  print("Player2s turn")
  p=2
  row=input("Which row would you like to enter in top middle or bottom")
  where=input("Where in that row would you like to place ur mark left middle or right")
  tic(row,where,p)
  
  #final turn
print("Player1s turn")
p=1
row=input("Which row would you like to enter in top middle or bottom")
where=input("Where in that row would you like to place ur mark left middle or right")
tic(row,where,p) 

print("Tie")
