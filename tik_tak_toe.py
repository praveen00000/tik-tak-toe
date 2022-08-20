'''TIK TAK TOE GAME USING PYTHON ITS A VERY BASIC VERSION'''


def sum(a,b,c):
    return a+b+c

def printboard(x,y):
    zero='X' if x[0] else ('0' if y[0] else 0)
    one='X' if x[1] else ('0' if y[1] else 1)
    two='X' if x[2] else ('0' if y[2] else 2)
    three='X' if x[3] else ('0' if y[3] else 3)
    four='X' if x[4] else ('0' if y[4] else 4)
    five='X' if x[5] else ('0' if y[5] else 5)
    six='X' if x[6] else ('0' if y[6] else 6)
    seven='X' if x[7] else ('0' if y[7] else 7)
    eight='X' if x[8] else ('0' if y[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    
def tocheck(x,y):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if(sum(x[win[0]],x[win[1]],x[win[2]])==3):
            print("X won the match")
            return 1
        if(sum(y[win[0]],y[win[1]],y[win[2]])==3):
            print("0 won the match")
            return 0
        else:
            return -1
    
x=[0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0]
turn=1
print("Welcome to Tic Tac Toe")

while(True):
    printboard(x,y)
    if turn==1:
        print("X's chance")
        value=int(input("Enter the index u want to chose: "))
        x[value]=1
    else:
        print("0's chance")
        value=int(input("Enter the index u want to chose: "))
        y[value]=1
    cwin=tocheck(x,y)
    if(cwin!=-1):
        print("game over")
        break
    turn=1-turn