map = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game = [["", "", ""], ["", "", ""], ["", "", ""]]
positions = [None, (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def toDesign(matrix):
  design = ""
  divider = "{0}{1}{0}{1}{0}".format("---", "+")
  for i in range(3):
    line = ""
    for j in range(3):
      line += f"{matrix[i][j]:^3}"
      if (j <= 1):
        line += "|"
    design += f"{line}\n"
    if (i <= 1):
     design += f"{divider}\n"
  return design

def update():
  return f"\n> Jogo Atual:\n\n{toDesign(game)}"

def toMark(player, position):
  game[positions[position][0]][positions[position][1]] = player
  return update()

print(f"> Mapa do jogo:\n\n{toDesign(map)}")   
print(update())

n = 1
while (n <= 9):
  if (n == 9):
    print("Deu velha!")
    break
  elif (n % 2 != 0):
    x = int(input("Marque uma posição (X): "))
    if (x < 1 or x > 9):
      print("Essa posição não existe!")
      continue
    elif (game[positions[x][0]][positions[x][1]] == ""):
      print(toMark("X", x))
      for i in wins:
        for j in i:
          if game[positions[j][0]][positions[j][1]] != "X":
            break
        else:
          print(f"O player 'X' ganhou!")
          n = 9 + 1
    else:
      print("Posição ocupada!")
      continue
  else:
    o = int(input("Marque uma posição (O): "))
    if (o < 1 or o > 9):
      print("Essa posição não existe!")
      continue
    elif (game[positions[o][0]][positions[o][1]] == ""):
      print(toMark("O", o))
      for i in wins:
        for j in i:
          if game[positions[j][0]][positions[j][1]] != "O":
            break
        else:
          print(f"O player 'O' ganhou!")
          n = 9 + 1
    else:
      print("Posição ocupada!")
      continue
  n += 1