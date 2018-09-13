print("Please key in four integers (with one space between) "
      "to indicate the coordinates of two Queens on a chessboard: ")
s = input()
l = s.split(' ')
l = [int(i) for i in l]     # list comprehension

if l[0] == l[2] or l[1] == l[3] or abs(l[0] - l[2]) == abs(l[1] - l[3]):
    print("YES!")
else:
    print("NO!")
