import numpy as np

iea = open('input.txt').readline().strip()

ii = []
for i,l in enumerate(open('input.txt')):
    l = l.strip()
    if i < 2:
        continue
    ii.append([int(c == '#') for c in l])

ii = np.array(ii)

print(ii)

output = np.copy(ii)

for step in range(50):
    n_row, n_col = output.shape

    bounded = np.full((n_row+4, n_col+4), step%2)
    bounded[2:n_row+2, 2:n_col+2] = output

    output = np.copy(bounded)
    for i in range(1,n_row+3):
        for j in range(1,n_col+3):
            sub = bounded[i-1:i+2, j-1:j+2]
            idx = int(''.join(map(str, np.reshape(sub, (1, 9))[0])), 2)
            output[i,j] = int(iea[idx] == '#')
        
    output[0, :] = 1 if bounded[0, 0] == 0 else 0
    output[n_row+3, :] = 1 if bounded[n_row+3, 0] == 0 else 0
    output[:, 0] = 1 if bounded[0, 0] == 0 else 0
    output[:, n_col+3] = 1 if bounded[0, n_col+3] == 0 else 0

print(np.sum(output))