# 👨‍👩‍👧‍👦 Day 18 - User System with Inheritance

Welcome to **Day 18** of my **#30DaysOfPythonChallenge**!  
Today’s focus was on mastering **inheritance** and **multiple inheritance** in Python using OOP.

---

## 📌 Topic
**Object-Oriented Programming: Inheritance & Multiple Inheritance**

---

## 🧠 What I Built

A **User System** that models different types of users with varying roles and capabilities using inheritance:

### 🧩 Class Structure

- **Base Class:**
  - `User`: Contains basic user details and methods.
  
- **Derived Classes:**
  - `Admin`: Inherits from `User`, includes admin privileges.
  - `Customer`: Inherits from `User`, includes shopping cart and checkout methods.
  - `PremiumCustomer`: Inherits from both `Customer` and `LoyaltyProgram` (multiple inheritance), offering loyalty rewards.

---

## 🧰 Concepts Practiced

- Inheritance (`class SubClass(BaseClass)`)
- Method overriding and extension
- Multiple inheritance and `super()`
- Clean, modular class design
- Real-world simulation using OOP

---

## 💻 How to Run

```bash
python Day-18Code.py
