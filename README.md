# Banking_Simulation_Project_With_Report

# ABC Bank Simulation System

## Overview

ABC Bank Simulation System is a desktop banking application developed using Python and Tkinter. The project simulates core banking operations such as account creation, deposits, withdrawals, balance inquiries, fund transfers, and account management. It is designed for educational purposes to demonstrate the implementation of GUI programming, database management, and banking workflows.

---

## Features

### Customer Operations

* Open New Account
* Customer Login
* Deposit Money
* Withdraw Money
* Balance Inquiry
* Fund Transfer
* Change Password
* Update Profile Information
* View Account Details

### Administrative Operations

* Admin Login
* Manage Customer Accounts
* View Customer Records
* Search Account Information
* Monitor Transactions

### Security Features

* CAPTCHA Verification
* Password Authentication
* Account Number Generation
* Secure Login Validation

### Additional Features

* Email Notification on Account Creation
* Customer Profile Picture Support
* SQLite Database Integration
* User-Friendly Graphical Interface

---

## Technologies Used

* Python 3.x
* Tkinter (GUI Development)
* SQLite3 (Database)
* Pillow (Image Processing)
* SMTP / Gmail API (Email Notifications)

---

## Project Structure

project/

├── project_part_16.py # Main Application

├── dbhandler.py # Database Operations

├── mailhandler.py # Email Services

├── mygenerator.py # Account Number & Password Generator

├── bank.sqlite # SQLite Database

├── ABC_bank_logo.png # Bank Logo

├── rbi_logo.png # RBI Logo

└── default.jpg # Default Profile Image

---

## Database

The application uses SQLite for storing:

* Customer Information
* Account Details
* Login Credentials
* Transaction Records

Database File:

bank.sqlite

---

## Installation

### 1. Clone or Download the Project

```bash
git clone <repository-url>
```

### 2. Install Required Packages

```bash
pip install pillow
```

### 3. Run the Application

```bash
python mainproject.py
```

---

## Screens Included

* Welcome Screen
* Customer Login Screen
* Admin Login Screen
* Open Account Screen
* Deposit Screen
* Withdraw Screen
* Fund Transfer Screen
* Balance Inquiry Screen
* Account Management Screen

---

## Learning Objectives

This project demonstrates:

* Python Programming
* Tkinter GUI Development
* SQLite Database Management
* Event Driven Programming
* Email Integration
* Basic Banking System Design

---

## Future Enhancements

* Transaction History Module
* ATM Simulation
* Interest Calculation
* Account Statement Generation
* PDF Report Generation
* OTP Based Authentication
* Dark Mode Interface

---

## Author

Sanskar Patel

Python Developer | Banking System Project

---

## Disclaimer

This project is developed solely for educational and learning purposes. It is a banking simulation and should not be used for real financial transactions.
