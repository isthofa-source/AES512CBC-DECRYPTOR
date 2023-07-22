# AES512CBC-DECRYPTOR
This script to perform decryption using the Advanced Encryption Standard (AES) algorithm with Cipher Block Chaining (CBC) mode and a 512-bit key length.

## POC
- This is sample file CTF Gemastik 2023 Forensik

![image](https://github.com/isthofa-source/AES512CBC-DECRYPTOR/assets/75401288/f18cfb52-6e30-49dd-aa0d-2dce07ac60f1)

- Experiment with extracting information from the image. Here I use Zsteg.
![image](https://github.com/isthofa-source/AES512CBC-DECRYPTOR/assets/75401288/447345c1-448a-4b4a-8cfc-d44b357501fc)

- From this information we can see that there is a data line in base64 form. Decode the data to see the information in plaintext.
![image](https://github.com/isthofa-source/AES512CBC-DECRYPTOR/assets/75401288/e36b655b-1dc8-46f4-a955-34d60e13142f)

- We get information in the form of the encryption used, the key and the message that will be decrypted using the encryption
![image](https://github.com/isthofa-source/AES512CBC-DECRYPTOR/assets/75401288/70c4c06b-3565-442f-ab93-3fd81801ef5f)

- We can use the aes512cbc.py script to decrypt the message.
![image](https://github.com/isthofa-source/AES512CBC-DECRYPTOR/assets/75401288/0430a920-45bb-4765-8173-3218245aed2e)

## DESCRIPTION

  This code imports required modules from the **cryptography.hazmat** library, which provides cryptographic algorithms such as AES and modes like CBC. The **base64** module is imported to perform decoding of the given base64-encoded ciphertext.
  This function takes two parameters: **key**, which is the encryption key (represented as a string), and **ciphertext**, which is the encrypted text (represented in base64 format). The function's purpose is to decrypt the ciphertext using the AES algorithm with CBC mode and the given key. The **key** variable holds the encryption key as a string, and the **ciphertext** variable holds the encrypted text in base64 format.
  The **plaintext** variable will contain the decrypted text after calling the **decrypt_aes_512_cbc()** function with the provided **key** and **ciphertext**. The decrypted result, which is in bytes, will be converted to a string using **.decode('utf-8')**, and then it will be printed to the screen.

So, this code will output the decrypted text from the ciphertext using the key and display it on the screen.

Hope it is useful :)
