import numpy as np

iea, _, *ii = open('input.txt').read().splitlines()
output = np.array([[int(p == "#") for p in row] for row in ii])

for step in range(50):
    n_row, n_col = output.shape

    bounded = np.full((n_row+4, n_col+4), 0 if iea[0] == '.' else step%2)
    bounded[2:n_row+2, 2:n_col+2] = output

    output = np.copy(bounded)
    for i in range(1,n_row+3):
        for j in range(1,n_col+3):
            sub = bounded[i-1:i+2, j-1:j+2]
            idx = int(''.join(map(str, np.reshape(sub, (1, 9))[0])), 2)
            output[i,j] = int(iea[idx] == '#')

    if int(iea[0] == '#'):
        output[0, :] = 1 if bounded[0, 0] == 0 else 0
        output[n_row+3, :] = 1 if bounded[n_row+3, 0] == 0 else 0
        output[:, 0] = 1 if bounded[0, 0] == 0 else 0
        output[:, n_col+3] = 1 if bounded[0, n_col+3] == 0 else 0

print(np.sum(output))