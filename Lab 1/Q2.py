# Lab 1 Q2

def main():
    sentence = input("Enter a sentence: ")
    number = int(input("Enter the number of times to be written: "))
    #print(sentence, number)
    file = open('CompletedPunishment.txt','w')
    i = 0
    while(i < number):
        file.write(sentence)
        file.write('\n')
        i += 1
    file.close()

if __name__ == '__main__':
    main()