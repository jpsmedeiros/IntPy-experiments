import time

def heap_permutation(data, n):
    if n == 1:
        #print(data)
        return
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]

data = [1, 2, 3, 4, 5, 6]
start_time = time.time()
heap_permutation(data, len(data))
end_time = time.time()
print(end_time - start_time)