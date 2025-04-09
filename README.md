# 🧮 Fraction Arithmetic and Comparison in Python

**Author**: Krishna Tripathi

---

## 📌 Overview

This project demonstrates a simple yet powerful **object-oriented Python class** to perform **arithmetic operations** and **comparisons** between two fractions. It includes:

- Fraction Addition, Subtraction, Multiplication, Division
- Fraction Simplification using `math.gcd`
- Fraction Comparisons: Equal, Not Equal, Greater Than, Less Than

---

## 📦 Features

- ➕ Addition of two fractions
- ➖ Subtraction of two fractions
- ✖️ Multiplication of two fractions
- ➗ Division of two fractions
- 📉 Automatic simplification of results
- 🔍 Fraction comparisons (`==`, `!=`, `<`, `>`)

---

## 🛠️ Requirements

- Python 3.6 or above
- No external dependencies

---

## 🚀 How to Use

### 🔢 Example

```python
from fraction import Fraction  # if saved as fraction.py

f = Fraction(16, 20, 5, 2)

print("Add:       ", f.__add__())
print("Subtract:  ", f.__sub__())
print("Multiply:  ", f.__mul__())
print("Divide:    ", f.__truediv__())
print("Equal:     ", f.__eq__())
print("Less than: ", f.__lt__())
print("Greater:   ", f.__gt__())
