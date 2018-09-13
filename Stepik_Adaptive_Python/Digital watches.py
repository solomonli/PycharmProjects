print("Please input elapsed seconds (less than 10 million): ", end='')
elapsed = int(input())

if elapsed > 3600*24:
    residual = elapsed % (3600*24)
    h = residual // 3600
    m = (residual % 3600) // 60
    s = (residual % 3600) % 60

else:
    h = elapsed // 3600
    m = (elapsed % 3600) // 60
    s = (elapsed % 3600) % 60

print("{:02d}:{:03d}:{:05d}".format(h, m, s))
# try '3601' seconds
