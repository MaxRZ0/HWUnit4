list_1 = [11, 92, 1, 42, 15, 12, 11, 81]
max_count = 0

for i in range(len(list_1)):
    if (list_1[i-2] + list_1[i-1] + list_1[i]) > max_count:
        max_count = list_1[i-2] + list_1[i-1] + list_1[i]
        max_idx = i - 1

print(f'Макс. кол-во ягод {max_count}, собрано для куста {max_idx+1}')
