#Lab2 Q1

import numpy as np

def main():
    #a)
    arr = np.arange(2,10).reshape(4,2)
    print(arr)
    #b) NEED TO CORRECT
    # arr2 = [n for n in range(0,2)].reshape(8,8)
    # print(arr2)
    #c)
    print("\n")
    List = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
    print("\nOriginal list:", List)
    print("\nUnique from list values:",np.unique(List))
    #d)
    List = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
    print("\nValues greater than 37:",List[np.where((List > 37))])
    #e)
    change = (9/5)
    change2 = 32
    List = np.array([0, 12, 45.21 ,34, 99.91])
    print("\nCentrigrade degrees:", List)
    List2 = np.array([0, 12, 45.21 ,34, 99.91]) * change + change2
    print("Farenheit degrees:", List2)


if __name__ == '__main__':
    main()