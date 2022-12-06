inputfile = open('aoc_input.txt', 'r')
datastream = inputfile.read()

# Part 1
markers = []
for position in range(3, len(datastream)):
    for character in datastream[position]:
        marker = []
        marker.append(datastream[position-3])
        marker.append(datastream[position-2])
        marker.append(datastream[position-1])
        marker.append(datastream[position])
        if len(set(marker)) == 4:
            markers.append(position+1)
print(markers[0])

# Part 2
markers = []
for position in range(13, len(datastream)):
    for character in datastream[position]:
        marker = []
        for xx in range (0, 14):
            marker.append(datastream[position-xx])
        if len(set(marker)) == 14:
            markers.append(position+1)
print(markers[0])
