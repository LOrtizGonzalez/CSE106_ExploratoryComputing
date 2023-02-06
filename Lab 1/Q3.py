#Lab 1 Q3: WORD COUNT

#range between 65 and 162
def sortChar(array, string):
    i = 0
    some = " "
    while(i < len(string)):
        if(ord(string[i]) >= 65 and ord(string[i]) <= 162):
            some += string[i]
        else:
            array.append(some)
            some = " "
        i += 1

def wordCount(arr, word1):
    length = len(word1)
    count = 0
    for i in arr:
        some = i.lower()
        some = some.strip(" ")
        if(some[:length] == word1[:length]):
            count += 1  
    return count

#              ----- PROGRAM STARTS HERE ------
def main():
    word = input("Enter a word: ")
    word = word.lower()
    size = len(word)
    number = 0
    count = 0
    s = " "
    r = ""
    arr = []

    file = open("PythonSummary.txt", 'r')
    while(s):
        s = file.readline()
        r += s.strip()
    file.close()

    sortChar(arr, r)
    times = wordCount(arr,word)
    print("The word ", word, "appears ",times, "times.\n")

if __name__ == '__main__':
    main()