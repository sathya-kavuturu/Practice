# 1.  *****
#     *****
#     *****
#     *****
#     *****
# 

def pattern1(n):
    print("1.")
    for row in range(n):
        for col in range(n):
            print("*", end='')
        print()

pattern1(5)

# 2.  *
#     **
#     ***
#     ****
#     *****

def pattern2(n):
    print("2.")
    for row in range(n):
        for col in range(row+1):
            print("*", end='')
        print()

pattern2(5)

# 
# 3.  *****
#     ****
#     ***
#     **
#     *
# 
def pattern3(n):
    print("3.")
    for row in range(n):
        for col in range(n-row):
            print("*", end='')
        print()

pattern3(5)

# 4.  1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
# 
def pattern4(n):
    print("4.")
    for row in range(n):
        for col in range(row+1):
            print(col+1, end=' ')
        print()

pattern4(5)

# 5.  *
#     **
#     ***
#     ****
#     *****
#     ****
#     ***
#     **
#     *
# 
def pattern5(n):
    print("5.")
    for row in range(int(n/2+1)):
        for col in range(row+1):
            print("*", end='')
        print()
    for row in range(int(n/2)):
        for col in range(int(n/2-row)):
            print("*", end='')
        print()  

pattern5(9)

        ###((((OR))))

def pattern5(n):
    print("5.")
    for row in range(2*n):
        totalcol = 2*n-row if row>n else row 
        for col in range(totalcol):
            print("*", end='')
        print()

pattern5(5)



# 6.       *
#         **
#        ***
#       ****
#      *****
# 
def pattern6(n):
    print("6.")
    for row in range(n):
        spaces = n-row
        for s in range(spaces):
            print(" ", end="")
        for col in range(row+1):
            print('*', end="")
        print()

pattern6(5)

# 7.   *****
#       ****
#        ***
#         **
#          *
# 
def pattern7(n):
    print("7.")
    for row in range(n):
        for space in range(row):
            print(" ", end='')
        for col in range(n-row):
            print("*", end='')
        print()

pattern7(5)

# 8.      *
#        ***
#       *****
#      *******
#     *********
# 
def pattern8(n):
    print('8.')
    for row in range(n):
        spaces = n-row
        for s in range(spaces):
            print(" ", end="")
        for col in range(row+1):
            print('*', end="")
        for col in range(row):
            print('*', end='')
        print()

pattern8(5)

# 9.  *********
#      *******
#       *****
#        ***
#         *
# 
def pattern9(n):
    print('9.')
    for row in range(n):
        for space in range(row):
            print(" ",end="")
        for col in range(n-row):
            print('*', end='')
        for col in range(n-1-row):
            print("*",end='')
        print()

pattern9(5)

# 10.      *
#         * *
#        * * *
#       * * * *
#      * * * * *
# 




# 11.  * * * * *
#       * * * *
#        * * *
#         * *
#          *
# 
# 
# 12.  * * * * *
#       * * * *
#        * * *
#         * *
#          *
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *
# 
# 
# 13.      *
#         * *
#        *   *
#       *     *
#      *********
# 
# 
# 14.  *********
#       *     *
#        *   *
#         * *
#          *
# 
# 
# 15.      *
#         * *
#        *   *
#       *     *
#      *       *
#       *     *
#        *   *
#         * *
#          *
# 
# 
# 16.           1
#             1   1
#           1   2   1
#         1   3   3   1
#       1   4   6   4   1
# 
# 
# 17.      1
#         212
#        32123
#       4321234
#        32123
#         212
#          1
# 
# 
# 18.   **********
#       ****  ****
#       ***    ***
#       **      **
#       *        *
#       *        *
#       **      **
#       ***    ***
#       ****  ****
#       **********
# 
# 
# 19.    *        *
#        **      **
#        ***    ***
#        ****  ****
#        **********
#        ****  ****
#        ***    ***
#        **      **
#        *        *
# 
# 
# 20.    ****
#        *  *
#        *  *
#        *  *
#        ****
# 
# 21.    1
#        2  3
#        4  5  6
#        7  8  9  10
#        11 12 13 14 15
# 
# 22.    1
#        0 1
#        1 0 1
#        0 1 0 1
#        1 0 1 0 1
# 
# 23.        *      *
#          *   *  *   *
#        *      *      *
# 
# 24.    *        *
#        **      **
#        * *    * *
#        *  *  *  *
#        *   **   *
#        *   **   *
#        *  *  *  *
#        * *    * *
#        **      **
#        *        *
# 
# 25.       *****
#          *   *
#         *   *
#        *   *
#       *****
# 
# 26.   1 1 1 1 1 1
#       2 2 2 2 2
#       3 3 3 3
#       4 4 4
#       5 5
#       6
# 
# 27.   1 2 3 4  17 18 19 20
#         5 6 7  14 15 16
#           8 9  12 13
#             10 11
# 
# 28.      *
#         * *
#        * * *
#       * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *
# 
# 29.      
#        *        *
#        **      **
#        ***    ***
#        ****  ****
#        **********
#        ****  ****
#        ***    ***
#        **      **
#        *        *
# 
# 30.         1
#           2 1 2
#         3 2 1 2 3
#       4 3 2 1 2 3 4
#     5 4 3 2 1 2 3 4 5
# 
# 
# 31.      4 4 4 4 4 4 4  
#          4 3 3 3 3 3 4   
#          4 3 2 2 2 3 4   
#          4 3 2 1 2 3 4   
#          4 3 2 2 2 3 4   
#          4 3 3 3 3 3 4   
#          4 4 4 4 4 4 4   
# 
# 32.    E
#        D E
#        C D E
#        B C D E
#        A B C D E
# 
# 33.    a
#        B c
#        D e F
#        g H i J
#        k L m N o
#      
# 34.    E D C B A
#        D C B A
#        C B A
#        B A
#        A


# 35.    1      1
#        12    21
#        123  321
#        12344321
#
