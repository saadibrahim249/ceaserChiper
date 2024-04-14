**Ceasar Cipher Implementation in Python**

Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### Implementation Overview:

This Python implementation of the Caesar Cipher consists of the following components:

1. **Cleaning Text Function (`cleanText`):** This function removes special characters from the input text and converts it to lowercase for uniformity.

2. **Encryption Function (`enCipher`):** This function encrypts the text using the Caesar Cipher algorithm. It shifts each letter in the plaintext by a fixed number of positions down the alphabet.

3. **Decryption Function (`deCipher`):** This function decrypts the text encrypted using the Caesar Cipher algorithm. It shifts each letter in the ciphertext by a fixed number of positions up the alphabet to recover the original plaintext.

4. **File Input/Output Functions (`readFile`, `writeFile`):** These functions facilitate reading input data from a file and writing output data to a file, respectively.

5. **Main Program:** The main program provides a menu-driven interface for users to choose between encryption and decryption, select the number of shifts, choose the input method (file or manual input), and optionally save the output to a file.

### Usage:

1. Run the program.
2. Choose whether you want to encrypt or decrypt.
3. Specify the number of shifts (the key).
4. Select the input method (file or manual input).
5. Enter the data or provide the filename if reading from a file.
6. View the output.
7. Optionally, save the output to a file.

### Example Usage:

```plaintext
Select Your Desired Task:
1: Encrypt
2: Decrypt
Enter Your Choice: 1
Enter The Number of Shifts: 3
Select Your Desired Input Method:
1: File
2: Manual
Enter Your Choice of Input: 2
Enter the Data: Hello World!
Khoor Zruog!
Do You Want to Save the Output? (y/n): y
Enter the File Name to Which You Want to Write Data: encrypted.txt
Do You Want to Perform More Tasks? (y/n): n
```

This implementation provides a straightforward way to encrypt and decrypt text using the Caesar Cipher algorithm in Python.
