import time

start_time = time.time()

for j in range(10):
    for i in range(50):
        if (i > 25):
            print(("j : %d, i : %d")%(j,i))
            break
    print(j)

print("duration : %d" % (time.time() - start_time))
