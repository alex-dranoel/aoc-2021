import numpy as np

octopus = np.array([list(l.strip()) for l in open('input.txt')], dtype=int)
n_row, n_col = octopus.shape
n_flashes = step = 0

while True:
    step += 1
    octopus += 1
    flashed = np.full_like(octopus, False)
    while np.sum(octopus > 9) > 0:
        for row in range(n_row):
            for col in range(n_col):
                if octopus[row, col] > 9 and not flashed[row, col]:
                    flashed[row, col] = True
                    octopus[max(row-1, 0):min(row+1, n_row-1)+1, max(col-1, 0):min(col+1, n_col-1)+1] += 1
                    
        octopus[flashed == True] = 0

    n_flashes += np.sum(flashed)
    if step == 100:
        print('Part 1:', n_flashes)
        
    if np.sum(flashed) == n_row*n_col:
        print('Part 2:', step)
        break

