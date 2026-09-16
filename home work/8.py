"""Given an unsorted array arr containing both positive and negative numbers. 
Your task is to rearrange the array and convert it into an array of alternate positive
and negative numbers without changing the relative order.
"""
class Solution:
    def rearrange(self, arr):
        pos = []
        neg = []

        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        pi = 0
        ni = 0
        i = 0
        while pi < len(pos) and ni < len(neg):
            if i % 2 == 0:
                arr[i] = pos[pi]
                pi += 1
            else:
                arr[i] = neg[ni]
                ni += 1
            i += 1

          while pi < len(pos):      

            arr[i] = pos[pi]
            pi += 1
            i += 1

       
        while ni < len(neg):
            arr[i] = neg[ni]
            ni += 1
            i += 1

        return arr