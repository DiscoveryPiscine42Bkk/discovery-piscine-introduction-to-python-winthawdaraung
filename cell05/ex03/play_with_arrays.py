#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()
for i in original_array:
    if i > 5:
        print(new_array)
        new_array.add(i+2)
print(original_array)
print(new_array)