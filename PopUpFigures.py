figurespawnendboard = {'knight', 'bishop', 'rook', 'queen'}




def createbuttonspawnatendboard(fig1, fig2, fig3, fig4):

    fig1.pack()
    fig2.pack()
    fig3.pack()
    fig4.pack()


def deletebuttonandpawnchangefig(choosenfigure, knight, bishop, rook, queen):
    print(f'Your choice is: {choosenfigure}')
    knight.pack_forget()
    bishop.pack_forget()
    rook.pack_forget()
    queen.pack_forget()