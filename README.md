# 🔐 Advanced Login System (Python Project)

## 📌 Objective

This project is a beginner-friendly Python program that simulates a secure login system with limited attempts, validation, and user feedback.

---

## 🧠 Features

* Takes username and password as input
* Validates credentials:

  * Username = `admin`
  * Password = `1234`
* Allows only **3 login attempts**
* Displays:

  * Remaining attempts
  * Error messages (wrong username/password)
* Security features:

  * Hint after 2 failed attempts
  * Warning on last attempt
  * Account lock after 3 failed attempts

---

## 🛠️ Technologies Used

* Python (Basic)
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`)

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the file as `login_system.py`
3. Run the program:

```id="z3h9k2"
python login_system.py
```

---

## 💻 Sample Output

```id="u5w8q1"
Enter Username: admin
Enter Password: 1111

Wrong password
Hint: Password is a 4-digit number
Attempts left: 2
```

---

## ⚠️ Security Logic

* If username is incorrect → "Username not found"
* If password is incorrect → "Wrong password"
* After 3 failed attempts → "Account locked"

---

## 🚀 Future Improvements

* Store multiple users (using dictionary)
* Hide password input
* Add OTP verification
* Connect to database

---

## 👨‍💻 Author

* Chandu

