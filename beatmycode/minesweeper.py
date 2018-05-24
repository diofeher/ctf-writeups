def minesweeper(inpt):
    matrix = {}
    new_matrix = []
    # create matrix 
    for i, x in enumerate(inpt.split('\n')):
        for j, y in enumerate(x.replace(' ', '')):
            matrix[i,j] = y
    # do the count
    print
    for i, x in enumerate(inpt.split('\n')):
        new_line = []
        for j, y in enumerate(x.replace(' ', '')):
            count = 0
            if matrix[i,j] == 'X': 
                new_line.append('X')
                continue
            # vertical
            if matrix.get((i+1,j), '') == 'X': count += 1
            if matrix.get((i-1,j), '') == 'X': count += 1
            if matrix.get((i,j+1), '') == 'X': count += 1
            if matrix.get((i,j-1), '') == 'X': count += 1
            # diagonal
            if matrix.get((i+1,j+1), '') == 'X': count += 1
            if matrix.get((i+1,j-1), '') == 'X': count += 1
            if matrix.get((i-1,j-1), '') == 'X': count += 1
            if matrix.get((i-1,j+1), '') == 'X': count += 1
            new_line.append(str(count))
        new_matrix.append(new_line)
    # print new_matrix
    for i in new_matrix:
        print ' '.join(i)



# minesweeper("""O O O O X O O O O O
# X X O O O O O O X O
# O O O O O O O O O O
# O O O O O O O O O O
# O O O O O X O O O O""")
minesweeper("BMC_TEST_INPUT_MAGIC")