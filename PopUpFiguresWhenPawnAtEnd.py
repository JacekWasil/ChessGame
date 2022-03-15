figurespawnendboard = {'knight', 'bishop', 'rook', 'queen'}


def showbuttonspawnatendboard(fig1, fig2, fig3, fig4):
    fig1.place(x=220, y=600)
    fig2.place(x=290, y=600)
    fig3.place(x=360, y=600)
    fig4.place(x=430, y=600)


def choosebuttonandpawnchangefig(choosenfigure, knight, bishop, rook, queen):
    knight.place(x=-100, y=600)
    bishop.place(x=-100, y=600)
    rook.place(x=-100, y=600)
    queen.place(x=-100, y=600)
    return choosenfigure

