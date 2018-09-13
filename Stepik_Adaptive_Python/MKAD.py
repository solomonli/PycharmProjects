'''print("Please enter Biker Vasya's speed '+ or -': ", end='')
V = int(input())

print("Please enter Biker Vasya's travel time: ", end='')
T = int(input())

mark = 0; circumference = 109
if V * T > circumference:
    mark = V*T % circumference
else:
    mark = V*T

if mark >= 0:
    print("Stop mark at: {}".format(mark))
else:
    print("Stop mark at: {}".format(circumference + mark))
'''
v, t = int(input()), int(input())
s = 109
m = (v * t) % s
print(m)
