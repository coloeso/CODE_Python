'''
print triangular pattern like
    *
   **
  ***--------------------------------
 ****
*****

Version:0.1
Author:coloeso
Data:2023-04-07------------------
'''
row = int(input('input the number:'))

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

# other verson

row = int(input('input the number:'))

for i in range(1,row+1):
    for j in range(1,row+1):
        if j <= row - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

'''
print triangular pattern like
    *
   ***
  *****
 *******
*********

Version:0.1
Author:coloeso
Data:2023-04-07
'''