import numpy as np

print('Part 1:', sum(np.diff(np.loadtxt('input.txt')) > 0))

arr = np.convolve(np.loadtxt('input.txt'), np.ones(3, dtype=np.int), mode='valid')
print('Part 2:', sum(np.diff(arr) > 0))
