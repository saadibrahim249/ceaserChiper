# implementatoin of Ceaser Cipher using python

def cleanText(sting): # Fuction To Clean the Text By Removing Secial Characters
 remove=".,!@#$%^&*()=+:\"\'{_-}[]<>\\/?"
 for chr in sting:
    if chr in remove:
        sting=sting.replace(chr,"")
        sting=sting.lower()
 return sting.lower()


def enCipher(text,shift): #Fucntion To Encrypt the text
    enCipherString=''
    text=cleanText(text)
    for i in text:
        if i.isalpha():
            enCipherString += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
           enCipherString +=i
    return enCipherString


def deCipher(text,shift):
    deCipherString=""
    text=cleanText(text)
    for i in text:  
        if i.isalpha():
            deCipherString += chr((ord(i) - 97 - shift) % 26 + 97)
             
        else:
            deCipherString += i
    return deCipherString


def readFile(fname):
    lines = ""  
    with open(fname, 'r') as file:
        for line in file:
            lines += line
    print(lines)
    return lines

def writeFile(data,fname):
    file=open(fname,'w')
    file.write(data)


if __name__ == "__main__":
    while True:
        print('Select Your Desired Task:')
        print('1: Encrypt\n2: Decrypt')
        choice = input('Enter Your Choice: ')

        shifts = int(input("Enter The Number of Shifts: "))

        print('Select Your Desired Input Method:')
        print('1: File\n2: Manual')
        inputMethod = input("Enter Your Choice of Input: ")

        if inputMethod == '1':
            file = input("Enter the File Name from Which You Want to Read Data: ")
            data = readFile(file)
        else:
            data = input("Enter the Data: ")

        if choice == '1':
            Text = enCipher(data, shifts)
            print(Text)
        else:
            Text = deCipher(data, shifts)
            print(Text)

        saveOutput = input("Do You Want to Save the Output? (y/n): ")
        if saveOutput.lower() == "y":
            file = input("Enter the File Name to Which You Want to Write Data: ")
            writeFile(Text, file)

        condition = input('Do You Want to Perform More Tasks? (y/n): ')
        if condition.lower() == 'n':
            break

   