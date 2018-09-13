grades = [int(input()) for _ in range(int(input()))]

counts = [grades.count(i) for i in range(2, 6)]

print(*counts)

# I think I can use dictionary to count grades
