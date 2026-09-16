"""arr = [10, 20, 10, 30, 20, 10]
Key     Value
----         -----
10  →    3
20  →    2
30  →    1"""

arr = [10, 20, 10, 30, 20, 10]
frequency = {}
for x in arr:
    frequency[x] = frequency.get(x, 0) + 1
print(frequency)