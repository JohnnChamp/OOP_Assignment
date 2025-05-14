# 🚗✈️🚢 Polymorphism Challenge — Vehicles in Motion

## 🎯 Goal

This project demonstrates **polymorphism** using a set of vehicle classes. Each class shares the same method name `move()` but behaves differently. This is a core concept in **Object-Oriented Programming (OOP)**.

---

## 📦 Files

- `vehicles.py` — Contains the `Vehicle` base class and its subclasses (`Car`, `Plane`, `Boat`, `Bicycle`).
- `main.py` — Runs the polymorphism demo.
- `README.md` — Project documentation.

---

## 🧠 Concepts

### What is Polymorphism?

Polymorphism allows objects of different classes to be treated as objects of a common superclass, while still executing their own overridden behaviors.

In this project, all vehicle types override the `move()` method in their own unique way.

---

## 🧱 Classes

### Base Class: `Vehicle`
```python
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")
