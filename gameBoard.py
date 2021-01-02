fill = "*"
noFill = " "
def buildFill():
  for row in range(1):
    for column in range(1,6):
      print(fill,end = "")
def buildNoFill():
  for row in range(1):
    for column in range(1,6):
      print(noFill,end = "")
def LastFill():
  for row in range(1):
    for column in range (1,6):
      if column == 5:
        print(fill)
      else:
        print(fill, end = "")
def LastNoFill():
  for row in range(1):
    for column in range (1,6):
      if column == 5:
        print(noFill)
      else:
        print(noFill, end = "")
        
        
def GameBoard(row,column):
  for rowout in range(row):
    for rowmid in range(1,3):
      for rowin in range(3):
        for columnout in range(column):
          for columnmid in range(1,3):
            for columnin in range(1,6):
              if columnout == column -1 and columnmid == 2 and columnin == 5:
                if rowmid == 1:
                  print(" ")
                else:
                  print(fill)
                continue
              if rowmid == columnmid:
                print(fill,end = "")
              else:
                print(" ",end = "")
  return True

GameBoard(4,4)
