seconds = int(input())

units = [3600, 60, 1]

times = [24, 60, 60]

watches = [seconds // units[i] % times[i] for i in range(3)]
###     super super smart!

# print('%d:%02d:%02d' % tuple(watches))

print("{w[0]:02d}:{w[1]:03d}:{w[2]:05d}".format(w=watches))
