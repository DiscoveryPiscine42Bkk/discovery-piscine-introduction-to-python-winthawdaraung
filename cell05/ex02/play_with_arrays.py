#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for i in range(len(original_array)):
    if original_array[i] > 5:
        new_array.append(original_array[i]+2)

print(original_array)
print(new_array)