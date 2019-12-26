

from games import *


print("Do you want to take X or O")
user_ch=input()
if user_ch=='X':
    comp_ch='O'
else:
    comp_ch='X'

print("Do you want to move first ? Y or N")
m=input()
if m=='Y':
    turn=user_ch
else:
    turn=comp_ch


mys=GameState(to_move=turn, utility=0, board={},moves=[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]) #GameState to collect best moves 
ttt=TicTacToe()#Creating TicTacToe game


while not(ttt.terminal_test(mys)):
    if user_ch==mys.to_move:
        print("Available Moves for You")
        print(mys.moves)
        print("Enter the move in the formate (row,column)")
        r=int(input())
        c=int(input())
        v=(r,c)
        print(v)
        mys=ttt.result(mys,v)
        print("Your Move ")
        ttt.display(mys)
    else:
        returned_list2=alphabeta_search(mys,ttt)
        w=returned_list2.pop()    
        mys=ttt.result(mys,w)
        print("AI Computers Moves ")
        ttt.display(mys)


if comp_ch=='X':
    if mys.utility==1 :
        print("Opps !! You lose,AI wins")
    elif mys.utility==-1 :
        print("Congrats!!You Win")
    elif mys.utility==0:
        print("Its a tie")
else:
    if mys.utility==1 :
        print("Congrats!!You Win")
        
    elif mys.utility==-1 :
        print("Opps !! You lose,AI wins")
        
    elif mys.utility==0:
        print("Its a tie")




