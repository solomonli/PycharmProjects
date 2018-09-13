time1 = [int(input()) for _ in range(3)]    # three inputs to form a list
time2 = [int(input()) for _ in range(3)]

units = [3600, 60, 1]
diff = sum(units[i] * (time2[i] - time1[i]) for i in range(3))

# a*(A1-B1) + b*(A2-B2) + c*(A3-B3)

print(diff)
