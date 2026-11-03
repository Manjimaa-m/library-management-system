# Library Management System

A Library Management System developed using **Python and Frappe Framework v16**. This application helps manage library members, articles, memberships, and book issue/return transactions.

## Project Overview

This project demonstrates how to build a library management application using Frappe DocTypes, document lifecycle methods, and Python controllers.

## Technologies Used

* Python
* Frappe Framework v16
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

Stores library member details such as name, email, phone number, and address.

### 2. Library Article

Stores article details including article name, author, ISBN, publisher, description, image, and availability status.

### 3. Library Membership

Manages library membership details, membership dates, and payment status.

### 4. Library Transaction

Manages book issue and return transactions by linking library members and articles.

## Business Logic

The Library Transaction controller uses Frappe document lifecycle methods:

* **`validate()`** – Checks article availability and validates issue/return conditions.
* **`on_submit()`** – Updates the article status when a transaction is submitted.
* **`frappe.get_doc()`** – Retrieves Library Article documents for processing.

### Transaction Workflow

**Issue**

1. Checks whether the article is available.
2. Prevents issuing an article that is already issued.
3. Updates the article status to `Issued` after submission.

**Return**

1. Checks whether the article is currently issued.
2. Prevents returning an article that is not issued.
3. Updates the article status to `Available` after submission.

## Screenshots

Application screenshots are available in the [`screenshots`](screenshots/README.md) folder.

## Installation

Make sure Frappe Bench is installed and configured.

```bash
cd /path/to/frappe-bench

bench get-app https://github.com/Manjimaa-m/library-management-system.git --branch main

bench --site your-site-name install-app library_management

bench --site your-site-name migrate
```

## Project Repository

[GitHub Repository](https://github.com/Manjimaa-m/library-management-system)

## Developer

**GitHub:** [Manjimaa-m](https://github.com/Manjimaa-m)

## License

MIT License
