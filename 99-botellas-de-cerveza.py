def sing(b, end):
    print b or 'No more', 'bottle' + ('s' if b-1 else ''), end

for i in range(99, 0, -1):
    sing(i, 'of beer on the wall, ')
    sing(i, 'of beer, ')
    print "Take one down and pass it around, "
    sing(i-1, 'of beer on the wall.\n')