# To-Do License Application

## Description
This project is a Python-based application with license authentication.
The program can only be used if a valid license key is provided and the license belongs to the correct user.

After successful license validation, the user gains access to a simple To-Do manager where tasks can be added, viewed, and deleted.

The project is developed as part of a **Tverrfaglig oppdrag / Datasikkerhet** assignment.

---

## Features
- License authentication using a license key and user email
- License verification against a local SQLite database
- Hashed license keys (SHA-256) for improved data security
- Expiration date and active/inactive license control
- Simple To-Do manager (add, view, delete tasks)
- Compiled to a Windows `.exe` file using PyInstaller

---

## Technologies Used
- Python 3
- SQLite
- PyInstaller

---

## How It Works
1. The user starts the application.
2. The user enters their email and license key.
3. The program validates:
   - that the license exists
   - that the license belongs to the correct user
   - that the license is active and not expired
4. If validation is successful, the To-Do application becomes available.
5. Tasks are stored locally in a text file.

---


---

## Security Considerations
- License keys are not stored in plain text.
- SHA-256 hashing is used to protect license data.
- Access to application functionality is restricted by license authentication.


