ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff [1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])



planes = ['plane0', 'plane1', 'plane2', 'plane3', 'plane4']

print "There is space for a total of 7 planes on the runway."
more_planes = ['plane5', 'plane6', 'plane7', 'plane8']

while len(planes) != 7:
    next_plane = more_planes.pop(0)
    print "Rolling out: ", next_plane
    planes.append(next_plane)
    print "There are %i planes now." % len(planes)
    
print "Displaying different planes in the runway:"

print planes[2]
print planes[1]
print planes[0]
print planes[-1]
print ", The next plane to depart is: ".join(planes[0:6])


