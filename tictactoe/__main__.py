def main():
    place = [1,2,3,4,5,6,7,8,9]

    turn = 0

    while (checkwin):
        drawboard(place)
        turn += 1
        xo = " "

        if (turn % 2 == 0):
            play = int(input("x's turn to choose a square (1-9):"))
            xo = "x"
        else:
            play = int(input("o's turn to shoose a square (1-9):"))
            xo = "o"

        makechange(play, xo, place)

def drawboard(place):
    print(f"{place[0]}|{place[1]}|{place[2]}\n-+-+-\n{place[3]}|{place[4]}|{place[5]}\n-+-+-\n{place[6]}|{place[7]}|{place[8]}")

def makechange(play, xo, place): 
    for x in place: 
        if (play == place[x - 1]):
            x = xo
            place[play-1] = x

def checkwin(place):
    return (place[0] == place[1] == place[2] or
            place[3] == place[4] == place[5] or
            place[6] == place[7] == place[8] or
            place[0] == place[3] == place[6] or
            place[1] == place[4] == place[7] or
            place[2] == place[5] == place[8] or
            place[0] == place[4] == place[8] or
            place[2] == place[4] == place[6])

def checkdraw(place):
    if not checkwin(place):
        return ()

if __name__ == "__main__":
    main()
    