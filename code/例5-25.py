from random import sample
from itertools import combinations

def subAscendingList(lst):
    for length in range(len(lst), 0, -1):
        for sub in combinations(lst, length):
            if list(sub) == sorted(sub):
                return sub

def getList(start=0, end=1000, number=20):
    if number > end-start:
        return None
    return sample(range(start,end), number)

def main():
    lst = getList(number=10)
    if lst:
        print(lst)
        print(subAscendingList(lst))

main()
