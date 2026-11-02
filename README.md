# Library Management System

A Library Management System developed using the **Frappe Framework (Version 16)** and Python. This application helps manage library members, articles, memberships, and book issue/return transactions.

## Project Overview

The application provides a structured way to manage library operations using Frappe DocTypes and Python Controllers.

## Technologies Used

* Python
* Frappe Framework – Version 16
* JavaScript
* MariaDB
* HTML / CSS
* VS Code
* Docker
* Git & GitHub

## Features

* Library Member Management
* Library Article Management
* Library Membership Management
* Library Transaction Management
* Book Issue and Return
* Automatic Article Status Updates
* Transaction Validation using Python Controllers
* Automatic Document Naming

## DocTypes

### 1. Library Member

Stores library member information.

### 2. Library Article

Stores article details such as article name, author, ISBN, publisher, description, and availability status.

### 3. Library Membership

Manages member subscriptions, membership dates, and payment status.

### 4. Library Transaction

Manages book issue and return transactions.

## Business Logic

The Library Transaction controller uses Python document lifecycle methods:

* `validate()` – Checks article availability and transaction conditions.
* `on_submit()` – Updates the article status when a transaction is submitted.
* `frappe.get_doc()` – Retrieves Library Article documents.

### Transaction Workflow

**Issue:**

* Checks the article status.
* Updates the status to `Issued` after submission.

**Return:**

* Checks whether the article is currently issued.
* Updates the status to `Available` after submission.

## Installation

Make sure Frappe Bench is installed and configured.

```bash
cd /path/to/frappe-bench

bench get-app https://github.com/Manjimaa-m/library-management-system.git --branch main

bench --site your-site-name install-app library_management

bench --site your-site-name migrate
```

## Project Repository

GitHub: https://github.com/Manjimaa-m/library-management-system

## Developer

**GitHub:** Manjimaa-m

## License

MIT License
