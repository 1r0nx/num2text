# num2text

A collection of tools to convert numbers into text

Convert numbers from different numeral systems into human-readable text.\
Supports **binary**, **octal**, **ASCII**, and **hexadecimal** inputs.

---

## 🚀 Features

- Convert **binary** to text
- Convert **octal** to text
- Convert **ASCII codes** to text
- Convert **hexadecimal** to text
- Supports multiple numbers at once (separated by space/comma)

---

## 🧱 Requirements

- Python 3.x
- Optional: pyInstaller to compile the scripts into binaries

Install PyInstaller with:

```bash
pip3 install pyinstaller
```

## 🔧 Installation

Clone the repository and create a binary:
```bash
git clone https://github.com/1r0nx/num2text.git
cd num2text
chmod +x build.sh
./build.sh
sudo cp dist/* /usr/bin/
```
All the executable will be in dist/

Or run it as a script:
```bash
git clone https://github.com/1r0nx/num2text.git
cd num2text
chmod +x *.py
```

## ⚙️ Example 1

```bash
❯ hex2text -s "0x48 0x65 0x6C 0x6C 0x6F"
```

Output:

```bash
Hello
```


## ⚙️ Example 2

```bash
❯ ascii2text -s "72 101 108 108 111"
```

Output:

```bash
Hello
```

## ⚙️ Example 3

```bash
❯ cat bin.txt 
01001000 01100101 01101100 01101100 01101111 00001010  
 
❯ bin2text -f bin.txt 
Hello
```

## ⚙️ Example 4

```bash
❯ cat octal.txt 
110 145 154 154 157

❯ octal2text -f octal.txt 
Hello
```


## 📜 License

MIT License

---

## 🙋 Contributing

Pull Requests and suggestions are welcome. Please follow standard coding practices and document your changes.

