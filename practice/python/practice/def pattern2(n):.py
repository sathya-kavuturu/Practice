def pattern2(n):
    print("2.")
    for row in range(n):
        col=0
        for(col=0; col<=row; col++):
            print("*", end='')
        print()
pattern2(5)