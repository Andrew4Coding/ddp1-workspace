for i in range(1, 15):
    for j in range(1, 15):
        for z in range(100):
            if i*j == z**2 and i != j:
                print(i, j)