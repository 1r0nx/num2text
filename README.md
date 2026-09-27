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
- Split a string into fixed-size chunks (**str_split**)
- Supports multiple numbers at once (separated by space/comma), `0x`/`0o`/`0b` prefixes, and contiguous forms
- Robust: out-of-range or noisy tokens are skipped instead of crashing

---

## 🧱 Requirements

- Python 3.x
- Optional: pyInstaller to compile the scripts into binaries

Install PyInstaller with:

```bash
pip3 install pyinstaller
```

## 🔧 Installation

Clone the repository and build standalone binaries with PyInstaller:
```bash
git clone https://github.com/1r0nx/num2text.git
cd num2text
for s in bin2text octal2text ascii2text hex2text str_split; do
    pyinstaller --onefile "src/$s.py"
done
sudo cp dist/* /usr/bin/
```
All the executables will be in dist/

Or run them directly as scripts:
```bash
git clone https://github.com/1r0nx/num2text.git
cd num2text
chmod +x src/*.py
python3 src/hex2text.py -s "48 65 6C 6C 6F"
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

## ⚙️ Example 5 — str_split

Split a string into fixed-size chunks (handy to prepare input for the converters):

```bash
❯ str_split -s "48656c6c6f" -n 2
48 65 6c 6c 6f

❯ str_split -s "48656c6c6f" -n 2 -se ":"
48:65:6c:6c:6f
```


## 📜 License

MIT License

---

## 🙋 Contributing

Pull Requests and suggestions are welcome. Please follow standard coding practices and document your changes.

