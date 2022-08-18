field=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    ["1"]]
    
def print_field():
    for i in range(3):
        for j in range(3):
            print (field[i][j], ' | ', end=' ')
        print ("\n----------------")
        
def next_move(s):
    if s:
        print ("Сейчас ходят крестики.")
    else:
        print ("Сейчас ходят нолики.")
    i=4
    j=1
    while field[i-1][j-1]!=' ':
        i, j=input("Ваш ход: ").split()
        i=int(i)
        j=int(j)
        if field[i-1][j-1]!=' ': print ("Эта клетка уже занята")
    field[i-1][j-1]='X' if s else 'O'
    
def check():
    xxx=['X', 'X', 'X']
    zzz=['O', 'O', 'O']
    win_cross=False
    win_cross=(field[0]==xxx) or (field[1]==xxx) or (field[2]==xxx)
    win_cross=win_cross or ([field[0][0], field[1][0], field[2][0]]==xxx)
    win_cross=win_cross or ([field[0][1], field[1][1], field[2][1]]==xxx)
    win_cross=win_cross or ([field[0][2], field[1][2], field[2][2]]==xxx)
    win_cross=win_cross or ([field[0][0], field[1][1], field[2][2]]==xxx)
    win_cross=win_cross or ([field[0][2], field[1][1], field[2][0]]==xxx)
    zero_cross=False
    zero_cross=(field[0]==zzz) or (field[1]==zzz) or (field[2]==zzz)
    zero_cross=zero_cross or ([field[0][0], field[1][0], field[2][0]]==zzz)
    zero_cross=zero_cross or ([field[0][1], field[1][1], field[2][1]]==zzz)
    zero_cross=zero_cross or ([field[0][2], field[1][2], field[2][2]]==zzz)
    zero_cross=zero_cross or ([field[0][0], field[1][1], field[2][2]]==zzz)
    zero_cross=zero_cross or ([field[0][2], field[1][1], field[2][0]]==zzz)
    if win_cross: print("Выиграли крестики!")
    if zero_cross: print("Выиграли нолики!")
    return win_cross or zero_cross
    
print("Крестики и нолики ходят по очереди. Введите номер строки и столбца (через пробел, от 1 до 3).")
k=0
while (not check()) and (k<9):
    k+=1
    next_move(k % 2)
    print_field()
    
if (k==9): print ("Ничья.")
