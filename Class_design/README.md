# Smartphone Class Project 📱

## Overview

This Python project demonstrates **Object-Oriented Programming (OOP)** concepts using a `Smartphone` class and a subclass `GamingPhone`. It showcases:

- **Encapsulation** (private attributes like battery level)
- **Inheritance** (GamingPhone inherits from Smartphone)
- **Polymorphism** (method overriding)

---

## 📦 Files Included

- `smartphone.py` — Contains the class definitions.
- `main.py` — Demonstrates how to use the classes.
- `README.md` — Project documentation.

---

## 📘 Classes

### `Smartphone`

Represents a general smartphone.

**Attributes:**
- `brand`
- `model`
- `__battery_life` (private)
- `price`

**Methods:**
- `get_battery_status()`
- `charge_phone(amount)`
- `use_phone(hours)`
- `phone_info()`

---

### `GamingPhone` (inherits from `Smartphone`)

Adds a `performance_mode` attribute and custom behavior.

**Extra Methods:**
- `activate_performance_mode()`
- `phone_info()` (overrides the parent method)

---

## ▶️ How to Run

1. Make sure `smartphone.py` and `main.py` are in the same folder.
2. Run the code using:

```bash
python main.py
