numbers = [int(input()) for _ in range(int(input()))]
# input x times

print(sum(i for i in numbers if i % 10 == 4))
