play = 1

xo = "x"

place = [1,2,3,4,5,6,7,8,9]

for x in place:
    if (play == place[x-1]):
            x = xo
            place[play-1] = x
            print(place[0])
