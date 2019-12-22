#!python3

process = [line.strip('\n') for line in open("day22.input").readlines()]
decksize = 10007

#testinput
#decksize = 10
#process = ["deal with increment 7", "deal into new stack", "deal into new stack"] # output is 0 3 6 9 2 5 8 1 4 7
#process = ["cut 6", "deal with increment 7", "deal into new stack"] # output is 3 0 7 4 1 8 5 2 9 6
#process = ["deal with increment 7", "deal with increment 9", "cut -2"] # output is 6 3 0 7 4 1 8 5 2 9
#process = ["deal into new stack", "cut -2", "deal with increment 7", "cut 8", "cut -4", "deal with increment 7", "cut 3", "deal with increment 9", "deal with increment 3", "cut -1" ] # output is 9 2 5 8 1 4 7 0 3 6


def shuffle(deck, process):
    for line in process:
        if line == "deal into new stack":
            deck.reverse()
            #print("reversed to " + str(deck))
        elif line[:3] == "cut":
            offset = int(line[4:])
            newdeck = []
            newdeck.extend(deck[offset:])
            newdeck.extend(deck[:offset])
            deck = newdeck
            #print("cut with offset " + str(offset) + " to " + str(deck))
        elif line[:4] == "deal":
            # do smart stuff 
            increment = int(line[20:])
            newdeck = {}
            for c in range(decksize):
                offset = c * increment
                newdeck[offset % decksize] = deck[c]
            for c in range(decksize):
                deck[c] = newdeck[c]
            #print("dealt with increment " + str(increment) + " to " + str(deck))
    return deck

startdeck = [x for x in range(decksize)]
resultdeck = shuffle(startdeck, process)
print(resultdeck.index(2019))

decksize = 119315717514047
deck2 = [x for x in range(decksize)]
for _ in range(101741582076661):
    deck2 = shuffle(deck2, process)

print(deck2[2020])