## Problem Descriptions

### **1. Convert Hex to Base64 and Back**
Write a program that converts a hex-encoded string to base64 and vice versa.

#### **Example**
**Input (Hex):**
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```

**Expected Output (Base64):**
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

---

### **2. Fixed XOR**
Write a function that takes two equal-length buffers and produces their XOR sum.

#### **Example**
**Input (Hex):**
```
1c0111001f010100061a024b53535009181c
```

**XOR Against:**
```
686974207468652062756c6c277320657965
```

**Expected Output:**
```
746865206b696420646f6e277420706c6179
```

---

### **3. Single-character XOR Cipher**
A given hex-encoded string has been XOR'd against a **single character**. Your task is to find the key and decrypt the message.

#### **Input (Hex):**
```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

#### **Approach**
- Attempt XOR decryption using all possible **single-character** keys.
- Use a **scoring function** based on character frequency to determine which output is the most likely English plaintext.
- Fine-tune your algorithm to ensure accuracy.

---

## Requirements
- Your program should be written in the programming language of your choice.
- The source file must be named **`crypto.zzz`**, where `zzz` is the appropriate file extension for your chosen language.
- The program should **not** hardcode the sample input/output but should instead read from and write to files.
- Follow the general problem descriptions rather than solving only the provided examples.

## Notes
- If using Python, refer to the provided sample solution for file I/O handling.
- Ensure your implementation handles **different inputs dynamically**.
- Use appropriate libraries for **hex encoding/decoding, Base64 conversion, and bitwise XOR operations**.

