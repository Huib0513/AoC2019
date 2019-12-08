#!python3

lines = str(open('day8.input').read())
layersize = 150
linesize = 25

#Testdata
#lines = '0222112222120000'
#layersize = 4
#linesize = 2

layers = []

def printlayer(image):
    for line in range(6):
        regel = ''
        offset = line * linesize
        for pixel in range(linesize):
            if image[offset + pixel] == '0':
                regel = regel + ' '
            else:
                regel = regel + '.'
        print(regel)

for layer in range(0, len(lines)-1, layersize):
    laag = lines[layer:layer+layersize]
    layers.append(laag)

minzeros = 151
result = -1
for laag in layers:
    printlayer(laag)
    ll = list(laag)
    if ll.count('0') < minzeros:
        minzeros = ll.count('0')
        result =ll.count('1') * laag.count('2')

print("Resultaat deel 1: " + str(result))

image = []
for pixel in range(len(layers[0])):
    for laag in layers:
        if laag[pixel] != '2':
            image.append(laag[pixel])
            break

printlayer(image)