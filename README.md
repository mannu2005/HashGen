# 🔐 Hash Generator Tool

A powerful Python-based Hash Generator that supports multiple cryptographic, password hashing, and Windows authentication hash algorithms.

## 🚀 Features

* Generate hashes for user-provided text
* Supports 21+ hashing algorithms
* Cryptographic hash functions
* Password hashing algorithms
* Windows authentication hashes
* Interactive terminal menu
* Colored terminal interface
* Easy to use and lightweight

---

## 📌 Supported Algorithms

### MD Family

* MD5

### SHA Family

* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

### SHA3 Family

* SHA3_224
* SHA3_256
* SHA3_384
* SHA3_512

### BLAKE Family

* BLAKE2S
* BLAKE2B

### Password Hashing

* BCRYPT
* ARGON2
* ARGON2I
* ARGON2D
* ARGON2ID
* SCRYPT
* PBKDF2

### Windows Hashes

* NTLM
* LM

---

## 📂 Project Structure

Hash_Generator/

├── start.py

├── code.py

├── banner.py

├── requirements.txt

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/mannu2005/HashGen.git
cd Hash_Generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Program

```bash
python start.py
```

---

## 📦 Requirements

```text
bcrypt
argon2-cffi
pycryptodome
impacket
```

---

## 🖥️ Usage

Run the program:

```bash
python start.py
```

Example:

```text
[+] Enter Text: hello

[01] MD5
[02] SHA1
[03] SHA224
[04] SHA256
...
[21] LM

[+] Select Hash Number: 4
```

Output:

```text
SHA256 HASH GENERATED

2cf24dba5fb0a30e26e83b2ac5b9e29e...
```

---

## 🔒 Security Notes

* BCRYPT uses random salt generation.
* ARGON2 is a modern password hashing algorithm.
* SCRYPT and PBKDF2 are designed for password storage.
* NTLM and LM hashes are included for educational and compatibility purposes.
* LM hashing is deprecated and insecure for modern systems.

---

## 📚 Technologies Used

* Python 3
* hashlib
* bcrypt
* argon2-cffi
* pycryptodome
* impacket

---

## 🎯 Educational Purpose

This project is intended for:

* Cybersecurity Students
* Ethical Hackers
* Penetration Testers
* Digital Forensics Learners
* Developers learning cryptography

---

## 👨‍💻 Author

Mannu Yadav

BCA Student | Developer | Cybersecurity Enthusiast

---

## ⭐ Support

If you found this project useful:

* Star the repository
* Fork the repository
* Share with others

Happy Coding 🚀
