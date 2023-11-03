map = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

game = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""]
]

positions = [
  None,
  (0, 0),
  (0, 1),
  (0, 2),
  (1, 0),
  (1, 1),
  (1, 2),
  (2, 0),
  (2, 1),
  (2, 2)
]

wins = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9],
  [1, 5, 9],
  [3, 5, 7]
]

def toDesign(matrix):
  design = ""
  divider = "{0}{1}{0}{1}{0}".format("---", "+")
  for i in range(3):
    line = ""
    for j in range(3):
      line += f"{matrix[i][j]:^3}"
      if (j <= 1):
        line += "|"
    design += line + "\n"
    if (i <= 1):
     design += divider + "\n"
  return design

def update():
  return "\n> Jogo Atual:\n\n" + toDesign(game)

def toMark(player, position):
  game[positions[position][0]][positions[position][1]] = player
  return update()

print("> Mapa do jogo:\n\n" + toDesign(map))   
print(update())

count = 1
while (count <= 9):
  if (count == 9):
    print("Deu velha!")
    break
  elif (count % 2 != 0):
    X = int(input("X - marque uma posição (1-9): "))
    if (X < 1 or X > 9):
      print("Essa posição não existe!")
      continue
    elif (game[positions[X][0]][positions[X][1]] != ""):
      print("Posição ocupada!")
      continue
    else:
      print(toMark("X", X))
      for v in wins:
        for i in v:
          if game[positions[i][0]][positions[i][1]] != "X":
            break
        else:
          print(f"O player 'X' ganhou!")
          count = 9 + 1
  else:
    O = int(input("O - marque uma posição (1-9): "))
    if (O < 1 or O > 9):
      print("Essa posição não existe!")
      continue
    elif (game[positions[O][0]][positions[O][1]] != ""):
      print("Posição ocupada!")
      continue
    else:
      print(toMark("O", O))
      for v in wins:
        for i in v:
          if game[positions[i][0]][positions[i][1]] != "O":
            break
        else:
          print(f"O player 'O' ganhou!")
          count = 9 + 1
  count += 1